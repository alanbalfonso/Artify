import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SCOPE

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=REDIRECT_URI,scope=SCOPE))

def get_recently_added_albums():
    results = sp.current_user_saved_albums(limit=50)
    albums = []

    for item in results["items"]:
        album = item["album"]
        album_id = album["id"]
        album_name = album["name"]
        artist_name = album["artists"][0]["name"]
        album_url = album["images"][0]["url"]
        albums.append((album_id, album_name, artist_name, album_url))

    return albums
