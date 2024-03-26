#針對csv每列進行測試並給出情緒分數以給熱力圖

import pandas as pd
import torch
from transformers import BertTokenizer, BertForSequenceClassification
from torch.nn.functional import softmax

# 加载模型和分词器
model_path = r"C:\上課專案\Bet_Chinese\model"
tokenizer_path = r"C:\上課專案\Bet_Chinese\tokenizer"

model = BertForSequenceClassification.from_pretrained(model_path)
tokenizer = BertTokenizer.from_pretrained(tokenizer_path)

# 检查是否有可用的GPU，如果没有，则使用CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# 读取CSV文件
df = pd.read_csv(r"C:\上課專案\UdicOpenData\processed_texts.csv", encoding='utf-8-sig')

# 准备一个空DataFrame来存储结果
results_df = pd.DataFrame()

# 对CSV中的每行文本进行情绪分析
for index, row in df.iterrows():
    text = str(row['processed_text']).strip()
    if not text:
        print(f"Skipping empty text at row {index}")
        continue  # 跳过空字符串

    encoded_input = tokenizer(text, return_tensors='pt', padding=True, truncation=True, max_length=512)
    
    # 检查是否成功获取了input_ids和attention_mask
    if 'input_ids' not in encoded_input or 'attention_mask' not in encoded_input:
        print(f"Failed to tokenize text at row {index}")
        continue  # 如果分词或编码失败，则跳过

    input_ids = encoded_input['input_ids'].to(device)
    attention_mask = encoded_input['attention_mask'].to(device)

    # 尝试进行预测
    try:
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
    except Exception as e:
        print(f"Model prediction failed at row {index} with error: {e}")
        continue  # 如果模型预测失败，则跳过当前迭代

    predictions = softmax(outputs.logits, dim=1)
    
    # 预测
    with torch.no_grad():
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        predictions = softmax(outputs.logits, dim=1)
        
    # 获取预测标签和置信度
    pred_label = torch.argmax(predictions, dim=1).item()
    confidence_scores = predictions.tolist()[0]
    
    # 定义情绪分类
    emotion_label = {
        0: 'Neutral',
        1: 'Positive',
        2: 'Negative',
        3: 'Mixed'
    }

    # 将结果添加到DataFrame
    results_df = pd.concat([results_df, pd.DataFrame({
        'Text': [text],
        'Predicted Label': [emotion_label[pred_label]],
        'Confidence Score Neutral': [confidence_scores[0]],
        'Confidence Score Positive': [confidence_scores[1]],
        'Confidence Score Negative': [confidence_scores[2]],
        'Confidence Score Mixed': [confidence_scores[3]]
    })])

# 将分析结果保存到新的CSV文件
results_df.to_csv('analysis_results.csv', index=False, encoding='utf-8-sig')
