import requests
from bs4 import BeautifulSoup
import re
import base64
import urllib.parse

class Crawler():
     def __init__(self, name):
          self.name = name
class Pcstore(Crawler):
    def __init__(self, name):
        super().__init__(name)
    def showTitle(self):
        word_encode = urllib.parse.quote(self.name).encode('ascii')
        word_base64 = base64.b64encode(word_encode).decode()
        url = 'https://www.pcstore.com.tw/adm/psearch.htm?store_k_word='+ word_base64 + '&slt_k_option=1'
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
        res = requests.get(url, headers=headers)
        res.encoding = 'Big5'
        soup = BeautifulSoup(res.text, 'html.parser')
        dcard_title = soup.find_all('div', re.compile('pic2t'))
        print('標題：')
        for index, item in enumerate(dcard_title):
            print("{0:2d}. {1}".format(index + 1, item.text.strip()))
        return dcard_title

if __name__ == '__main__':
    p = Pcstore('球')
    p.showTitle()