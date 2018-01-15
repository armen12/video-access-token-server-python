import os
from flask import Flask, jsonify, request
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VideoGrant
from dotenv import load_dotenv, find_dotenv

app = Flask(__name__)
load_dotenv(find_dotenv())

@app.route('/')
def token():
    # Get credentials for environment variables
    account_sid = 'ACbce0865b277c75152da6fc469b650463'
    api_key = 'SK2e4b45c9cb8835c6ad1a614c3346b209'
    api_secret = 'l6GKan4KkOKCmiktZDTmhahRY7q2aTPz'

    # Create an Access Token
    token = AccessToken(account_sid, api_key, api_secret)

    # Set the Identity of this token
    token.identity = request.values.get('identity') or 'identity'
    
    # Grant access to Video
    grant = VideoGrant()
    grant.room = request.values.get('room')
    token.add_grant(grant)

    # Return token
    return token.to_jwt()


app.run(host=os.environ['HOST'],port=os.environ['PORT'], debug=True)
