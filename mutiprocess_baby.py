import requests,time ,re
import multiprocessing as mp

def save_txt(names,year):
    print('staring file',time.time()-starts)
    with open(r'F:\c语言\python\babynames\yob%s.txt'%year,'w',encoding='utf-8') as f:
        for name in names:
                f.write(name+'\n')
        f.close()
        print('the %s babynames has done'%year)

def Get_html(year,reg,q):
            # reg = r'<td id="LC\d+" class=.*?>(.*?)\r</td>'
            # reg = re.compile(reg)
    #for year in range(1980,2014):
            start=time.time()
            print('html is working')
            html=requests.get('https://github.com/tspike/babynames/blob/master/data/yob%s.txt'%year )
            #html.encoding=html.apparent_encoding  检索浪费时间  先查找网站的编码格式
            html.encoding='utf-8'
            html=html.text
            print('html cost time is %s'%(time.time()-start))
            names = re.findall(reg, html)
            #save_txt(names=names,year=year)
            print(type(names),(time.time()-start))
            #return names
            q.put(names)

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
def main(year):
    # names=Get_html(year,reg)
    # save_txt(names,year)
    q=mp.Queue()
    p1=mp.Process(target=Get_html,args=(year,reg,q))
    names=q.get()
    p2=mp.Process(target=save_txt,args=(names,year))
    p1.start()
    p1.join()
    #p2.start()
    print('the totally time is :%s '%(time.time()-starts))

starts=time.time()
print('the work is staring')
reg = r'<td id="LC\d+" class=.*?>(.*?)\r</td>'
reg = re.compile(reg)


#for year in range(1980,2014):
main(1980)
