from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.tokopedia.com/")
driver.get_screenshot_as_file("tokped.png")
driver.save_screenshot("ped.png")