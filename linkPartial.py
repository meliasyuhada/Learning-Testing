from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://thinkjubilee.com/")
# driver.find_element(By.LINK_TEXT, "Jubilee Enterprise Official Site").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Jubilee").click()
time.sleep(3)
