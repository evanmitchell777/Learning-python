#this program scrapes images from any link you give it!
from bs4 import BeautifulSoup
import requests
import urllib.request
url = "insert url here "
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")


images = soup.find_all("img")
number = 0

for image in images:
    image_src = image["src"]
print(image_src)
urllib.request.urlretrieve(image_src)
number += 1
