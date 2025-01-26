# good code to get refresh token 26/1/2024

import dropbox
from dropbox import DropboxOAuth2FlowNoRedirect

# Replace these with your app's key and secret
APP_KEY = 'hgabefdupnfjf7e'
APP_SECRET = 'ul0anfyr08to982'

# Set up the OAuth2 flow with offline access
auth_flow = DropboxOAuth2FlowNoRedirect(
    APP_KEY,
    APP_SECRET,
    token_access_type='offline'  # Request offline access to get a refresh token
)

# Get the authorization URL
authorize_url = auth_flow.start()
print("1. Go to: " + authorize_url)
print("2. Click \"Allow\" (you might have to log in first).")
print("3. Copy the authorization code.")
auth_code = input("Enter the authorization code here: ").strip()

# Exchange the authorization code for an access token and refresh token
try:
    oauth_result = auth_flow.finish(auth_code)
    print("Access Token:", oauth_result.access_token)
    print("Refresh Token:", oauth_result.refresh_token)  # This should now have a value
    print("User ID:", oauth_result.user_id)
except Exception as e:
    print("Error: %s" % (e,))