import requests
from bs4 import BeautifulSoup
import os


url = 'https://ikman.lk/en/ads/sri-lanka/property?sort=relevance&buy_now=0&urgent=0&query=colombo&page=1';

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

Img = soup.find_all('img')

for image in Img:
    name = image['alt']
    link = image['src']
    with open(name.replace('', '-').replace('/', '').replace('|', '') + '.jpg', 'wb') as f:
        im = requests.get(link)
        f.write(im.content)

