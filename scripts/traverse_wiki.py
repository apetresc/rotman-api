import requests
from bs4 import BeautifulSoup
import time
import urlparse


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
  return [urlparse.urljoin(DOMAIN, a["href"]) for a in soup.find(id="content").find_all('a') if a.get("href") and a["href"].startswith('/')]


ROOT_NODE = "https://en.wikipedia.org/wiki/Star_Wars"


if __name__ == "__main__":
  bft(ROOT_NODE)
