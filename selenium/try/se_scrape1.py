from re import search
from selenium import webdriver
from icecream import ic
from selenium.webdriver.common.by import By

# start driver
chrome_driver_path = "C:\dev_tools\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# scrape event data from python.org site
url = "https://www.python.org"

# drive into url
driver.get(url)

# events -> in .medium-widget.event-widget.last-- ul "
event_container = driver.find_element(By.CSS_SELECTOR,".medium-widget.event-widget.last ul")

# finding list elements
event_list = event_container.find_elements(By.TAG_NAME,'li')
event_dict = {}
# create dictionary
for idx, event in enumerate(event_list):
    time_ = event.find_element(By.CSS_SELECTOR,'li>time').get_attribute('datetime')
    venue = event.find_element(By.TAG_NAME,'a')
    event_dict[idx] = {'time' : time_, 'name': venue.text}


#### alternate ####
event_times = driver.find_elements(By.CSS_SELECTOR,".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR,".event-widget li a")


driver.close()