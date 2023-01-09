from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.instagram.com/")

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.ID, "userEmail"))

        # tunggu 10 detik atau menunggu setelah userEmail ditemukan.
    )
except TimeoutException:
    print("Element tidak ditemukan")
    driver.quit()
    # namun jika sudah 10 detik dan tidak menemukan userEmail, maka akan dialihkan 
    # ke pilihan timeoutexception yaitu tampilkan element tidak ditemukan dan keluar.

# finally:
#     driver.quit()

# except TimeOutException:
#     print("Element tidak ditemukan")
#     driver.quit()

driver.find_element(By.NAME, "username").send_keys("username")
driver.implicitly_wait(20)
driver.find_element(By.NAME, "password").send_keys("******")
driver.implicitly_wait(20)
driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > section:nth-child(1) > main:nth-child(2) > article:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(1) > div:nth-child(3)").click()
driver.implicitly_wait(20)