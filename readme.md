Hal-hal yang harus dilakukan dan yang dimiliki untuk melakukan pengujian otomatis menggunakan
Selenium Webdriver.

1. Install Python => python.org
2. Install Webdriver
        Chrome:	https://chromedriver.chromium.org/downloads
        Edge:	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
        Firefox:	https://github.com/mozilla/geckodriver/releases
        Safari:	https://webkit.org/blog/6900/webdriver-support-in-safari-10/
3. Install Selenium
        => pip install Selenium
        => pip list
3. Install VSCode / PyCharm


menulis script python nya
- bisa langsung menggunakan python
    => dengan cara masuk ke folder yang akan dibuat
    => misalkan cd C://selenium-python
    => kemudian masukkan tulisan python
    => kemudian kita akan masuk ke terminal python dan kita bisa tuliskan scriptnya disana
    => misalkan 
    => from selenium import Webdriver
        driver = webdriver.Chrome()
    => maka otomatis akan terbuka jendela browser Chrome.

- bisa juga dengan menggunakan file seperti rutin.py
- atau bisa juga dengan menggunakan google colab (https://colab.research.google.com/), 
  jika kalian lagi tidak membawa leptop atau pun lagi berada diluar
    => hal yang harus dilakukan untuk menggunakan selenium di google colab yaitu :
        1. install selenium dengan cara
            => !pip install selenium
        2. install webdriver
            => !apt-get update
            => !apt install chromium-chromedriver
        3. menggunakan headles (pilihan, ketika tidak akan menjalankan jendela browser.)
            