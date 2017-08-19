# -*- encoding:utf-8 -*-
"""import jieba.analyse
from os import path
from scipy.misc import imread
import matplotlib as mpl
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

if __name__ == "__main__":

    mpl.rcParams['font.sans-serif'] = ['FangSong']
    #mpl.rcParams['axes.unicode_minus'] = False

    content = open("testing.txt","rb").read()

    # tags extraction based on TF-IDF algorithm
    tags = jieba.analyse.extract_tags(content, topK=100, withWeight=False)
    text =" ".join(tags)
    text = unicode(text)
    # read the mask
    d = path.dirname(__file__)
    trump_coloring = imread(path.join(d, "Trump.jpg"))

    wc = WordCloud(font_path='simsun.ttc',
            background_color="white", max_words=300, mask=trump_coloring,
            max_font_size=40, random_state=42)

    # generate word cloud
    wc.generate(text)

    # generate color from image
    image_colors = ImageColorGenerator(trump_coloring)

    plt.imshow(wc)
    plt.axis("off")
    plt.show()


"""

#coding:utf-8
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
import jieba
import numpy as np
from PIL import Image

#读入背景图片
abel_mask = np.array(Image.open("stormtrooper_mask.png"))

#读取要生成词云的文件
text_from_file_with_apath = open(u'E:\\学\\python代码\\爬虫\\淘宝_js-m\\info.csv').read()

#通过jieba分词进行分词并通过空格分隔
wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)
#my_wordcloud = WordCloud().generate(wl_space_split) 默认构造函数
my_wordcloud = WordCloud(
            background_color='black',    # 设置背景颜色
            mask = abel_mask,        # 设置背景图片
            max_words = 100,            # 设置最大现实的字数
            stopwords = STOPWORDS,        # 设置停用词
            font_path = 'C:/Users/Windows/fonts/simkai.ttf',# 设置字体格式，如不设置显示不了中文
            max_font_size = 50,            # 设置字体最大值
            random_state = 30,            # 设置有多少种随机生成状态，即有多少种配色方案
                scale=.5
                ).generate(wl_space_split)

# 根据图片生成词云颜色
image_colors = ImageColorGenerator(abel_mask)
#my_wordcloud.recolor(color_func=image_colors)

# 以下代码显示图片
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()