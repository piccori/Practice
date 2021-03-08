import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_Nobel_laureates'
print('Googling...' + url)  # Googleページをダウンロード中にテキストを表示
res = requests.get(url)
res.raise_for_status()

# newsページのタイトルを取得する
soup = res
soup.find('table', {'class': 'wikitable sortable'})
soup.select('table.sortable.wikitable')
table = soup.select_one('table.sortable.wikitable')
print(table)
