import re
import os
import git
import git.exc
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# ANSI escape codes for coloring
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'

class DocumentProcessor:
    def __init__(self, internal_docs_path, external_docs_base_path, acceptable_extensions=None):
        self.internal_docs_path = internal_docs_path
        self.external_docs_base_path = external_docs_base_path
        self.acceptable_extensions = acceptable_extensions or ['.md']  # Default to .md if not provided
        self.tag = self.get_current_git_tag()
        self.external_docs_path = os.path.join(self.external_docs_base_path, self.tag)
    
    def get_current_git_tag(self):
        '''Fetch the current git tag'''
        try:
            repo = git.Repo(search_parent_directories=True)
            tag = repo.git.describe('--tags', always=True)  # Use '--tags' with 'always' to handle no tags case
            logger.info(f"{YELLOW}Recent repo's tag is: {tag} {RESET}")
            return tag
        except git.exc.GitCommandError as e:
            logger.error(f"{RED}Error fetching Repo's tag: {e}{RESET}")
            return "latest"
    
    def remove_internal_sections(self, content):
        '''Remove sections marked with <!-- start-internal --> and <!-- end-internal -->'''
        return re.sub(r'<!-- start-internal -->.*?<!-- end-internal -->', '', content, flags=re.DOTALL)
    
    def process_file(self, internal_file, external_file):
        '''Process a single file to remove internal sections'''
        logger.info(f"{YELLOW}Processing file: {internal_file}{RESET}")
        try:
            with open(internal_file, 'r', encoding='utf-8') as input_file:
                content = input_file.read()
            cleaned_content = self.remove_internal_sections(content)

            with open(external_file, 'w', encoding='utf-8') as output_file:
                output_file.write(cleaned_content)

            logger.info(f"{YELLOW}Processed file: {internal_file} -> {external_file}{RESET}")
        except Exception as e:
            logger.error(f"{RED}Error processing file {internal_file}: {e}{RESET}")

    def process_directory(self, internal_docs_path=None, external_docs_path=None):
        '''Process all files in the directory and replicate the structure'''
        if internal_docs_path is None:
            internal_docs_path = self.internal_docs_path
        if external_docs_path is None:
            external_docs_path = self.external_docs_path

        logger.info(f"{YELLOW}Starting directory processing: {internal_docs_path} -> {external_docs_path}{RESET}")
        for root, dirs, files in os.walk(internal_docs_path):
            relative_path = os.path.relpath(root, internal_docs_path)
            target_root = os.path.join(external_docs_path, relative_path)
            os.makedirs(target_root, exist_ok=True)

            logger.info(f"{YELLOW}Processing directory: {root}{RESET}")
            for file in files:
                if any(file.endswith(ext) for ext in self.acceptable_extensions):
                    internal_file = os.path.join(root, file)
                    external_file = os.path.join(target_root, file)
                    self.process_file(internal_file, external_file)
                else:
                    logger.info(f"{YELLOW}Skipping file (unacceptable extension): {file}{RESET}")

if __name__ == "__main__":
    # Paths based on your provided directory structure
    internal_directory = 'internal_docs/'
    external_directory = 'external_docs/'
    acceptable_extensions = ['.md', '.txt', '.rst']

    processor = DocumentProcessor(internal_directory, external_directory, acceptable_extensions)
    processor.process_directory()