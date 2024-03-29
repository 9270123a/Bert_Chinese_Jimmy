from snownlp import SnowNLP
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.sans-serif'] = ['Arial']
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

def get_sentiment_score(data_path):
    df = pd.read_csv(data_path, encoding='utf-8')
    texts = df['message'].to_list()
    scores = []
    for i in texts:
        s = SnowNLP(i)
        print(s.sentiments)  # 越接近0越负面，越接近1越正面
        scores.append(s.sentiments)
    df['sentiment_score'] = scores
    # 保存更改后的 DataFrame 回原 CSV 文件
    df.to_csv(data_path, index=False, encoding='utf-8-sig')

get_sentiment_score(data_path=r"C:\上課專案\wechat_analysis\new.csv")
