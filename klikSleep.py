from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://www.kompas.com/")
driver.find_element(By.NAME, "q").send_keys("jadwal timnas")
time.sleep(2)
search = driver.find_element(By.NAME, "submit")
search.click()
time.sleep(2)