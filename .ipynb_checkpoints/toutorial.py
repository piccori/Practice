from bs4 import BeautifulSoup
import requests

BASE_URL = 'http://en.wikipedia.org'

HEADERS = {'User-Agent': 'Mozilla/5.0'}


def get_Nobel_soup():
    response = requests.get(
        BASE_URL+'/wiki/List_of_Nobel_laureates',
        headers=HEADERS)
    return BeautifulSoup(response.content, "lxml")


soup = get_Nobel_soup()
soup = find('table', {'class': 'wikitable sortable'})
