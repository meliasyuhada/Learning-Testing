from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://thinkjubilee.com/cara-memperbaiki-cahaya-foto-digital-dengan-mudah/")
print(driver.page_source)
# digunakan untuk mengambil source pada halaman link yang dipanggil