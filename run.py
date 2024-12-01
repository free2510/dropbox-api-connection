import requests

# Replace these with your actual values
client_id = 'wxm9lux682kowpc'
client_secret = 'nagtdb0sck0yu9j'
redirect_uri = 'https://www.google.com'
authorization_code = '5_j4SWNFudsAAAAAAAAARrUTmdmBPB4b2bsz8OqVONc'

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
