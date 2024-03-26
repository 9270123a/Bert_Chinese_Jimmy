import pandas as pd

# 加载CSV文件
df = pd.read_csv(r"C:\上課專案\Bet_Chinese\data\Data Augmentation - 複製.csv")

# 选择前5000条记录
df_head = df.head(5000)

# 如果需要，可以将这5000条记录保存到一个新的CSV文件
df_head.to_csv(r"C:\上課專案\Bet_Chinese\data\Data Augmentation - 複製.csv", index=False, encoding='utf_8_sig')