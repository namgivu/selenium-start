from selenium           import webdriver
from selenium.webdriver import DesiredCapabilities

driver = webdriver.Remote(
  command_executor='http://localhost:4444/wd/hub',
  desired_capabilities=DesiredCapabilities.CHROME
)

#this is working
driver.get('https://www.google.com.vn/search?q=abb')
print(driver.title)

#TODO this not working, why?
driver.get('https://www.tiki.vn/dien-gia-dung/c1882?src=mega-menu')
print(driver.title)
