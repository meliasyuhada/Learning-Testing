from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/text-box")
driver.find_element(By.XPATH, "//input[@id='userName']").send_keys("liana")
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys("liana@gmail.com")
time.sleep(3)
driver.find_element(By.XPATH, "//textarea[@id='currentAddress']").send_keys("Riau")
time.sleep(3)
driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']").send_keys("Ending")
time.sleep(3)
driver.find_element(By.XPATH, "//button[@id='submit']").click()
time.sleep(3)