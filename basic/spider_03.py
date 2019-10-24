"""
爬取猫眼电影榜单top100的电影名称、主演、上映时间
"""

import requests
from bs4 import BeautifulSoup

# 100部电影，但是猫眼上一页只展示10部，要查10页

for i in range(10):
    offset = i * 10
    print('开始爬取第' + str(i + 1) + "页")
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    response = requests.get(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"})

    soup = BeautifulSoup(response.text, "html.parser")

    rank = soup.select("i.board-index")  # 排名
    name = soup.select("p.name a")  # 电影名
    star = soup.select("p.star")  # 主演
    releaseTime = soup.select("p.releasetime")  # 上映时间

    f = open('/Users/lewy/WorkSets/pythonSet/DebutSpider/data/maoyan', 'a')
    for j in range(len(rank)):
        f.write('排名' + rank[j].text + '：' +
                name[j].text + ' ' +
                star[j].text.strip() + ' ' +
                releaseTime[j].text + '\n'
                )
    f.close()

#   for i in range(len(rank)):
#      print("排名" + rank[i].text + "：" + name[i].text + " " + star[i].text.strip() + " " + releaseTime[i].text)
