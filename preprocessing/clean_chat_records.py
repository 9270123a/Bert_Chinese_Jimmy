import pandas as pd
import re

# 假设已经读取了 CSV 文件到 DataFrame
df = pd.read_csv(r'C:\上課專案\wechat_analysis\data\new.csv', encoding='utf-8')

# 定义一个函数，用于判断是否应该删除该行
def check_for_removal(text):
    patterns = [r'\[\貼圖\]', r'\[\照片\]', r'☎.*']
    for pattern in patterns:
        if re.search(pattern, text):
            return True
    return False

# 使用 str.contains() 检查 'message' 列，并反转布尔值，仅保留不包含特定文本模式的行
df = df[~df['message'].str.contains(r'☎.*', regex=True)]

# 可能还需要应用 check_for_removal 函数来进一步清理数据
df['remove'] = df['message'].apply(check_for_removal)
df = df[df['remove'] == False]
df.drop('remove', axis=1, inplace=True)

# 保存清理后的 DataFrame 到新的 CSV 文件
df.to_csv('cleaned_data.csv', index=False, encoding='utf-8-sig')