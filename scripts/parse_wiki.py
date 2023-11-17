import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Rotman_School_of_Management"

html = requests.get(URL).content
soup = BeautifulSoup(html, 'html.parser')

print("Text on the page:")
print('\n'.join(p.get_text() for p in soup.find(id="content").find_all('p')))
