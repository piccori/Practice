from bs4 import BeautifulSoup
import requests

BASE_URL = 'http://en.wikipedia.org'
HEADERS = {'User-Agent': 'Mozilla/5.0'}


def get_Nobel_soup():
    response = requests.get(
        BASE_URL + '/wiki/List_of_Nobel_laureates')
    return BeautifulSoup(response.content, 'html.parser')


soup = get_Nobel_soup()
soup.find('table', {'class': 'wikitable sortable'})
soup.select('table.sortable.wikitable')
table = soup.select_one('table.sortable.wikitable')
print(table)


def get_column_titles(table):

    cols = []
    for th in table.select_one('tr').select('th')[1:]:
        link = th.select_one('a')
        if link:
            cols.append({'name': link.text,
                         'href': link.attrs['href']})
        else:
            cols.append({'name': th.text, 'href': None})
        return cols


get_column_titles(table)


def get_Nobel_winners(wikitable):
    cols = get_column_titles(table)
    winners = []
    for row in tabel.select('tr')[1:-1]:
        year = int(row.select_one('td').text)
        for i, th in enumerate(row.select('td')[1:]):
            for winner in td.select('a'):
                href = winner.attrs['href']
                if not href.startswith('#endnote'):
                    winners.append({
                        'year': year,
                        'vategory': cols[i]['name'],
                        'name': winner.text,
                        'link': winner.attrs['href']})
        return winners


get_Nobel_winners(wikitable)
