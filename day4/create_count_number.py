import random


def create_file():
    # eg.txt保存100000个随机数字（1~100）
    with open("D:\LLcode\day4\eg.txt", "a") as f:
        for i in range(100000):
            number = random.randint(1, 100)
            f.write(str(number) + "\n")


def count():
    d = {}
    # 统计每个数字出现的次数
    with open("D:\LLcode\day4\eg.txt", "r") as f:
        for line in f.readlines():
            d[line] = d.get(line) + 1 if line in d else 0
    # 对字典进行降序排序
    sorted_by_value = sorted(d.items(), key=lambda item: item[1], reverse=True)[0:10]
    # 把前10写到文件中myresult.txt
    with open("D:\LLcode\day4\myresult.txt", "a") as f:
        for item in sorted_by_value:
            f.write(item[0].replace("\n", "") + ":" + str(item[1]) + "\n")


if __name__ == "__main__":
    # create_file()         # 执行一次，创建100000个随机数字
    count()                 # 统计并把出现最多的前10个写到文件
