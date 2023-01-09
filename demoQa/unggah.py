from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
driver.find_element(By.ID, "photo").send_keys("C:\python_selenium\Learning-Testing\demoQa\ped.png")