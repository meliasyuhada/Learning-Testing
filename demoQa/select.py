from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
# driver.find_element(By.ID, "sex-0").click()
# # driver.find_element(By.ID, "sex-1").click()

menu = driver.find_element(By.ID, "continents")
drop=Select(menu)
# menu = Select(driver.find_element_by_id("continents"))
# time.sleep(3)