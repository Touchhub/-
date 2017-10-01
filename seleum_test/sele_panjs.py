from  selenium import webdriver
import time,re,json
from bs4 import BeautifulSoup
start=time.time()
driver=webdriver.PhantomJS()
url='http://lol.qq.com/web201310/info-heros.shtml?ADTAG=lolweb.v2'
def driver_web(url):
    driver.get(url)
    time.sleep(1.5)
    soup=BeautifulSoup(driver.page_source,'html.parser')
    html=soup.find(id='jSearchHeroDiv')
    print(html)
    return  html
def parser(reg,html,champions):

        champions=re.findall(reg,str(html))
        with open(r'F:\c语言\python\champions\champion.txt','w',encoding='utf-8') as f:
            for i in range(len(champions)):
                f.write(champions[i][0]+'\t'+champions[i][1]+'\n')
        f.close()
        print('txt has done')

def regex(reg):
    reg=re.compile(reg)
    return reg



champions=[]
def main():
    html=driver_web(url)
    parser(regex(r'<a href="(.*?)".*?title="(.*?)">'),html,champions)
    print(time.time()-start)

main()
