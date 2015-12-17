import requests
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import unittest

CRN = input("Enter CRN of class: ")

driver = webdriver.Chrome()
driver.get("https://registrar.ucdavis.edu/courses/search/index.cfm")


url = "https://registrar.ucdavis.edu/courses/search/index.cfm"

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")


