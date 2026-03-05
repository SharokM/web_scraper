import requests
from bs4 import BeautifulSoup

honey_badger = requests.get("https://en.wikipedia.org/wiki/Honey_badger")
honey_badger.raise_for_status()
honey_badger_html = honey_badger.text.encode("utf-8")
honey_badger_soup = BeautifulSoup(honey_badger_html, 'html.parser')

h2 = honey_badger_soup.find_all("h2")
print("Number of h2 tags:", len(h2))
for index in h2:
    print(index)
    print(index.text.strip())

links = honey_badger_soup.find_all("a")
print("First 6 links:", links[:6])

images = honey_badger_soup.find_all("img")
print("Last 6 images:", images[4:9])