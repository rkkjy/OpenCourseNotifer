import requests
from bs4 import BeautifulSoup
from selenium import webdriver 
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
#import unittest

CRN = input("Enter CRN of class: ") #Obtain CRN from user
url = "https://registrar.ucdavis.edu/courses/search/index.cfm"

driver = webdriver.Chrome()
driver.get(url)

enterCRN = driver.find_element_by_id("course_number")
enterCRN.send_keys(CRN)

searchButton = driver.find_element_by_name("search")
searchButton.click()

r = requests.get(url)
data = BeautifulSoup(r.content, "html.parser")


