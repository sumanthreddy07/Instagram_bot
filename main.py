from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as BS
import login
import time
import getpages
username = ''           #enter username
password = ''           #enter password
driver = 0
max_likes = 100         #increase later on
max_follows= 50         #increase later on
def main():
    global driver
    print('running script...')
    driver = webdriver.Chrome( ) #insert location of .exe file
    log = login.Login(driver, username, password)
    log.signin()
    driver.get('') #provide the link of the page whose followers are to be followed
    gp = getpages.Getpages(driver)
    refs = gp.get_followers()
    print(gp.get_num_flw())
    run_bot(refs,driver,gp)

def run_bot(refs, driver, gp):
    t =time.time()
    L = 0           #likes
    F = 0           #followers

    for r in refs:
        driver.get('https://www.instagram.com' + r)
        time.sleep(2)
        if gp.get_num_flw() < 3000:
            if gp.is_public():
                print("public account")
                print('current likes' + str(L))
                if L<max_likes:
                    gp.like_post()
                    L+=1
                    print('Post Liked')
                else:
                    time.sleep(3600) #waiting for an hr
            else:
                print('Account is private')
                print('current follows: '+str(F))
                if F< max_follows:
                    time.sleep(2)
                    gp.follow_page()
                    print('Page followed')
                    F+=1
                else:
                    time.sleep(3600) #sleep for an hr

if __name__ == '__main__':
    main()