import urllib.request
import re

def getHtml(url):
    page = urllib.request.urlopen(url) 
    html = page.read() 
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'  
    imgre = re.compile(reg) 
    html = html.decode('utf-8') 
    imglist = re.findall(imgre,html)   
    x = 0

    for imgurl in imglist:
     urllib.request.urlretrieve(imgurl,r'C:\cxl\%s.jpg' % x)
     x += 1


html = getHtml("http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808")
print(getImg(html))







import requests
URLS=[]
url=''
response=requests.get(url)
html=response.text
line=html.split('\n')
for line in lines:
    if '<img' in line:
        split_=line.split('<img src=')
        for i in split_:
            if 'http'in i or 'https' in i
            url=i.split('"')[1]
            if 'jpg'in url:
                URLS.append(url)
for url in URLS:
    response= requests.get(url)
    content=response.content
    name=url.split('/')[-1]
    with open(name,'wb') as f:
        f.write(content)