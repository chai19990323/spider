#homework1
from bs4 import BeautifulSoup
import requests
urls = ['https://www.yrw.com/products/list-direct-all-performance-1-createTimeDesc-{}.html'.format(str(i)) for i in range(1,11)]
def get_titles(urls,data = None):
web_data = requests.get(urls)
soup = BeautifulSoup(web_data.text, 'lxml')
    titles = soup.select(' h3 > a > em > strong')
for title in titles:
        data = {
            'title': title.get_text()
         }
        print(data)

for titles in urls:
    get_titles(titles)




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
