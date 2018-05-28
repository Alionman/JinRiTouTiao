import sys
from pymongo import MongoClient
import jieba.analyse
from PIL import Image, ImageSequence
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator

#从数据库读取热点模块的文章，制作成云词图
def word_cloud(subject, image_path):
    content_list = []
    content_str = ''
    client = MongoClient('47.100.161.81', 27017)
    db = client.toutiao
    collection = db.headlines
    contents = collection.find({'subject':subject})
    for item in contents:
        if item['content'] not in content_list:
            content_list.append(item['content'])
    content_str = ' '.join(content_list)
    #运用jieba生成词频表
    result=jieba.analyse.textrank(content_str,topK=500,withWeight=True)
    keywords = dict()
    for i in result:
        keywords[i[0]]=i[1]
    image= Image.open(image_path)
    graph = np.array(image)
    #此配置生成图效果较好
    wc = WordCloud(font_path='/System/Library/Fonts/Msyh.ttf',background_color='Black',max_words=500,mask=graph)
     #根据词频表生成词云图
    wc.generate_from_frequencies(keywords)
    image_color = ImageColorGenerator(graph)
    plt.imshow(wc)
    plt.imshow(wc.recolor(color_func=image_color))
    plt.axis("off")
    plt.show()
    wc.to_file('%s.png' % subject)

if __name__ == '__main__':
    try:
        subject = sys.argv[1]
        image_path = sys.argv[2]
    except IndexError:
        print('param error')
    word_cloud(subject, image_path)
