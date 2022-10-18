from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
data = response.text

bs = BeautifulSoup(data, "html.parser")

movies_raw = bs.select(selector="div.article-title-description__text h3.title")
movie_list = [movie.get_text() for movie in movies_raw]

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in reversed(movie_list):
        file.write(f"{movie}\n")
