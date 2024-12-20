import os
from github import Github

# Get environment variables
repo_name = os.getenv('ORG_REPO')
pr_number = os.getenv('PR_details')
print("in main : ",repo_name, len(pr_number))
github_token = os.getenv('GITHUB_TOKEN')
print("in main : ",github_token, len(github_token))
# Initialize GitHub client
g = Github(github_token)
repo = g.get_repo(repo_name)

# Fetch the pull request by number
pr = repo.get_pull(int(pr_number))

# List of prohibited names to check against
prohibited_names = ['bad_name', 'forbidden_term']

# Check if any prohibited names are present in PR title or body
def check_for_prohibited_names(pr):
    # Check PR title
    if any(name in pr.title for name in prohibited_names):
        return f"Prohibited name found in title: {pr.title}"

    # Check PR body
    if any(name in pr.body for name in prohibited_names):
        return f"Prohibited name found in body: {pr.body}"

    return "No prohibited names found."

# Execute check
result = check_for_prohibited_names(pr)
print(result)
