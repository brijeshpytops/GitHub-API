import requests

token = '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'

owner = 'brijeshpytops'
repo = '9AUG23-py-brijesh-4'

url = f'https://api.github.com/repos/{owner}/{repo}'

headers = {
    'Authorization': f'token {token}'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    repository_data = response.json()
    # Process the repository data as needed

    print(repository_data)
else:
    print(f'Error: {response.status_code} - {response.text}')