import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_prepare_data(data_path):
    df = pd.read_csv(data_path, encoding='utf-8')
    if 'datetime' not in df.columns or 'sentiment_score' not in df.columns or 'isSend' not in df.columns:
        raise ValueError("CSV文件中必须包含名为'datetime'、'sentiment_score'和'isSend'的列。")
    df['datetime'] = pd.to_datetime(df['datetime'])
    return df

def visualize_sentiment_scores(df, save_path, time_frame='W'):
    plt.rcParams['font.sans-serif'] = ['Arial']
    plt.rcParams['axes.unicode_minus'] = False

    # 仅保留2021年及以后的数据
    df = df[df['datetime'] >= '2021-01-01']

    if time_frame.upper() == 'W':
        # 按周和isSend分组并计算平均情感得分
        df['week_start'] = df['datetime'].dt.to_period('W').apply(lambda r: r.start_time)
        sentiment_by_week_and_isSend = df.groupby(['week_start', 'isSend'])['sentiment_score'].mean().reset_index()
    else:
        # 如果需要支持其他时间框架
        sentiment_by_time_and_isSend = df.groupby([pd.Grouper(key='datetime', freq=time_frame), 'isSend'])['sentiment_score'].mean().reset_index()
        sentiment_by_week_and_isSend = sentiment_by_time_and_isSend  # 为了统一变量名，这里不做实际处理

    sns.lineplot(data=sentiment_by_week_and_isSend, x='week_start', y='sentiment_score', hue='isSend')
    plt.xticks(rotation=45)
    plt.title('情感得分随时间变化 (2021年及以后)')
    plt.xlabel('日期时间')
    plt.ylabel('情感得分均值')
    # 根据isSend值设置图例标签
    plt.legend(title='isSend', labels=['lin', 'wang'])
    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()

# 示例使用
csv_path = r"C:\上課專案\wechat_analysis\new.csv"
result_path = r"C:\上課專案\wechat_analysis\result\情感得分随时间变化_2021以后.png"
df = load_and_prepare_data(csv_path)
visualize_sentiment_scores(df, result_path, time_frame='W')  # 使用'W'代表按周
