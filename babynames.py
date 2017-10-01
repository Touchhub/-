def Get_babyname_soup(html):
    from bs4 import BeautifulSoup
    soup=BeautifulSoup(html,'html.parser')
    names=soup.find_all(class_='blob-code blob-code-inner js-file-line')
    for name in names:
        print((name.text))
        break

import requests,time
def Get_html(url,year):
    try:
        html=requests.get(url=url)
        html.encoding='utf-8'
        html=html.text
        return html
    except Exception as e:
        main(year+1)

def Get_babynames(html,year):
    try:
        names=re.findall(reg,html)
        return names
    except:
        main(year+1)

def save_txt(names,year):
    with open(r'F:\c语言\python\babynames\yob%s.txt'%year,'w',encoding='utf-8') as f:
        for name in names:
                f.write(name+'\n')
        print('the %s babynames has done'%year)

def main(year):
    url='https://github.com/tspike/babynames/blob/master/data/yob%s.txt'%year
    html=Get_html(url,year)
    names=Get_babyname_soup(html=html)
    names=re.findall(reg,html)
    save_txt(names=names,year=year)
    Get_babyname_soup(html)
    print('the totally time is :%s '%(time.time()-starts))
import re
reg=r'<td id="LC\d+" class=.*?>(.*?)\r</td>'
reg=re.compile(reg)
starts=time.time()
years=range(1980,2014)
for year in years:
    main(year)
