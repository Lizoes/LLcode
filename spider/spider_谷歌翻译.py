"""
https: // play.google.com / log?format = json & hasfast = true & authuser = 0
https://translate.google.cn/translate_a/single?client=webapp&sl=auto&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&otf=1&ssel=0&tsel=0&kc=4&tk=367698.211985&q=time
https://play.google.com/log?format=json&hasfast=true&authuser=0
"""
import requests

url = "https://translate.google.cn/#view=home&op=translate&sl=auto&tl=zh-CN&text={}"
word = input(">>>")
response = requests.get(url.format(word))
# html_str = response.content.decode("utf-8")
html_str = response.content.decode("GBK")
with open("a.html", "a") as f:
    f.write(html_str)
