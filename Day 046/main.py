import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# creating the Spotify Client
scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
user_id = sp.current_user()["id"]

# getting and saving the date the user wants
url = "https://www.billboard.com/charts/hot-100/"
target = input("Which year do you want to travel to? Type the date in this format: YYYY-MM-DD: ")
# target = "1998-06-09"
url += f"{target}/"
year = target.split("-")[0]

# start webscraping the songtitles
response = requests.get(url)
data = response.text
bs = BeautifulSoup(data, "html.parser")
titles_raw = bs.select("li.o-chart-results-list__item h3.c-title")
titles = [title.text.strip() for title in titles_raw]

# creating a list of URI for every songtitle (if its found)
uri_list = []
for title in titles:
    result = sp.search(q=f"track:{title} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        uri_list.append(uri)
    except IndexError:
        print(f"Can't find the song: '{title}' on Spotify.")

# creating a playlist and adding all found songtitles to it
playlist = sp.user_playlist_create(user=user_id, name=f"{target} Billboard 100", public=False)
playlist_id = playlist["id"]
sp.playlist_add_items(playlist_id=playlist_id, items=uri_list)


