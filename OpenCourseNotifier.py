import requests
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time 

#################### Start function definitions ####################
def initialize(CRN, url):
	driver = webdriver.Chrome()
	driver.get(url)
	enterCRN = driver.find_element_by_id("course_number")
	enterCRN.send_keys(CRN)
	search(driver)
	return driver 
	
#click search button
def search(driver):
	searchButton = driver.find_element_by_name("search")
	searchButton.click()

#pulls data from page, returns space available in the class 
def pull(driver):
	data = BeautifulSoup(driver.page_source, "html.parser")
	for line in data.find_all(id = "courseResultsDiv"): 
		space = line.find_all(title = "View Course Detail")[2].find("em").get_text()
		space = int(space.strip())
		return space 

#################### End function definitions ####################

CRN = input("Enter CRN of class: ") #Obtain CRN from user
url = "https://registrar.ucdavis.edu/courses/search/index.cfm" #define URL to be class search website
driver = initialize(CRN, url)

time.sleep(5)

spacesAvailable = pull(driver)

if spacesAvailable != 0:
	print "There is space available in this class"
else:
	print "There is no space available in this class"

driver.close() #close driver 


		
	