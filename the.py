#BeautifulSoup  5秒
import requests ,time
from bs4 import BeautifulSoup
def Get_html(url):
    try:
        html=requests.get(url)
        html.encoding=html.apparent_encoding
        if html.status_code==200:
            return html.text
    except Exception:
        print('timeout')
def parser_sourse(lists,html):
    print('parser is working')
    soup=BeautifulSoup(html,'html.parser')
    #print(soup)
    items= soup.find_all(class_="item")
    titles=soup.find_all(class_="title")
    shopnicks=soup.find_all(class_="shopNick")
    paynums=soup.find_all(class_="payNum")
    pricedetails=soup.find_all('strong')
    count=1
    for pricedetail,title,shopnick,paynum in zip(pricedetails,titles,shopnicks,paynums):
        lists.append([pricedetail.next.strip(),title.string,shopnick.next,paynum.next])
        count+=1
    print(count)
def EXCEL(list,goods):
    import pandas as pd
    table=pd.DataFrame(list)
    table.columns=['price','title','shopname','paynum']
    table.to_excel(r'C:\Users\Shinelon\Desktop\%s.xlsx'%goods)
def main():
    inforlist=[]
    goods=input('please input your search:' )
    url='http://uland.taobao.com/sem/tbsearch?keyword=%s'%goods
    start=time.time()
    html=Get_html(url)
    parser_sourse(inforlist,html)
    EXCEL(inforlist,goods)
    print('time=%s'%(time.time()-start))
main()
