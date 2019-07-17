import os
import jieba
# jieba 用于分割中文
# wordcloud
# matplotlib
# imageio

def test():
    paragraph = "《西游记》作者：吴承恩,跳树攀枝，采花觅果；抛弹子，么儿；跑沙窝，砌宝塔；赶蜻蜓，扑蜡；参老天，拜菩萨"
    cut_words_gen = jieba.cut(paragraph)     # 返回一个生成器
    cut_words_list = jieba.lcut(paragraph)   # 返回一个列表

    cut_words_cut_all_gen = jieba.cut(paragraph, cut_all=True)  #
    cut_words_cut_all_list = jieba.lcut(paragraph, cut_all=True)  #

    cut_words_cutfor_search_gen = jieba.lcut_for_search(paragraph)
    cut_words_cutfor_search_list = jieba.lcut_for_search(paragraph)
    print(list(cut_words_gen))
    for word in cut_words_gen:
        print(word)


class Demo():
    """
    1. 读文件
    2. 切割词语
    3. 统计
    """

    def count_words(self):
        # 用于记录词语出现的次数
        count = {}
        # 打开文件
        current_path = os.path.dirname(__file__)
        print(current_path)
        file = os.path.join(current_path, "West.txt")
        with open(file, "r") as f:
            pass


if __name__ == "__main__":
    demo = Demo()
    demo.count_words()
