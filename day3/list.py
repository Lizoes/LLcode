import random


def guess_word():
    """a game of guessing word"""
    words = ["tom", "jerry", "apple", "banana", "peal", "water", "ice", "one", "tw0", "three"]
    word = list(words[random.randint(0, len(words)-1)])
    print(word)
    length = len(word)
    underline = ["_ " for i in range(length)]
    count = 5
    while count > 0:
        # 输出当前状态
        output = "".join(underline)
        print(output)
        guess = input("guess a char(left guess %d times ):" % (count))
        if guess in word:
            index = word.index(guess)
            underline[index] = guess
            word[index] = " "
        else:
            count -= 1
        # 跳出循环的条件
        if word.count(" ") == length:
            break
    if count > 0:
        print("yur are right!")
    else:
        print("游戏结束！你没有猜对。")


def count_words():
    """counting words occurring times """
    paragraph = "a distinct section of a piece of writing,"
    # 替换
    paragraph.replace(",", " ").replace(":", " ").replace(";", " ").replace(".", " ").replace("?", " ")
    words = paragraph.split(" ")
    nums = {}

    for word in words:
        nums[word] = nums[word]+1 if word in nums else 1
        # nums[word] = nums.get(word, 0) + 1

    for word, num in nums.items():
        print(word, ": ", num)


def fibonacci(n):
    """return n numbers of fibonacci"""
    a, b = 1, 1
    count = 0
    while count < n:
        yield a
        count += 1
        a, b = b, a+b


def mysum(n):
    if n <= 0:
        return 0
    nums = [i for i in range(1, n+1)]
    return sum(nums)


if __name__ == "__main__":
    # count_words()
    # guess_word()
    # print(mysum(5))
    for i in fibonacci(10):
        print(i)


