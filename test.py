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

# 准备文本
text = "我還是很喜緩你，我想要繼續嘗試"  # 这里替换成你自己的文本
encoded_input = tokenizer(text, return_tensors='pt', padding=True, truncation=True, max_length=512)
input_ids = encoded_input['input_ids'].to(device)
attention_mask = encoded_input['attention_mask'].to(device)

# 预测
with torch.no_grad():
    outputs = model(input_ids=input_ids, attention_mask=attention_mask)
    predictions = softmax(outputs.logits, dim=1)

# 输出预测结果
# 假设类别0为负面，类别1为正面
pred_label = torch.argmax(predictions, dim=1).item()
print(f"Predicted label: {'Positive' if pred_label == 1 else 'Negative'}")
print(f"Confidence scores: {predictions.tolist()}")
