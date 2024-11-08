import requests

# Replace these with your actual values
client_id = 'spj951z8two8un4'
client_secret = '0dpx6yc9mytplza'
redirect_uri = 'https://www.google.com'
authorization_code = 'tQtCNMl2fYoAAAAAAAAAo5NE-WJRHIUFYcDI3-iRDe8'

# Set up the request parameters
token_url = 'https://api.dropboxapi.com/oauth2/token'
data = {
    'code': authorization_code,
    'grant_type': 'authorization_code',
    'client_id': client_id,
    'client_secret': client_secret,
    'redirect_uri': redirect_uri,
}

# Make the request
response = requests.post(token_url, data=data)
response_data = response.json()

# Print the results
if 'access_token' in response_data and 'refresh_token' in response_data:
    print("Access Token:", response_data['access_token'])
    print("Refresh Token:", response_data['refresh_token'])
else:
    print("Failed to retrieve tokens:", response_data)
