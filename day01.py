#homework1
from urllib.request import urlopen
html = urlopen(
    "https://www.taobao.com/"
).read().decode('utf-8')
print(html)



#homework2
import urllib.request
import urllib.parse
import requests
data=urllib.parse.urlencode({'wd':'淘宝'})
print(data)
url='http://www.baidu.com/s?'+data
response=urllib.request.urlopen(url)
HTML=response.read().decode('utf8')
print(HTML)