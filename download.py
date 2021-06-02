import requests


url = 'https://www.worldnovel.online/novel/ovrgrd/'
r = requests.get(url, allow_redirects=True)

open('Overgeared.htm', 'wb').write(r.content)