import requests
import time


# Replace these with your actual values
client_id = 'spj951z8two8un4'
client_secret = '0dpx6yc9mytplza'
refresh_token = 'Ye6EozTtiDIAAAAAAAAAASBISsv6nd16q4Ctrvb0M_jCQVQu4PP3mG6NfXthEs-A'

def refresh_access_token():
    # Set up the request parameters
    token_url = 'https://api.dropboxapi.com/oauth2/token'
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': client_id,
        'client_secret': client_secret,
    }
    
    # Make the request
    response = requests.post(token_url, data=data)
    response_data = response.json()
    
    # Check for the access token in response
    if 'access_token' in response_data:
        access_token = response_data['access_token']
        print("New Access Token:", access_token)
        return access_token
    else:
        print("Failed to retrieve access token:", response_data)
        return None

# Refresh the access token every minute
while True:
    access_token = refresh_access_token()
    if access_token:
        # You can use the new access token here for any Dropbox API calls
        pass
    
    # Wait for 1 minute before refreshing again
    time.sleep(60)
