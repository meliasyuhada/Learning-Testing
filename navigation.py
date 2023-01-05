from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://thinkjubilee.com/")

alamat = driver.current_url
judul = driver.title
panjangjudul = len(judul)

print("Alamat situs: {}, Judul situs: {}, panjang judulnya: {}".format(alamat, judul, panjangjudul))

time.sleep(5)

driver.forward()
driver.back()

time.sleep(10)
driver.close()

# Output :
# Alamat situs: https://thinkjubilee.com/, Judul situs: Welcome - Jubilee Enterprise, panjang judulnya: 28