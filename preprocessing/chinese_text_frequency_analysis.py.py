import jieba
import pandas as pd
from collections import Counter
import re

# 定義一個函數來加載停用詞
def load_stopwords(stopwords_path):
    with open(stopwords_path, 'r', encoding='utf-8') as file:
        stopwords = set([line.strip() for line in file])
    return stopwords

# 文本清洗函數（去除標點符號和數字）
def clean_text(text):
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    text = pattern.sub('', text)
    return text

# 分詞並去除停用詞
def tokenize(text, stopwords):
    words = jieba.cut(text)
    return [word for word in words if word not in stopwords and word != ' ']

# 主函數處理流程
def process_messages(csv_path, stopwords_path):
    # 加載停用詞
    stopwords = load_stopwords(stopwords_path)
    
    # 讀取CSV文件
    df = pd.read_csv(csv_path)
    
    # 清洗並分詞
    df['message'] = df['message'].astype(str).apply(clean_text)
    # df['tokens'] = df['message'].apply(lambda x: tokenize(x, stopwords))
    
    # 統計詞頻
    word_counts = Counter()
    df['message'].apply(word_counts.update)
    
    # 按詞頻排序
    word_freq_df = pd.DataFrame(word_counts.most_common(), columns=['word', 'count'])
    
    # 保存到CSV檔案
    word_freq_df.to_csv(r'C:\上課專案\Bet_Chinese\word_frequency.csv', index=False, encoding='utf_8_sig')
    
    return word_freq_df

# 假設CSV文件路徑和停用詞檔案路徑已經設定好
csv_path = r'C:\上課專案\Bet_Chinese\modified_csv_file_path_here.csv'  # 請替換成你的檔案路徑
stopwords_path = r'C:\上課專案\Bet_Chinese\data\cn_stopwords.txt'  # 請替換成你的停用詞檔案路徑

# 執行主函數
word_freq_df = process_messages(csv_path, stopwords_path)

# 打印出前幾個詞頻
print(word_freq_df.head())
