"""
https://www.biqulou.net/439/439271/2284951.html
https://www.biqulou.net/439/439271/2436753.html
https://www.biqulou.net/439/439271/2436754.html
https://www.biqulou.net/439/439271/2436755.html
https://www.biqulou.net/439/439271/2436756.html
...
https://www.biqulou.net/439/439271/2441646.html         152
https://www.biqulou.net/439/439271/2441647.html         153

"""

import requests
import re


class Spider:
    def __init__(self):
        self.urls_list = []

    def make_urls(self):
        # 生成url列表
        self.urls_list.append("https://www.biqulou.net/439/439271/2284951.html")
        base_url = "https://www.biqulou.net/439/439271/{}.html"
        for i in range(2436753, 2441647):
            self.urls_list.append(base_url.format(i))

    def spider(self):
        """爬取数据，并对每一次的结果进行提取内容、保存"""
        for url in self.urls_list:
            response = requests.get(url)
            html_str = response.content.decode("utf-8")
            # 提取内容
            data = self.handel_data(html_str)
            # 保存到文件中
            self.save_file(data)

    def handel_data(self, html_str):
        """处理html，提取所需的内容"""
        title = re.search('<div class="bookname"><h1>(.*)</h1>', html_str)
        print(title)

    def save_file(self, data):
        """保存文件"""
        with open("text.txt", "a") as f:
            f.write(data)

    def go(self):
        self.make_urls()
        html = self.spider()
        self.handel_data(html)


if __name__ == "__main__":
    s = Spider()
    s.go()