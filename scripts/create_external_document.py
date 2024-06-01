import re
import os
import git
import git.exc
import logging

logging.basicConfig(level=logging.INFO,format='%(message)s')
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
            tag = repo.git.describe('--tags') 
            logger.info(f"{YELLOW}Recent repo's tag is :{tag} {RESET}")
            return tag
        except git.exc.GitCommandError:
            logger.error(f"{RED}Error fetching Repo's tag{RESET}")
            return "latest"
            
    
    def remove_internal_section(self,content):
        '''Remove sections marked with <!-- start-internal --> and <!-- end-internal -->"'''
        pass
    
    def process_file(self,internal_file,external_file):
        '''Process all files in the directory and replicate the structure'''
        pass
    
    def process_directory(self,internal_docs_path=None,external_docs_base_path=None):
        '''Process all files in the directory and replicate the structure'''
        pass



if __name__ == "__main__":
    # Paths based on your provided directory structure
    internal_directory = '../internal_docs/'
    external_directory = '../external_docs/'
    acceptable_extensions = ['.md', '.txt', '.rst']

    processor = DocumentProcessor(internal_directory, external_directory, acceptable_extensions)
    processor.process_directory()
    
    