# Documentation Automation
This repository automates the generation of external documentation artifacts from internal documentation sources using GitHub Actions and Python scripts. The process ensures that confidential sections of the documentation are excluded from the external artifacts. The workflow is triggered by pushing changes to a specific branch and creating tags to organize the releases.
## Repository Structure
```
.
├── external_docs
├── internal_docs
│   ├── Buildroot
│   │   └── README.md
│   └── Yocto
│       └── README.md
├── LICENSE
├── README.md
└── scripts
    ├── create_external_document.py
    └── requirements.txt
```

### Sample Documents
The internal_docs folder contains sample documentation for demonstration purposes. These documents include sections marked as internal, which will be filtered out during the generation of external documents.
## Use Case: Updating Documents and Creating Artifacts
### Step-by-Step Process
Create/Update Documents:
Make necessary updates to your documents in the internal_docs directory.
Commit and Push Changes:
Commit your changes with a meaningful commit message.
```

git add .
git commit -m "Update documents for upcoming tag"
git push origin feature/update_internal_documents
```
Create and Push a Tag:
Create a tag for the changes.
```
git tag <tag_name>
git push origin <tag_name>
```
Trigger the Workflow:
The GitHub Action will be triggered on the push to feature/update_internal_documents, fetch the latest tag, process the documents, and upload the artifacts.
Verify the Workflow:
Check the logs of the workflow run in the Actions tab on GitHub to ensure the environment variables are set correctly and the artifact is named as expected.
Download and Verify the Artifact:
Download the artifact from the Actions tab in your GitHub repository. The artifact will be named using the following schema:
``` ${REPO_NAME}-${TAG_NAME}-${COMMIT_HASH}-${DATE}.```
## Artifacts
Artifacts are the external documentation generated by the GitHub Action. They are uploaded to GitHub and can be downloaded for use.
### Naming Schema
The artifacts are named using the following schema:
```

${REPO_NAME}-${TAG_NAME}-${COMMIT_HASH}-${DATE}
```

REPO_NAME: The name of the repository.
TAG_NAME: The current tag of the commit.
COMMIT_HASH: The short hash of the commit.
DATE: The date when the artifact was created.
How to Download Artifacts
Go to the Actions Tab:
Navigate to the Actions tab in your GitHub repository.
Select the Workflow Run:
Click on the workflow run that corresponds to your recent push to ```feature/update_internal_documents.```
Download the Artifact:
In the workflow run details, find the "Artifacts" section. Click on the artifact to download it.
Marking Internal Sections
To mark sections of your documents as internal, enclose the content within special HTML comments as shown below:
```
<!-- start-internal -->
## Internal Use Only

The following information is confidential and should not be shared publicly. 

### API Keys

- API Key for Service A: `abcd1234`
- API Key for Service B: `efgh5678`

### Internal URLs

- Internal Dashboard: `https://internal.example.com/dashboard`
- Internal API: `https://api.internal.example.com`

### Internal Procedures

1. Access the internal dashboard using your company credentials.
2. Use the internal API keys to authenticate your requests.
3. Follow the internal SOPs for handling sensitive data.
<!-- end-internal -->
```
## Benefits of This Process
Separation of Concerns: Keeps internal and external documentation separate, ensuring that confidential information is not inadvertently exposed.
Automation: Automates the generation of external documents, reducing the risk of human error and saving time.
Version Control: Uses Git tags to version the documentation, making it easy to track changes and maintain historical records.
Consistency: Ensures that all external documentation is consistently generated and up-to-date with the latest internal changes.
By following these steps, you can ensure that your documents are updated and artifacts are generated correctly based on the tags, all while using a single branch (feature/update_internal_documents). This process helps maintain the integrity and confidentiality of your documentation.

