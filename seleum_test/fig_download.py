from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import  BeautifulSoup

import time, os,requests,re
start=time.time()
links=[]
names=[]
url='http://lol.qq.com/web201310/'
with open('F:\c语言\python\champions\champion.txt','r',encoding='utf-8') as f:
    for line in f.readlines():
        line=line.split('\t')
        links.append(url+line[0])
        names.append(line[1][:-1])
#print(links)
champions_url=[]
reg=re.compile('small')
for link,name in zip(links,names):
    starts_2=time.time()
    os.makedirs(r'F:\c语言\python\英雄联盟\%s'%name)
    print(link,names[0])
    driver = webdriver.PhantomJS()
    driver.get(link)
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 700)")
    try:
        element=WebDriverWait(driver,20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"#skinBG > li > img")))
    finally:
        lis=BeautifulSoup(driver.page_source,'html.parser').find('ul',attrs={'id':'skinNAV'})
        print(lis)
        driver.close()
        for li in lis :
            print(li.img['alt'],'-----')
            src=re.sub(reg,'big',li.img['src'])
            print(src)
            img_data=requests.get(src).content
            with open(r'F:\c语言\python\英雄联盟\%s\%s.jpg'%(name,li.img['alt']),'wb') as f:
                f.write(img_data)
                f.close()
        print('%s has download,the next is downing'%name)
print(time.time()-start)

