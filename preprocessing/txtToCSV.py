import pandas as pd
from datetime import datetime
import re

data = []

file_path = r"C:\上課專案\wechat_analysis\data\[LINE] 與Jimmy的聊天.txt"

# 这里我们不需要区分发送者了，因为你已经有sender的名字了
with open(file_path, 'r', encoding='utf-8') as file:
    current_date = None  # 初始化日期变量
    for line in file:
        # 调整正则表达式以匹配日期
        date_match = re.match(r'(\d{4}/\d{2}/\d{2})', line)
        if date_match:
            current_date = date_match.group(0)  # 更新当前处理的日期
            continue  # 跳过这一行，继续下一行

        # 调整正则表达式以匹配时间、发送人和消息
        match = re.match(r'(\d{2}:\d{2})\t(.+?)\t(.+)', line)
        if match:
            time, sender, message = match.groups()
            
            # 在这里，我们直接使用24小时制的时间，无需转换
            datetime_str = f"{current_date} {time}"
            datetime_obj = datetime.strptime(datetime_str, "%Y/%m/%d %H:%M")
            
            # 假设"羅胖🖤"是发信人时isSend为1，否则为0
            isSend = 1 if sender == "王梓蓉" else 0
            msg_type = 1  # 假定消息类型，这里你可能需要根据实际情况调整
            
            data.append({'datetime': datetime_obj, 'sender': sender, 'message': message, 'type': msg_type, 'isSend': isSend})

df = pd.DataFrame(data)

# 对DataFrame按时间排序
df.sort_values(by='datetime', inplace=True)

# 将datetime转换为timestamp，这会创建一个以秒为单位的时间戳
df['timestamp'] = df['datetime'].apply(lambda x: x.timestamp())

csv_file_path = 'line_chat.csv'
df.to_csv(csv_file_path, index=False, encoding='utf-8-sig')

print(f'Chat records have been saved to {csv_file_path}')
