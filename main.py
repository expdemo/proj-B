import os
from github import Github

# Get environment variables
repo_name = os.getenv('ORG_REPO')
pr_number = os.getenv('PR_details')
print("in main : ",repo_name, len(pr_number))
