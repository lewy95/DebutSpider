"""
爬取拉勾网数据分析岗位数据
爬虫协议：robots.txt，只是个君子协议，声明哪些地方不希望被爬虫使用，但是不能禁止你怎么做
"""

import csv
import json
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    "Connection": "keep-alive",
    "Host": "www.lagou.com", #  注意：这样是不行的https://www.lagou.com，不要带上https，https是一个私密协议
    # Refer表示请求是从哪里发送过来的，有的网站禁止外部请求爬取数据，这时需要一个内部的地址来糊弄过关
    "Referer": "https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=sug&fromSearch=true&suginput=%E6%95%B0%E6%8D%AE"
}

#  start_url的作用是，首先登陆到拉钩网，获取一个cookie，从取获取登陆信息
#  因为有的网站的数据是需要登陆后才可以查看的，这样是爬不下来的，会报403，必须要登陆信息才可以
#  我们可以从浏览器的header中查看cookie信息，并将它添加到这里请求的header中
start_url = 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/p-city_0?&cl=false&fromSearch=true&labelWords=&suginput='
url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

prompt = input('请您输入想要爬取的岗位信息')
for i in range(1, 31):
    print(f'正在爬取第{i}页')
    data = {
        'first': 'false',
        'pn': str(i),
        'kd': prompt
    }
    # response = requests.post(url,headers=headers,data=data)
    # 创建一个session对象
    session = requests.session()
    # 用session对象先发送一次请求 获得cookies保持
    session.get(start_url, headers=headers)
    # 再 用一个带着cookies 的session发送一个post请求 这次是真正的数据链接
    response = session.post(url, headers=headers, data=data, cookies=session.cookies)
    # print(response.status_code)
    # print(response.text)
    # print(type(response.text))
    text = json.loads(response.text)
    info = text.get('content').get('positionResult').get('result')
    f = open('/Users/lewy/WorkSets/pythonSet/DebutSpider/data/lagou', 'a', encoding='utf-8', newline='')
    for i in info:
        data = []
        data.append(i.get('positionName'))  # 岗位名称
        data.append(i.get('companyFullName'))  # 公司名称
        data.append(i.get('financeStage'))  # 是否融资
        print(data)
        ow = csv.writer(f)
        ow.writerow(data)
    f.close()

# print(text)
# print(type(text))
# srt1 = '{"岗位信息":"数据分析","薪资":"20K","地点":"北京"}'# 正则表达式
# s = json.loads(srt1)# 可以把一个json字符串  转化成一个字典
# print(s)
# print(type(s))# dict