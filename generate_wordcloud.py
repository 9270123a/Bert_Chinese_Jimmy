from wordcloud import WordCloud
import pandas as pd
import jieba
import re
from collections import Counter
import matplotlib.pyplot as plt
# 如果 generate_wordcloud.py 這個檔案中含有生成詞雲的函數，並且你希望在這個程式碼中使用，
# 請確保該檔案存在且能夠被正確引用。否則，這行代碼可能會引起錯誤。
import generate_wordcloud as gw

def get_wordcloud(data_path, save_path, is_send=0):
    '''
    生成聊天記錄的詞雲圖。

    :param data_path: 聊天記錄文件csv的路徑。
    :param is_send: 0代表對方發送的消息，1代表我發送的消息。
    :param save_path: 詞雲圖片保存路徑。
    :return: None
    '''

    df = pd.read_csv(data_path, encoding='utf-8')
    texts = df[df['isSend'] == is_send]['message'].to_list()

    with open(r"C:\上課專案\Bet_Chinese\data\CNstopwords.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()
        stopwords = [line.strip().replace("\ufeff", "") for line in lines]

    # 分詞，去除停用詞和表情（表情都是這樣的格式：[xx]）
    norm_texts = []
    pattern = re.compile("(\[.+?\])")
    for text in texts:
        text = pattern.sub('', text).replace("\n", "")    # 刪除表情、換行符
        words = jieba.lcut(text)
        res = [word for word in words if word not in stopwords and word.replace(" ", "") != "" and len(word) > 1]
        if res != []:
            norm_texts.extend(res)

    count_dict = dict(Counter(norm_texts))
    wc = WordCloud(font_path="data/simhei.ttf", background_color='white', include_numbers=False,
                   random_state=0)      # 如果不指定中文字型路徑，詞雲會亂碼
    wc = wc.fit_words(count_dict)
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')  # 不顯示軸線和標籤
    plt.show()
    wc.to_file(save_path)

# 示例：繪製對方發送的信息的詞雲圖
get_wordcloud(r'C:\上課專案\Bet_Chinese\data\new.csv', r'C:\上課專案\wechat_analysis\wordcloud.png', 0) 
