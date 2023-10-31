import requests

token = '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'
username = 'brijeshpytops'

url = f'https://api.github.com/users/{username}'

headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'  # Specify the API version
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    user_data = response.json()
    print(f'Username: {user_data["login"]}')
    print(f'Name: {user_data.get("name", "Not provided")}')
    print(f'Location: {user_data.get("location", "Not provided")}')
    print(f'Public Repositories: {user_data["public_repos"]}')
    # Add more fields as needed
else:
    print(f'Error: {response.status_code} - {response.text}')
