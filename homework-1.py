#homework_1
#抓取网页
import urllib.request
response=urllib.request.urlopen('http://www.17k.com/chapter/2933095/36699279.html')
print(response.read().decode('utf8'))
print(response.status)


#homework_2
import http.cookiejar,urllib.request
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; ServiceUI 13.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
}
daili=({'http':'http://127.0.0.1:5555'},{'http':'http://175.181.40.199:44308'})
for proxy_handler in daili:
    try:
        opener = urllib.request.build_opener(proxy_handler)
        reponse = opener.open('http://www.taobao.com',timeout=1)
        print(reponse.read())
        if response.status==200:
            print('成功')
        else:
            print('错误')
    except:
        print('代理失效')