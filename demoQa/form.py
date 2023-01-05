from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/text-box")
driver.find_element(By.ID, "userName").send_keys("liana")
time.sleep(3)
driver.find_element(By.ID, "userEmail").send_keys("liana@gmail.com")
time.sleep(3)
driver.find_element(By.ID, "currentAddress").send_keys("Riau")
time.sleep(3)
driver.find_element(By.ID, "permanentAddress").send_keys("Ending")
time.sleep(3)
driver.find_element(By.ID, "submit").click()