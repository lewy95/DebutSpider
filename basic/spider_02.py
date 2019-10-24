url = 'http://quotes.toscrape.com/'

import requests
from bs4 import BeautifulSoup

response = requests.get(url)
# 用于解析 参数一：待解析的数据  参数二：解析器（html.parser是py自带的，工作用常用lxml）
soup = BeautifulSoup(response.text, 'html.parser')
# 找到这个页面中所有的<span>标签
span = soup.select("span.text")
# select 查询出来的数据是列表类型[sp1,sp2,sp3,....]
# print(span)

# 保存数据
f = open("/Users/lewy/WorkSets/pythonSet/DebutSpider/data/quotes", 'w')
# 遍历输出
for i in span:
    f.write(i.text + '\n')

f.close()


