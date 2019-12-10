import requests
from bs4 import BeautifulSoup
import json
import unicodedata


session = requests.Session()
url = 'https://cs.ucsb.edu/education/courses/descriptions'
headers = {'Accept-Encoding': 'identity'}
r = requests.get(url, headers=headers)

decoded_content = ""
for line in r.iter_lines():
    if line:
        decoded_line = line.decode('utf-8')
        decoded_content += decoded_line


soup = BeautifulSoup(decoded_content, 'html.parser')

table = (soup.tbody.prettify())
soup = BeautifulSoup(table)

links = []
for link in soup.find_all('a'):
    links.append(link.get('href'))

print(links)