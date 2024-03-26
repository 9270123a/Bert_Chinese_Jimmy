import pandas as pd
import jieba

def load_emotion_dict(emotion_dict_path):
    emotion_dict = {'positive': {}, 'negative': {}}
    df = pd.read_csv(emotion_dict_path)
    for index, row in df.iterrows():
        if row['senti'] == 'positive':
            emotion_dict['positive'][row['phrase']] = 1.1  # 正面词加乘系数
        else:
            emotion_dict['negative'][row['phrase']] = 0.9  # 负面词加乘系数
    return emotion_dict

def adjust_sentiment_scores(message, initial_score, emotion_dict):
    words = jieba.lcut(message)
    adjusted_score = initial_score
    for word in words:
        if word in emotion_dict['positive']:
            adjusted_score *= emotion_dict['positive'][word]
        elif word in emotion_dict['negative']:
            adjusted_score *= emotion_dict['negative'][word]
    return adjusted_score

def process_messages(data_path, emotion_dict_path):
    emotion_dict = load_emotion_dict(emotion_dict_path)
    df = pd.read_csv(data_path)
    df['adjusted_score'] = df.apply(lambda row: adjust_sentiment_scores(row['message'], row['sentiment_score'], emotion_dict), axis=1)
    df.to_csv(data_path, index=False, encoding='utf_8_sig')
    print("Adjusted scores have been saved.")

# Example usage
data_path = r'C:\上課專案\Bet_Chinese\data\processed_sentiment - 複製.csv'  # Path to the CSV file with initial sentiment scores
emotion_dict_path = r'C:\上課專案\Bet_Chinese\data\Tradition_Chinese_SentiDict.csv'  # Path to the emotion dictionary CSV file
process_messages(data_path, emotion_dict_path)
