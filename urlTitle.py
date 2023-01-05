from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://thinkjubilee.com/")

alamat = driver.current_url
judul = driver.title
panjangjudul = len(judul)

print("Alamat situs: {}, Judul situs: {}, panjang judulnya: {}".format(alamat, judul, panjangjudul))

# Output :
# Alamat situs: https://thinkjubilee.com/, Judul situs: Welcome - Jubilee Enterprise, panjang judulnya: 28