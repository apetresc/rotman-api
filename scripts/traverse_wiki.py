import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin


DOMAIN = "https://en.wikipedia.org/"


def bft(root):
  seen = set()
  q = [root]

  while q:
    n = q.pop(0)
    if n not in seen:
      print(n)
      seen.add(n)
      q += get_links(n)
    time.sleep(1)

def get_links(url):
  html = requests.get(url).content
  soup = BeautifulSoup(html, 'html.parser')
  return [urljoin(url, a["href"]) for a in soup.select('#content a') if a.get("href", "").startswith('/')]


ROOT_NODE = "https://en.wikipedia.org/wiki/Rotman_School_of_Management"


if __name__ == "__main__":
  bft(ROOT_NODE)
