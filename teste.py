import requests

# GitHub API details
url = "https://api.github.com/repos/ferdleorg/test/actions/jobs/JOB_ID/rerun"
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": "Bearer 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",
    "X-GitHub-Api-Version": "2022-11-28"
}

response = requests.post(url, headers=headers)
print(response.status_code)
print(response.json())
