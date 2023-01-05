from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
# driver.maximize_window()
driver.get("https://thinkjubilee.com/")
time.sleep(3)
# driver.execute_script("alert('Hallo Dunia!!')")
driver.execute_script("window.open('http://project-ubah.open/')")
time.sleep(3)