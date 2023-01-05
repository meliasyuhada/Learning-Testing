# belajar selenium, buka browser dan buka url browser
from selenium import webdriver
# pertama panggil selenium dan import webdriver
# jika selenium nya error coba install kembali selenium sesuai python yang kamu miliki.

# in a virtual environment or using Python 2 => pip install selenium
# for python 3 (could also be pip3.10 depending on your version) => pip3 install selenium
# if you get permissions error => sudo pip3 install selenium => pip install selenium --user
# if you don't have pip in your PATH environment variable => python -m pip install selenium
# for python 3 (could also be pip3.10 depending on your version) => python3 -m pip install selenium
# using py alias (Windows) => py -m pip install selenium
# for Anaconda => conda install -c conda-forge selenium
# for Jupyter Notebook => !pip install selenium

driver = webdriver.Chrome()
driver.get("http://project-ubah.open/")
driver.maximize_window()


# jalankannya dengan cara
# python rutin.py