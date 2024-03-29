import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification, AdamW
from sklearn.model_selection import train_test_split
import torch
from torch.utils.data import DataLoader, TensorDataset, RandomSampler, SequentialSampler
from sklearn.metrics import accuracy_score
import os


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 加载数据集，仅选取 'message' 和 'sentiment_category' 列
df = pd.read_csv(r"C:\上課專案\Bet_Chinese\data\Data Augmentation - 複製.csv", usecols=['message', 'sentiment_category'], encoding='utf-8-sig')

# 分割数据集为训练集和测试集，并直接转换为字符串
train_texts, val_texts, train_labels, val_labels = train_test_split(df['message'].astype(str), df['sentiment_category'], test_size=0.2)

# 初始化BERT tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')

# 使用tokenizer进行编码
train_encodings = tokenizer(train_texts.tolist(), truncation=True, padding=True, return_tensors="pt")
val_encodings = tokenizer(val_texts.tolist(), truncation=True, padding=True, return_tensors="pt")

# 创建TensorDataset
train_data = TensorDataset(train_encodings['input_ids'], train_encodings['attention_mask'], torch.tensor(train_labels.values))
val_data = TensorDataset(val_encodings['input_ids'], val_encodings['attention_mask'], torch.tensor(val_labels.values))

# 创建DataLoader
batch_size = 32
train_dataloader = DataLoader(train_data, sampler=RandomSampler(train_data), batch_size=batch_size)
val_dataloader = DataLoader(val_data, sampler=SequentialSampler(val_data), batch_size=batch_size)

# 初始化模型，指定为2类（因为你的任务是二分类）
model = BertForSequenceClassification.from_pretrained("bert-base-chinese", num_labels=2).to(device)


# 优化器
optimizer = AdamW(model.parameters(), lr=5e-5)



# 训练模型
model.train()
for epoch in range(5):
    for batch in train_dataloader:
        batch = tuple(t.to(device) for t in batch)
        inputs = {'input_ids': batch[0], 'attention_mask': batch[1], 'labels': batch[2]}
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
    logits = outputs.logits
    predictions.extend(torch.argmax(logits, dim=-1).tolist())
    true_labels.extend(batch[2].tolist())


accuracy = accuracy_score(true_labels, predictions)
print(f'Accuracy: {accuracy}')

# 确保保存路径存在
model_save_path = r"C:\上課專案\Bet_Chinese\model"
tokenizer_save_path = r"C:\上課專案\Bet_Chinese\tokenizer"
os.makedirs(model_save_path, exist_ok=True)
os.makedirs(tokenizer_save_path, exist_ok=True)

# 保存模型和分词器
model.save_pretrained(model_save_path)
tokenizer.save_pretrained(tokenizer_save_path)
