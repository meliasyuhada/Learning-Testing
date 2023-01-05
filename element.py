from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://thinkjubilee.com/")
driver.maximize_window()
# ada berbagai macam cara untuk memanggil element yang ada di website, 
# baik dengan memenggil id, css, type dll.
# driver.find_element(By.ID, "woocommerce-product-search-field-0").send_keys("python")
# driver.find_element(By.CSS_SELECTOR)
# driver.find_element(By.PARTIAL_LINK_TEXT)
# driver.find_element(By.XPATH)
driver.find_element(By.NAME, "s").send_keys("python")
driver.find_element(By.CLASS_NAME, "wp-element-button").click()