from lxml import html

html_strs = None
with open(r"D:\MyCode\spider\text.html", "r", encoding="utf8") as f:
    html_strs = f.read()
element = html.fromstring(html_strs)
# 获取文本信息 test()
# 获取属性 @属性名称
title = element.xpath('/html/body/div/div/div/h1/text()')
# xpath语法的索引从1开始
