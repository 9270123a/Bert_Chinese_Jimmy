import pandas as pd
import jieba

# 载入停用词
def load_stopwords(stopwords_path):
    with open(stopwords_path, 'r', encoding='utf-8') as file:
        stopwords = set(line.strip() for line in file)
    return stopwords

# 移除停用词
def remove_stopwords(text, stopwords):
    words = jieba.cut(text)
    return ' '.join(word for word in words if word not in stopwords)

# 处理CSV文件，移除停用词并删除空白行
def process_csv_remove_stopwords(input_csv_path, output_csv_path, stopwords_path):
    # 载入停用词
    stopwords = load_stopwords(stopwords_path)
    
    # 读取CSV文件
    df = pd.read_csv(input_csv_path)
    
    # 移除停用词
    df['processed_message'] = df['message'].apply(lambda x: remove_stopwords(x, stopwords))
    
    # 移除那些'processed_message'为空的行
    df = df[df['processed_message'].str.strip() != '']
    
    # 如果需要保留其他列，但只想移除文本为空的行，确保上一步完成后不要直接删除整行，
    # 而是应该基于'processed_message'列的内容是否为空来决定。
    
    # 保存处理后的数据到新的CSV文件
    df.to_csv(output_csv_path, index=False, encoding='utf_8_sig')
    
    print(f"已移除停用词并保存到新文件 {output_csv_path}")

# 输入CSV文件路径，输出CSV文件路径，停用词文件路径
input_csv_path = r'C:\上課專案\Bet_Chinese\processed_sentiment - 複製.csv'  # 输入文件路径，请根据需要调整
output_csv_path = r'C:\上課專案\Bet_Chinese\word_frequency.csv'  # 输出文件路径，请根据需要调整
stopwords_path = r'C:\上課專案\Bet_Chinese\data\cn_stopwords.txt'  # 停用词文件路径，请根据需要调整

# 执行处理
process_csv_remove_stopwords(input_csv_path, output_csv_path, stopwords_path)
