from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://thinkjubilee.com/")
driver.refresh()
time.sleep(3)
driver.get("http://project-ubah.open/")
time.sleep(3)
driver.quit()