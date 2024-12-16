import os

def main():
  org_repo = os.environ["ORG_REPO"]
  pr_details = os.getenv(PR_details)
  print("Hellooooo")
  print(org_repo)
  print(pr_details)
  print("Hellooooo")

if __name__ == "__main__":
    main()
