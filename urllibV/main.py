import urllib.request
from bs4 import BeautifulSoup
import json
import unicodedata

r = urllib.request.urlopen('https://cs.ucsb.edu/education/courses/descriptions')
decoded_content = r.read()
soup = BeautifulSoup(decoded_content, 'html.parser')
table = (soup.tbody.prettify())
soup = BeautifulSoup(table, 'html.parser')
scrapedInfo = {}

for link in soup.find_all('a'):
    r = urllib.request.urlopen('https://cs.ucsb.edu'+link.get('href'))
    soup = BeautifulSoup(r.read(), 'html.parser')
    contentName = soup.find(id='content').find('div', recursive = False).find('div', recursive = False).find('div', recursive = False)
    try:
        key = contentName.get_text().split(' ')[1]
    except IndexError:
        key = contentName.get_text()[8:]
    key = 'CS'+key.strip(',')
    scrapedInfo[key] = {'title': soup.find(id = 'page-title').get_text(), 'desc': soup.find(id = 'block-system-main').prettify()}
    print(soup.find(id = 'page-title').get_text())
    print(soup.find(id = 'block-system-main').prettify())

fout = open('info.json', 'w')
fout.write(json.dumps(scrapedInfo))
fout.close()