"""
1.准备url
2.发送请求
3.获取数据
4.str -》 html的element对象
5.提取数据
6.入库
"""

import requests
from lxml import html
import os

thing = "python"
url = "http://search.dangdang.com/?key={}&act=input".format(thing)

while True:
    response = requests.get(url=url)
    element = html.fromstring(response.text)
    element_ul_list = element.xpath('//*[@id="search_nature_rg"]/ul')
    element_li_list = element_ul_list[0].xpath("./li")
    for li in element_li_list:
        book_name = li.xpath("./a/@title")[0].strip()
        href = li.xpath("./a/@href")[0]
        price_list = li.xpath('./p[@class="price"]/span[@class="search_now_price"]/text()')
        if price_list:
            price = price_list[0]
        else:
            price = li.xpath('./div/p/span/text()')[0]

        file = "dangdnag.txt"
        mode = "a" if os.path.getsize(file) > 0 else "w"
        with open(file, mode, encoding="utf8") as f:
            f.write("书名：" + book_name + "\n价格：" + price + "\n链接：" + href + "\n\n")
    url = "http://search.dangdang.com" + element.xpath('//*[@id="12810"]/div[5]/div[2]/div/ul/li[10]/a/@href')[0]
    print(url)
    if not url:
        break

