import os

def main():
  org_repo = os.environ["ORG_REPO"]
  pr_num = os.getenv("PR_details")
  print("Hellooooo")
  print(org_repo)
  print(type(pr_num))
  print(pr_num)
  print("Hellooooo")

if __name__ == "__main__":
    main()
