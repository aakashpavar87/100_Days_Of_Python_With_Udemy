from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year do you want to travel to ? Type the Date in this Format (YYYY-MM-DD) : ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
soup = BeautifulSoup(response.text, "html.parser")
song_title = [song.getText().strip() for song in soup.select(selector=".lrv-u-width-100p ul li h3")]

SPOTIFY_ID = "3c1e4abb77754671a6b12211c4325bf1"
SPOTIFY_KEY = "a13ace54e6bf4c069c12a37a1521dfa5"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_ID, 
    scope="playlist-modify-private",
    client_secret=SPOTIFY_KEY,
    redirect_uri="https://example.com",
    cache_path="tokens.txt",
    show_dialog=True))

user_key = sp.current_user()["id"]

playlist = sp.user_playlist_create(user=user_key, name=f"{date} BillBoard 100", public=False)["id"]

song_uris = []

year = date.split("-")[0]
for song in song_title:
    try:
        track_info = sp.search(q=f"track:{song} year:{year}", type='track')
        song_uris.append(track_info["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"{song.strip()} doesn't exist in spotify so skipped.")
        continue

#print(len(song_uris))   

sp.playlist_add_items(playlist_id=playlist, items=song_uris[:100])
