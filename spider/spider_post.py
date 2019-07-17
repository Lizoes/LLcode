import requests

url = "http://httpbin.org/post"
url = "https://www.baidu.com"
h = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
# 准备代理，类型为键，url:port为值
# proxies = {"http": "http://218.60.8.99:3129"}
proxies = {"https": "https://39.137.69.10:8080"}

para = {"aa": "AA"}
# 代理
response = requests.post(url, headers=h, data=para, proxies=proxies)


print(response.content.decode())
"""
"origin": "222.200.111.238, 222.200.111.238", 
"""