import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv, dotenv_values

#Carga de datos de .env
load_dotenv()
keys = dotenv_values()

#os.getenv(key)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv("CLIENT_ID"),client_secret=os.getenv("CLIENT_SECRET"),redirect_uri=os.getenv("REDIRECT_URI"),scope=os.getenv("SCOPE")))

def albumsRecienGuardados():
    # Puedes cambiar el limite de albumes
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
