import requests
from bs4 import BeautifulSoup

q = input("请输入您要搜索的单词：")
url = 'https://cn.bing.com/dict/search?q=' + q

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
response = requests.get(url, headers = headers)

# 设置编码
response.encoding = response.raise_for_status()

html = response.text
soup = BeautifulSoup(html, 'html.parser')
span = soup.select('span.def span')
print(span[0].text)