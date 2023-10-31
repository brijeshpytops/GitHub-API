import requests

token = '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'

owner = 'brijeshpytops'
repo = '9AUG23-py-brijesh-4'

url = f'https://api.github.com/repos/{owner}/{repo}/issues'

headers = {
    'Authorization': f'token {token}',
    'Content-Type': 'application/json'
}

# Issue data to create a new issue
issue_data = {
    'title': 'New Issue Title',
    'body': 'This is the description of the new issue.'
}

response = requests.post(url, headers=headers, json=issue_data)

if response.status_code == 201:
    created_issue = response.json()
    print(f'Issue created successfully. Issue number: {created_issue["number"]}')
else:
    print(f'Error: {response.status_code} - {response.text}')
