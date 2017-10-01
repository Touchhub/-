import requests,re,time

headers={
'Referer':'http://lol.qq.com/web201310/info-heros.shtml?ADTAG=lolweb.v2',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}
def get_html(url):
    html=requests.get(url,headers=headers)
    code=(html.status_code)
    print(code)
    if code==200:
        html.encoding=html.apparent_encoding
        return html.text
    print('获取失败')



def parser_sourse(list,html):
    rex=r'keys":{(.*?)}'
    rex=re.compile(rex)
    result=re.findall(rex,html)
    results=','.join(result)
    reg = re.compile(r'"(.*?)"')
    results=re.findall(reg,results)
    for result in results:
        list.append(result)



def GET_image(champions):
    i=0
    for champion in champions:
        try:
            url='http://ossweb-img.qq.com/images/lol/web201310/skin/big%s000.jpg'%champions[i]
            image_data=requests.get(url).content
            with open(r'F:\c语言\python\英雄联盟\%s.jpg'%champions[i+1],'wb') as f:
                f.write(image_data)
            i+=2
        except Exception:
            print('i>138')
            break

def main():
    print('The work starts:')
    start=time.time()
    champions=[]
    url='http://lol.qq.com/biz/hero/champion.js'
    html=get_html(url)
    parser_sourse(champions,html)
    print(champions)
    #GET_image(champions)
    print('The work has done,the total time is %s'%(time.time()-start))

main()
