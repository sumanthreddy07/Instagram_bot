from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as BS
import login
import time

username = ''           #enter username
password = ''           #enter password
driver = 0
def main():
    global driver
    print('running script...')
    driver = webdriver.Chrome( ) #insert location of .exe file
    log = login.Login(driver, username, password)
    log.signin()


if __name__ == '__main__':
    main()