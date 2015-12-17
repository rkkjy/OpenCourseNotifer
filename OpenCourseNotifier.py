import requests
from bs4 import BeautifulSoup

url = "https://registrar.ucdavis.edu/courses/search/index.cfm"

r = requests.get(url)
soup = BeautifulSoup(r.content)


