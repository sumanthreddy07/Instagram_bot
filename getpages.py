from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as BS
import login
import time

class Getpages:
    def __init__(self,driver):
        self.driver = driver
        self.driver.get(' ') #enter page link
        self.hrefs= []

    def get_num_flw(self):
        time.sleep(1)
        flw = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '//*[@id="react-root"]/section/main')))
        sflw= BS(flw.get_attribute('innerHTML'), 'html.parser')
        followers = sflw.findAll('span', {'class':'g47SY'})
        f = followers[0].getText().replace(',', '')

        if 'k' in f:
            f= float(f[:-1]) *10**3
            return f
        elif 'm' in f:
            f= float(f[:-1]) * 10**6
            return f
        else:
            return float(f)
    def get_followers(self):
        time.sleep(2)
        flw_btn = WebDriverWait(self.driver ,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '//*[@id="react-root"]/section/main/div/ul/li[2]/a/span')))
        flw_btn.click()
        time.sleep(15)
        self.popup = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]')))

        for h in range(11):
            time.sleep(1)
            print('scrolling...')
            print('arguments[0].scrollTop = arguments[0].scrollHeight/{}'.format(str(11-h)))
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight/{}'.format(str(11-h)),self.popup)
            if h == 5:
                 break

        for _ in range(15):
            time.sleep(2)
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight',self.popup)
    
        self.popup = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]')))
        b_popup= BS(self.popup.get_attribute('innerHTML'), 'html.parser')
        for p in b_popup.findAll('li', {'class': 'wo9IH'}):
            try:
                hlink= p.findAll('a')[0]['href']
                if 'div' in hlink:
                    return self.hrefs
                else:
                    self.hrefs.append(hlink)
            except:
                pass
        return self.hrefs

    def is_public(self):
        try:
            astate=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'rkEop')))
            if astate.text == 'This Account is Private':
                return False
            else:
                return True
        except:
            return True

    def like_post(self):
        post= self.driver.find_element_by_css_selector('#react-root > section > main > div > div._2z6nI > article > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(1) > a')
        html= post.get_attribute('innerHTML')
        h= BS(html, 'html.parser')
        href= h.a['href']
        self.driver.get('https://www.instagram.com' + href)
        like_btn= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > div.ltEKP > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n')))
        like_btn.click()

    def follow_page(self):
        follow = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > header > section > div.Y2E37 > div > span > span.vBF20._1OSdk > button')))
        f_text = follow.text
        if f_text.lower() == 'follow' or f_text.lower() == 'follow back':
            follow.click()
        elif f_text == 'already following':
            print('already following')
        time.sleep(1)