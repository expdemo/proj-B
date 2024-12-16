def main():
  org_repo = os.environ["ORG_REPO"]
  token = os.environ["GITHUB_TOKEN"]
  pr_details = os.environ["PR_details"]
  print(org_repo)
  print(token)
  print(pr_details)
  print("Hellooooo")

if __name__ == "__main__":
    main()
