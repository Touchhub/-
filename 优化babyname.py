import requests,time ,re
from  bs4 import  BeautifulSoup

def save_txt(names,year):
    print('staring file')
    with open(r'F:\c语言\python\babynames\yob%s.txt'%year,'w',encoding='utf-8') as f:
        for name in names:
                f.write(name+'\n')
        f.close()
        print('the %s babynames has done'%year)

def Get_html():
    reg = r'<td id="LC\d+" class=.*?>(.*?)\r</td>'
    reg = re.compile(reg)
    for year in range(1980,2014):
            start=time.time()
            print('html is working')
            html=requests.get('https://github.com/tspike/babynames/blob/master/data/yob%s.txt'%year)
            html.encoding='utf-8'
            html=html.text
            names = re.findall(reg, html)
            save_txt(names=names,year=year)
            print(type(names),(time.time()-start))

# def Get_html():
#     for year in range(1980,2014):
#             print('html is working')
#             html=requests.get('https://github.com/tspike/babynames/blob/master/data/yob%s.txt'%year)
#             html.encoding=html.apparent_encoding
#             html=html.text
#             soup=BeautifulSoup(html,'html.parser')
#             names=soup.find_all(class_="blob-code blob-code-inner js-file-line")
#             #save_txt(names=names,year=year)
#             print(names)
#             break
def main():
    Get_html()
    print('the totally time is :%s '%(time.time()-starts))

starts=time.time()
print('the work is staring')
main()
