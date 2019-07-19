"""
https://www.biqulou.net/439/439271/2284951.html
https://www.biqulou.net/439/439271/2436753.html
https://www.biqulou.net/439/439271/2436754.html
https://www.biqulou.net/439/439271/2436755.html
https://www.biqulou.net/439/439271/2436756.html

https://www.biqulou.net/439/439271/2436804.html
https://www.biqulou.net/439/439271/2436833.html
...
https://www.biqulou.net/439/439271/2441646.html         152
https://www.biqulou.net/439/439271/2441647.html         153

"""

import requests
import re
from lxml import html
import jieba



class Spider:
    def __init__(self):
        self.urls_list = []
        self.base_url = ""

    # def make_urls(self):
    #     # 生成url列表
    #     self.urls_list.append("https://www.biqulou.net/439/439271/2284951.html")
    #     base_url = "https://www.biqulou.net/439/439271/{}.html"
    #     for i in range(2436753, 2441647):
    #         self.urls_list.append(base_url.format(i))

    def spider(self, url):
        """爬取数据，并对每一次的结果进行提取内容、保存"""
        # for url in self.urls_list:
        self.base_url = "https://www.biqulou.net/439/439271/"
        while url:
            response = requests.get(url)
            html_bytes = response.content
            # 提取内容
            title_str, content_list, url = self.handel_data(html_bytes)
            if not any([title_str, content_list, url]):
                break
            # 保存到文件中
            self.save_file(title_str, content_list)

    def handel_data(self, html_str):
        """
        处理html，提取所需的内容
        :param html_str:
        :return: title->str, content->list
        """
        element = html.fromstring(html_str)
        title_list = element.xpath('/html/body/div/div/div/h1/text()')
        content_list = element.xpath('/html/body/div/div/div[@id="content"]/text()')
        html_tail = element.xpath('//a[@id="pager_next"]/@href')

        if html_tail:
            next_url = self.base_url + html_tail[0]
        else:
            return None, None, None
        print(title_list)
        contents_list = []
        for e in content_list[:]:
            contents_list.append(str(e))
        return str(title_list[0]), contents_list, next_url

    def save_file(self, title, content_list):
        """保存文件"""

        with open("破冰行动.txt", "ab") as f:
            f.write(title.replace('…', "").encode())
            for line in content_list:
                if "　　" in line:
                    line = "\n" + line
                if "　　    " in line:
                    line = line.replace("　　    ", "　　")
                f.write(line.encode())

    def go(self):
        # self.make_urls()
        html = self.spider("https://www.biqulou.net/439/439271/2284951.html")


if __name__ == "__main__":
    # s = Spider()
    # s.go()
    pass

