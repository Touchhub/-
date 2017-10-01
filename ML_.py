import requests
from bs4 import BeautifulSoup
def GETHTML(html):
    try:
        html=requests.get(html)
        html.raise_for_status()
        html.encoding=html.apparent_encoding
        return html.text
    except:
        return ' '
def PRINT(ilt,html):
    soup=BeautifulSoup(html,'html.parser')
    strong=soup.find_all('strong')
    title = soup.find_all(class_="title")
    for list1,list2 in zip(strong,title):
        ilt.append([list1.string.strip(),list2.string.strip()])
    print (len(ilt))
    return ilt
def printGoodlirt(ilt):
    tplt="{:4}\t{:8}\t{:16}"
    print(tplt.format('序号','价格','商品名称'))
    count=0
    for g in ilt :
        count=count+1
        theend=('{:4}\t{:8}\t{:16}'.format(count,g[0],g[1]))
        #print(theend)
def main():
    inforlist=[]
    html='http://uland.taobao.com/sem/tbsearch?keyword='+'书包'
    txt=GETHTML(html=html)
    PRINT(inforlist,txt)
    printGoodlirt(inforlist)
    import pandas as pd
    table=pd.Series([inforlist[0],inforlist[1]])
    table.to_excel('taobao1.xlsx')
main()
