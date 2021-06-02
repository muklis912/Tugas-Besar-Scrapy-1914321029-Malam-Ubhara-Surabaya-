import requests
from bs4 import BeautifulSoup
url = "https://www.worldnovel.online/rkr/prologue-chapter-1/"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
for body in soup.find_all('p'):
   print(body.text)