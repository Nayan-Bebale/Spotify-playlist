import time
from flask import Flask, request, url_for, redirect, session
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os


app = Flask(__name__)

TOKEN_INFO = "token_info"


@app.route('/')
def login():
    sp_oauth = create_spotify_ouath()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)


@app.route('/redirect')
def redirectPage():
    sp_oauth = create_spotify_ouath()
    session.clear()
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    session[TOKEN_INFO] = token_info
    return redirect(url_for('getTracks', _external=True))


@app.route('/getTracks')
def getTracks():
    try:
        token_info = get_token()
    except "HTTPError":
        print("user not logged in")
        return redirect('/')
    sp = spotipy.Spotify(auth=token_info['access_token'])
    return sp.current_user_top_tracks(time_range='medium_term', limit=20, offset=0)
    # return sp.current_user_saved_tracks(limit=20, offset=0)
    # The commented line above seems to work but the one with top_tracks throws an error.


def get_token():
    token_info = session.get(TOKEN_INFO, None)
    if not token_info:
        raise "exception"
    now = int(time.time())
    is_expired = token_info['expires_at'] - now < 60
    if is_expired:
        sp_oauth = create_spotify_ouath()
        token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
    return token_info


def create_spotify_ouath():
    return SpotifyOAuth(
        client_id=os.getenv("client_id"),
        client_secret=os.getenv("client_secret"),
        # Where to come back to
        redirect_uri=os.getenv("redirect_uri"),
        scope="user-library-read")


if __name__ == "__main__":
    app.run(debug=True)


