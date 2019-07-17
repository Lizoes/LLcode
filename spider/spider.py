"""
聚焦爬虫：

url列表
遍历列表
提取data -> 保存到数据库（入库）

robots协议

投毒：状态码200但是访问错了
"""
import requests

h = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}

url = "https://www.baidu.com"
response = requests.get(url)
# 获取的html
# print(response.text)  # ISO-8859-1编码方式
# print(response.content, type(response.content))  # 获取的是二进制数据
# response.content.decode("utf8")  #

# 状态码、编码方式、url
# print(response.status_code)
# print(response.url)
# print(response.encoding)
print(response.headers)

# 修改编码方式
# response.encoding = "utf8"
# print(response.text)
