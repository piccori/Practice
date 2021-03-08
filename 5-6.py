import requests
from bs4 import BeautifulSoup

BASE_URL = "http://en.wikipedia.org"
HEADERS = {'User-Agent': 'Mozilla/5.0'}


def get_Nobel_soup():
    response = requests.get(
        BASE_URL + '/wiki/List_of_Nobel_laureates', headers=HEADERS)
    return BeautifulSoup(response.content, "lxml")


print(get_Nobel_soup())
