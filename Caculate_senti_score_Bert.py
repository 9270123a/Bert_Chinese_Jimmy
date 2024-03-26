import pandas as pd
import torch
from transformers import BertTokenizer, BertForSequenceClassification
from torch.nn.functional import softmax

# 加载模型和分词器
model_path = "C:\\上課專案\\Bet_Chinese\\model"
tokenizer_path = "C:\\上課專案\\Bet_Chinese\\tokenizer"

model = BertForSequenceClassification.from_pretrained(model_path)
tokenizer = BertTokenizer.from_pretrained(tokenizer_path)

# 检查是否有可用的GPU，如果没有，则使用CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# 加载CSV文件
csv_path = r"C:\上課專案\Bet_Chinese\data\line_chat.csv" # 请替换为您的CSV文件路径
df = pd.read_csv(csv_path)

def predict_sentiment(text):
    encoded_input = tokenizer(text, return_tensors='pt', padding=True, truncation=True, max_length=512)
    input_ids = encoded_input['input_ids'].to(device)
    attention_mask = encoded_input['attention_mask'].to(device)

    with torch.no_grad():
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        predictions = softmax(outputs.logits, dim=1)

    # 假设类别0为负面，类别1为正面，这里返回正面情感的概率
    return predictions[0][1].item()

# 为每条message打分
df['sentiment_score'] = df['message'].apply(predict_sentiment)

# 保存结果到新的CSV文件
output_csv_path = "C:\\上課專案\\Bet_Chinese\\data\\updated_with_scores.csv"  # 输出文件的路径
df.to_csv(output_csv_path, index=False, encoding='utf_8_sig')

print("Completed sentiment scoring and saved to new CSV file.")
