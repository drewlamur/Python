from bs4 import BeautifulSoup
import requests

page = requests.get('http://www.lipsum.com/')
soup = BeautifulSoup(page.text)

print soup.html