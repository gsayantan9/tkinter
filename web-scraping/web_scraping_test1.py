from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"

page = urlopen(url=url)

html = page.read().decode("utf-8")

soup = BeautifulSoup(html,"html.parser")

print(soup)
print(soup.get_text().strip("\n"))


