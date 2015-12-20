import requests
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time 
from twilio.rest import TwilioRestClient

ACCOUNT_SID = "AC260cd4e8e27fad2fe13461826e9e5256" 
AUTH_TOKEN = "8bc1c3a48457cdc2ccaf277428023ab7" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

#################### Start function definitions ####################

#Opens driver, enters in CRN, and searches 
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
	for line in data.find_all(id = "courseResultsDiv"): #Navigate to correct location 
		space = line.find_all(title = "View Course Detail")[2].find("em").get_text()
		space = int(space.strip())	#Strip whitespace and convert to integer 
		return space 

#notify user about space availability 
def notify():
	client.messages.create(
    to="+14087817153", 
    from_="+16503833845", 
    body="There is space available!", 
	)
	#print "notify"

#################### End function definitions ####################

url = "https://registrar.ucdavis.edu/courses/search/index.cfm" #define URL to be class search website
CRN = input("Enter CRN of class: ") #Obtain CRN from user
interval = input("How often do you want to check in seconds? ")

driver = initialize(CRN, url)

time.sleep(5) #Allow adequate time for javascript to execute and generate desired html

spacesAvailable = pull(driver) #Returns spaces available for the class

while True:						#loop until break 
	if spacesAvailable != 0:
		print "There is space available in this class"
		notify()
		break 
	else:
		time.sleep(interval-5)	#wait given amount of time
		search(driver)			#click search button again
		time.sleep(5)
		spacesAvailable = pull(driver) 	#check updated space availability 

driver.close() #close driver 


		
	