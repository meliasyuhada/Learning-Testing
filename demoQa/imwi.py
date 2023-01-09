from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.instagram.com/")
driver.implicitly_wait(20)
driver.find_element(By.NAME, "username").send_keys("username")
driver.implicitly_wait(20)
driver.find_element(By.NAME, "password").send_keys("******")
driver.implicitly_wait(20)
driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > section:nth-child(1) > main:nth-child(2) > article:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(1) > div:nth-child(3)").click()
driver.implicitly_wait(20)