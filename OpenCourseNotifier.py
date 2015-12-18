import requests
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time 

CRN = input("Enter CRN of class: ") #Obtain CRN from user
url = "https://registrar.ucdavis.edu/courses/search/index.cfm" #define URL to be class search website

#must dynamically generate html 
driver = webdriver.Chrome()
driver.get(url)

#enter in CRN into text box 
enterCRN = driver.find_element_by_id("course_number")
enterCRN.send_keys(CRN)

#click search button
searchButton = driver.find_element_by_name("search")
searchButton.click()

time.sleep(5) #wait to load 

#obtain generated html code into data 
data = BeautifulSoup(driver.page_source, "html.parser")

for line in data.find_all(id = "courseResultsDiv"): 
	space = line.find_all(title = "View Course Detail")[2].find("em").get_text()
	space = int(space.strip())
	print space
	print (space == 1)

driver.close() #close driver 
		
	