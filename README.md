
## Bert_Chinese_Jimmy 項目

項目概覽

Bert_Chinese_Jimmy 是一個使用 BERT 模型對中文文本進行情感分析的項目。它包含了從文本預處理、数据增强、模型訓練與評估，到生成词云和情感趋势分析等多个步骤的实现。


## 主要特色


文本預處理：包括清理聊天记录中的无关信息（例如贴图、图片等），将文本数据从 txt 格式转换为 CSV 格式，以及去除停用词。

数据增强：通过調整情感得分来优化模型的输入数据。

模型訓練：使用 BERT 模型对文本进行情感分析，包括二分类和回归任务的实现。

評估與分析：提供了工具来测试模型对 CSV 文件中每条数据的预测结果，并给出情感得分以便生成热力图。

词云生成：基于文本数据生成词云，以直观展示高频词汇。

情感趋势分析：绘制情感得分随时间变化的趋势图。


[App Screenshot](https://github.com/9270123a/Bert_Chinese_Jimmy/issues/1#issue-2208150962)

## 項目結構


```bash
Bert_Chinese_Jimmy/
├── data/                        # 数据目录，存放原始数据和处理后的数据
├── models/                      # 模型目录，存放训练好的模型
├── preprocessing/               # 数据预处理脚本
│   ├── clean_chat_records.py    # 清理聊天记录
│   ├── txtToCSV.py              # 将 txt 格式的聊天记录转换为 CSV 格式
│   └── ...                      # 其他预处理脚本
├── training/                    # 模型训练和评估脚本
│   ├── bet.py                   # BERT 模型训练脚本（二分类任务）
│   ├── Bet_regression.py        # BERT 模型训练脚本（回归任务）
│   └── ...                      # 其他训练和评估脚本
├── analysis/                    # 数据分析和可视化脚本
│   ├── EmotionTrendPlotter.py   # 情感趋势分析脚本
│   ├── generate_wordcloud.py    # 生成词云脚本
│   └── ...                      # 其他分析脚本
└── README.md                    # 項目文档



```


## 快速開始

準備數據：將您的原始聊天记录数据放入 data/ 目录中。

文本預處理：运行 preprocessing/ 目录下的脚本来清理和转换数据格式。

訓練模型：根据需求运行 training/ 目录下的脚本来训练模型。

评估与分析：使用 analysis/ 目录下的脚本对模型进行评估和结果分析。


## 貢獻指南


我們歡迎各種形式的貢獻，無論是改進現有功能、修复bug還是添加新的功能。請通過 GitHub 的 Pull Request 或 Issue 提交您的貢獻。

