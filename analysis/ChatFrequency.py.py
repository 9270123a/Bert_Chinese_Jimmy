import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.font_manager import FontProperties
# Load the data
data = pd.read_csv('data/new.csv')
data.drop('timestamp', axis=1, inplace=True)
# data.drop('sentiment_score', axis=1, inplace=True)
# print(data.head)
# simhei_font = FontProperties(fname=r"/Users/zirong/Desktop/bert/data/simhei.ttf")

# Convert the Datetime column to datetime type
data['datetime'] = pd.to_datetime(data['datetime'])

# Sort by datetime
data.sort_values('datetime', inplace=True)

# 首先標記出哪些行是回覆
data['Is Reply'] = data['isSend'].diff().ne(0)

# 然後計算所有訊息的時間差
data['Time Diff'] = data['datetime'].diff()

# 只保留回覆訊息的時間差
data.loc[data['Is Reply'] == False, 'Time Diff'] = pd.NaT
print('\n time diff check \n',data.head(20))
# # 筛选出 2020 年 7 月的数据
# july_2020_data = data[(data['datetime'].dt.year == 2020) & (data['datetime'].dt.month == 8)]

# # 打印结果查看
# print(july_2020_data)


# 篩選出有回覆時間的訊息
replies = data[data['Is Reply'] == True].copy()

# 計算回覆時間的總秒數
replies['Reply Time Minutes'] = replies['Time Diff'].dt.total_seconds() / 60

# 新增月份列
replies['Month'] = replies['datetime'].dt.to_period('M')
replies = replies[replies['datetime'] >= '2020-10']

# 按照 'sender' 和 'Month' 分組並計算平均回覆時間
grouped = replies.groupby(['sender', 'Month'])['Reply Time Minutes'].mean().reset_index()
# 重新命名列以反映它們是每月平均
grouped.rename(columns={'Reply Time Minutes': 'Monthly Average Reply Time'}, inplace=True)

# 現在 grouped 就是你想要的新的 DataFrame
new_df = grouped
print('newdf\n',new_df)
# 確保 'Monthly Average Reply Time' 列是數值型別
# new_df['Monthly Average Reply Time'] = pd.to_numeric(new_df['Monthly Average Reply Time'], errors='coerce')
# 将 'Month' 列转换为字符串格式
new_df['Month'] = new_df['Month'].astype(str)
new_df['sender'] = new_df['sender'].replace({'林政佑': 'jimmy', '王梓蓉': 'you'})
print('rename\n',new_df)
# 现在再尝试使用 seaborn 进行绘图
sns.lineplot(data=new_df, x='Month', y='Monthly Average Reply Time',hue='sender')

plt.xticks(rotation=45)  # 旋转 x 轴标签以改善可读性

plt.show()
