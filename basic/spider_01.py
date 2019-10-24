import requests

# 接收响应
response = requests.get("https://www.baidu.com/")
# print(response.encoding)  # ISO-8859-1
response.encoding = 'utf-8'  # 更改代码
# print(response.text)

# 将解析出来的数据保存下来
# open(param1, param2)可以打开一个文件或者创建一个文件
# param1: 路径
# param2: 写入模式(先判断文件是否存在，不存在则创建)
f = open("/Users/lewy/WorkSets/pythonSet/DebutSpider/data/baidu", 'w')
f.write(response.text)
f.close()
