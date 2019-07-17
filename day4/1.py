import os
# 文件管理器
import time
start = time.time()
with open("D:\LLcode\myfile\JourneyToTheWest.txt", "r") as f:
    f.read()
end = time.time()
print("cost time:", end - start)

start2 = time.time()
with open("D:\LLcode\myfile\JourneyToTheWest.txt", "r") as f:
    for line in f.readline():
        pass
end2 = time.time()
print("cost time:", end2 - start2)



# w+:如果没有改文件，自动创建文件，写的时候回覆盖原数据
# a+:如果没有改文件，自动创建文件，写的时候回在最后追加，打开的时候光标去到最后的位置
# r+:如果没有改文件，则报错FileNotFoundError，写的时候回覆盖原数据，打开的时候光标去到最前的位置
