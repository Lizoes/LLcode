import requests

url = "http://httpbin.org/post"
h = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

# 准备代理，类型为键，url:port为值
# proxies = {"http": "http://218.60.8.99:3129"}
proxies = {"https": "https://39.137.69.10:8080"}
# post参数
para = {"aa": "AA"}
# cookie,或者放到header也可以
cookie = {"Cookie": "JSESSIONID=39ABA5DBDF63C51CC72F918DA7473AD2; UM_distinctid=16bf889697b25b-04d8ff4bf11cc-3f385804-15f900-16bf889697ca1f; CNZZDATA1253707717=369178737-1563242173-null%7C1563242173"}
response = requests.post(url, headers=h, data=para, proxies=proxies, cookie=cookie)


print(response.content.decode())
"""
"origin": "222.200.111.238, 222.200.111.238", 
"""