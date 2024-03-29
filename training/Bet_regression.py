import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification, AdamW, BertConfig
from sklearn.model_selection import train_test_split
import torch
from torch.utils.data import DataLoader, TensorDataset, RandomSampler, SequentialSampler
from torch import nn
from sklearn.metrics import mean_squared_error
import numpy as np
import os

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 加载数据集
df = pd.read_csv(r"C:\上課專案\Bet_Chinese\data\Data Augmentation - 複製.csv", encoding='utf-8-sig')

# 分割数据集
train_texts, val_texts, train_labels, val_labels = train_test_split(
    df['message'].astype(str), 
    df['sentiment_score'],  # 假设现在是情感得分
    test_size=0.2
)

# 初始化BERT tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')

# 编码
train_encodings = tokenizer(train_texts.tolist(), truncation=True, padding=True, return_tensors="pt")
val_encodings = tokenizer(val_texts.tolist(), truncation=True, padding=True, return_tensors="pt")

# 创建TensorDataset
train_data = TensorDataset(train_encodings['input_ids'], train_encodings['attention_mask'], torch.tensor(train_labels.values, dtype=torch.float))
val_data = TensorDataset(val_encodings['input_ids'], val_encodings['attention_mask'], torch.tensor(val_labels.values, dtype=torch.float))

# DataLoader
batch_size = 32
train_dataloader = DataLoader(train_data, sampler=RandomSampler(train_data), batch_size=batch_size)
val_dataloader = DataLoader(val_data, sampler=SequentialSampler(val_data), batch_size=batch_size)

# 修改模型配置为回归任务
config = BertConfig.from_pretrained("bert-base-chinese")
config.num_labels = 1  # 输出层改为1个神经元
model = BertForSequenceClassification(config).to(device)

# 优化器
optimizer = AdamW(model.parameters(), lr=5e-5)

# 训练模型
model.train()
for epoch in range(5):
    for batch in train_dataloader:
        batch = tuple(t.to(device) for t in batch)
        inputs = {
            'input_ids': batch[0],
            'attention_mask': batch[1],
            'labels': batch[2].unsqueeze(1)  # 确保labels的维度与模型输出一致
        }
        optimizer.zero_grad()
        outputs = model(**inputs)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
    print(f"Epoch {epoch+1}: Loss {loss.item()}")

# 评估模型
model.eval()
predictions, true_labels = [], []
for batch in val_dataloader:
    batch = tuple(t.to(device) for t in batch)
    inputs = {'input_ids': batch[0], 'attention_mask': batch[1]}
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits.squeeze().tolist()
