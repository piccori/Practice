from bs4 import BeautifulSoup
import requests


def get_nobel_winners(table):
    cols = get_column_titles(table)
    winners = []
    for row in table.select('tr')[1:-2]:
        year = str(row.select_one('td').text)
        for i, td in enumerate(row.select('td')[1:]):
            for winner in td.select('a'):
                href = winner.attrs['href']
                if not href.startswith('#endnote'):
                    winners.append({'year': year,
                                    'category': cols[i]['name'],
                                    'name': winner.text,
                                    'link': winner['href']})
    return winners


def get_column_titles(table):
    cols = []
    for th in table.select_one('tr').select('th')[1:]:
        link = th.select_one('a')
        if link:
            cols.append({'name': link.text, 'href': link.attrs['href']})
        else:
            cols.append({'name': th.text, 'href': None})
    return cols


BASE_URL = "http://en.wikipedia.org"
HEADERS = {'User-Agent': 'Mozilla/5.0'}


def get_Nobel_soup():
    response = requests.get(
        BASE_URL + '/wiki/List_of_Nobel_laureates', headers=HEADERS)
    return BeautifulSoup(response.content, "lxml")


soup = get_Nobel_soup()
table = soup.select_one('table.sortable.wikitable')
d = get_nobel_winners(table)
print(str(d).encode('UTF-8'))
