from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/alerts")
driver.find_element(By.ID, "confirmButton").click()
time.sleep(2)

alert = Alert(driver)
alert.dismiss()
