from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

# Dropbox API Token URL
DROPBOX_TOKEN_URL = "https://api.dropboxapi.com/oauth2/token"

# HTML template for the form page
form_template = '''
<h1>Dropbox Refresh Token Generator</h1>
<form action="/get-refresh-token" method="post">
    <label for="client_id">Client ID:</label><br>
    <input type="text" id="client_id" name="client_id" required><br>
    <label for="client_secret">Client Secret:</label><br>
    <input type="text" id="client_secret" name="client_secret" required><br>
    <label for="authorization_code">Authorization Code:</label><br>
    <input type="text" id="authorization_code" name="authorization_code" required><br><br>
    <input type="submit" value="Get Refresh Token">
</form>
'''

@app.route('/')
def home():
    return render_template_string(form_template)

@app.route('/get-refresh-token', methods=['POST'])
def get_refresh_token():
    # Retrieve user inputs from form
    client_id = request.form['client_id']
    client_secret = request.form['client_secret']
    authorization_code = request.form['authorization_code']

    # Make the request to Dropbox to exchange the code for a refresh token
    token_response = requests.post(DROPBOX_TOKEN_URL, data={
        'code': authorization_code,
        'grant_type': 'authorization_code',
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': "https://www.google.com"  # Update to the actual registered redirect URI
    })

    # Parse the JSON response
    token_data = token_response.json()

    # Check if we received a refresh token
    if 'refresh_token' in token_data:
        refresh_token = token_data['refresh_token']
        return f'''
        <h1>Refresh Token Received</h1>
        <p>Refresh Token: {refresh_token}</p>
        <p>Save this token securely to allow your app to access Dropbox data.</p>
        '''
    else:
        # Display the error if something went wrong
        error_message = token_data.get("error_description", "Unknown error occurred")
        return f"Failed to retrieve refresh token: {error_message}", 400

if __name__ == '__main__':
    app.run(debug=True)
