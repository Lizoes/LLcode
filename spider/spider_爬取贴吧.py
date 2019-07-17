import requests
import os

"""
https://tieba.baidu.com/f?kw=破冰行动ie=utf-8&pn=0
https://tieba.baidu.com/f?kw=破冰行动ie=utf-8&pn=50
https://tieba.baidu.com/f?kw=破冰行动&ie=utf-8&pn=100
"""
base_url = "https://tieba.baidu.com/f?kw={}ie=utf-8&pn={}"
urls_list = []
h = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

tieba_title = "破冰行动"
start_page = int(input("开始页:")) - 1
end_page = int(input("终止页:"))

for page in range(start_page, end_page):
    urls_list.append(base_url.format(tieba_title, page * 50))

# 创建文件夹
path = os.path.abspath('.')
dir = path + "\\" + tieba_title
if not os.path.exists(dir):
    os.makedirs(dir)

page = 1
for url in urls_list:
    response = requests.get(url, headers=h)
    # html = response.content.decode("utf8")
    html = response.content
    file_dir = dir + "\\"
    with open(file_dir + "破冰行动贴吧_page" + str(page) + ".html", "a", encoding="utf-8") as f:
        f.write(str(html))
    page += 1
