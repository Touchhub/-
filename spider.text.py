#re  84s
import requests ,re,time
def Get_html(url):
    try:
        html=requests.get(url)
        html.encoding=html.apparent_encoding
        if html.status_code==200:
            return html.text
    except Exception:
        print('timeout')
def parser_sourse(html):
    print('parser is working')
    #print(html)
    #price,title,shopname,paynum
    reg='<div class="info".*?<strong>.*?(\d+).*?title="(.*?)">.*?class="shopNick">(.*?)<.*?"payNum">(.*?)</span>'
    reg=re.compile(reg,re.S)
    try:
        lists=re.findall(reg,html)
        for list in lists:
            yield {
                'price':list[0],
                'title':list[1],
                'shopname':list[2],
                'paynum':list[3]
            }
    except:
        print('none')

    #for list in lists:
    #         print(list,'none')
    # except:
    #     print('nonework')
def main():
    goods='电脑'
    url='http://uland.taobao.com/sem/tbsearch?keyword=%s'%goods
    start=time.time()
    html=Get_html(url)
    count=1
    for list in parser_sourse(html):
        print(list)
        count+=1
    print('number=%s'%count,'time=%s'%(time.time()-start))
main()
