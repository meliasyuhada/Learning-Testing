from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/alerts")
driver.find_element(By.ID, "promtButton").click()
time.sleep(4)

alert = Alert(driver)

alert.send_keys("Liana")
time.sleep(4)
alert.accept()
