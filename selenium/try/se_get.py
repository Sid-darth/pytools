from re import search
from selenium import webdriver
from icecream import ic

chrome_driver_path = "C:\dev_tools\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

url = 'https://www.amazon.com/Metroid-Dread-Nintendo-Switch/dp/B097B1149G/ref=sr_1_2?crid=EJDQI713IFUI&keywords=nintendo+switch+metroid+dread&qid=1637567884&sprefix=nintendo+switch+metroi%2Caps%2C219&sr=8-2'

driver.get(url)

price = driver.find_element_by_id('priceblock_ourprice')
ic(price.text)

name_search = driver.find_element_by_name('field-keywords')
ic(name_search.get_attribute('value'))

# class_search = driver.find_element_by_class_name('nav-logo-base nav-sprite')
# ic(class_search)

# find attribute within another attribute
delivery_details = driver.find_element_by_css_selector(".a-spacing-base a")
ic(delivery_details.text)

# use xpath
img_link = driver.find_element_by_xpath('//*[@id="landingImage"]')
ic(img_link.get_attribute('src'))

driver.close()