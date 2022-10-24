import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


# creating the Spotify Client
scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
user_id = sp.current_user()["id"]


def get_song_year():
    # getting and saving the date the user wants
    url = "https://www.billboard.com/charts/hot-100/"
    target = input("Which year do you want to travel to? Type the date in this format: YYYY-MM-DD: ")
    # target = "1998-06-09"
    url += f"{target}/"
    year = target.split("-")[0]
    return url, year


def get_songs():
    # webscraping the song names and artists
    url, year = get_song_year()
    response = requests.get(url)
    data = response.text
    bs = BeautifulSoup(data, "html.parser")

    titles_raw = bs.select("li.o-chart-results-list__item h3.c-title")
    titles = [title.text.strip() for title in titles_raw]
    artists_raw = bs.select(r"li.o-chart-results-list__item.\/\/.lrv-u-flex-grow-1.lrv-u-flex.lrv-u-flex-direction"
                            r"-column.lrv-u-justify-content-center.lrv-u-border-b-1.u-border-b-0\@mobile-max.lrv-u"
                            r"-border-color-grey-light.lrv-u-padding-l-1\@mobile-max > span")
    artists = [artist.text.strip() for artist in artists_raw]
    song_dict = dict(zip(artists, titles))
    return song_dict, year


def create_song_uris():
    # creating a list of URI for every song title (if its found)
    titles, year = get_songs()
    uri_list = []
    for artist, title in titles.items():
        result = sp.search(q=f"artist:{artist} track:{title} year:{year}", type="track")
        try:
            uri = result["tracks"]["items"][0]["uri"]
            uri_list.append(uri)
        except IndexError:
            print(f"Can't find the song: '{title}' on Spotify.")
    return uri_list, year


def create_playlist():
    # creating a playlist and adding all found song titles to it
    uri_list, year = create_song_uris()
    playlist = sp.user_playlist_create(user=user_id, name=f"Billboard 100 from {year}", public=False)
    playlist_id = playlist["id"]
    sp.playlist_add_items(playlist_id=playlist_id, items=uri_list)


if __name__ == "__main__":
    create_playlist()
