# Tutorial from here: https://www.dataquest.io/blog/web-scraping-tutorial-python/

import requests
from bs4 import BeautifulSoup

URL = 'http://dataquestio.github.io/web-scraping-pages/simple.html'
page = requests.get(URL)
# help(page)
# print(page.text)
# print(page.status_code)
# print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify())
# print(list(soup.children))
# print([type(item) for item in list(soup.children)])
html = list(soup.children)[2]
body = list(html.children)[3]
# print(list(body.children))
p = list(body.children)[1]
# print(p.get_text())
