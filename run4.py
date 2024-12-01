import requests
import webbrowser
import json

# Dropbox App credentials
CLIENT_ID = "wxm9lux682kowpc"
CLIENT_SECRET = "nagtdb0sck0yu9j"

# Replace with your registered redirect URI
REDIRECT_URI = "https://www.google.com"  # Ensure this matches your Dropbox app settings

# Dropbox authorization and token endpoints
DROPBOX_AUTH_URL = "https://www.dropbox.com/oauth2/authorize"
DROPBOX_TOKEN_URL = "https://api.dropboxapi.com/oauth2/token"

def get_auth_code():
    """
    Generates the Dropbox authorization URL, opens it in the browser, 
    and prompts the user to input the authorization code.
    """
    auth_url = f"{DROPBOX_AUTH_URL}?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}"
    print(f"Visit this URL to authorize the application:\n{auth_url}\n")
    
    # Open the URL in the user's browser
    webbrowser.open(auth_url)
    
    # Prompt the user to paste the authorization code
    auth_code = input("Paste the authorization code here: ").strip()
    return auth_code

def exchange_code_for_tokens(auth_code):
    """
    Exchanges the authorization code for access and refresh tokens.
    """
    response = requests.post(DROPBOX_TOKEN_URL, data={
        'code': auth_code,
        'grant_type': 'authorization_code',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI
    })

    # Parse and return the response
    if response.status_code == 200:
        token_data = response.json()
        print("\nToken Exchange Successful!\n")
        print(json.dumps(token_data, indent=4))
        return token_data
    else:
        print(f"\nFailed to exchange tokens: {response.status_code}\n{response.text}")
        return None

def main():
    """
    Main flow for Dropbox OAuth2 token retrieval.
    """
    print("Dropbox Authorization Flow")
    
    # Step 1: Get Authorization Code
    auth_code = get_auth_code()
    if not auth_code:
        print("No authorization code provided. Exiting.")
        return
    
    # Step 2: Exchange Authorization Code for Tokens
    token_data = exchange_code_for_tokens(auth_code)
    if not token_data:
        print("Could not retrieve tokens. Exiting.")
        return

    # Step 3: Display Key Information
    print("\n--- Key Information ---")
    access_token = token_data.get("access_token", "N/A")
    refresh_token = token_data.get("refresh_token", "N/A")
    scope = token_data.get("scope", "N/A")
    expires_in = token_data.get("expires_in", "N/A")

    print(f"Access Token: {access_token}")
    print(f"Refresh Token: {refresh_token}")
    print(f"Scope: {scope}")
    print(f"Expires In: {expires_in} seconds")

if __name__ == "__main__":
    main()
