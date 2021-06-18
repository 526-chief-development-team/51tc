import csv
import os
import sqlite3

import jieba
from pprint import pprint
from wordcloud import WordCloud  # 词云
import jieba  # 分词
from matplotlib import pyplot as plt  # 绘图数据可视化
from PIL import Image  # 图片处理
import numpy as np  # 矩阵的生成


def post_desc_counter():
    """
    职位描述统计
    """
    # import thulac
    # post = open(
    #     os.path.join("/data", "post_require.txt"), "r", encoding="utf-8"
    # ).read()
    conn = sqlite3.connect('../Web')
    cur = conn.cursor()
    sql = '''
    select * from requirements
    '''
    data = cur.execute(sql)
    text = ''
    for item in data:
        text = text + str(item)
    # 使用 jieba 分词
    file_path = os.path.join("/Users/wangshengyu/PycharmProjects/douban/51同城/data", "user_dict.txt")
    jieba.load_userdict(file_path)
    seg_list = jieba.cut(text, cut_all=False)
    counter = dict()
    for seg in seg_list:
        counter[seg] = counter.get(seg, 1) + 1
    counter_sort = sorted(counter.items(), key=lambda value: value[1], reverse=True)
    pprint(counter_sort)
    with open(
            os.path.join("/Users/wangshengyu/PycharmProjects/douban/51同城/data", "post_pre_desc_counter.csv"), "w+", encoding="utf-8"
    ) as f:
        f_csv = csv.writer(f)
        f_csv.writerows(counter_sort)


def wordcloud():
    conn = sqlite3.connect('../Web')
    cur = conn.cursor()
    sql = '''
        select * from requirements
        '''
    data = cur.execute(sql)
    text = ''
    for item in data:
        text = text + str(item)
    cut = jieba.cut(text)
    string = ' '.join(cut)

    img = Image.open(r'/Users/wangshengyu/PycharmProjects/douban/51同城/data/Web.jpg')
    img_array = np.array(img)  # 将图片转换为数组
    wc = WordCloud(
        background_color='white',  # 设置背景色
        mask=img_array,
        font_path="Songti.ttc"
    )
    wc.generate_from_text(string)

    # 绘制图片
    fig = plt.figure(1)
    plt.imshow(wc)
    plt.axis('off')  # 是否显示坐标轴

    # plt.show()#显示生成的词云图片
    plt.savefig(r'/Users/wangshengyu/PycharmProjects/douban/51同城/data/wordcloud.PNG', dpi=500)


if __name__ == '__main__':
    wordcloud()
