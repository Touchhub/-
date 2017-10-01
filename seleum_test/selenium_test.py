from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import  BeautifulSoup
import time
start=time.time()
url='http://lol.qq.com/web201310/info-defail.shtml?id=Ahri'
driver=webdriver.Chrome()
driver.get(url)
try:
    element=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#skinBG > li > img")))
finally:
    #selector=driver.find_element_by_css_selector('#skinBG > li > img')
    html=BeautifulSoup(driver.page_source,'html.parser')
    #print(html)
    lis=(html.find('ul',attrs={'id':'skinNAV'}).find_all('li'))
    driver.close()
for li in lis:
    print(li.img['alt'],'-----',li.img['src'])
