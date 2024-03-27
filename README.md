
## Bert_Chinese_Jimmy 項目

項目概覽

Bert_Chinese_Jimmy 是一個使用 BERT 模型對中文文字進行情緒分析的項目。 它包含了從文字預處理、數據增強、模型訓練與評估，到生成文字雲和情緒趨勢分析等多個步驟的實現。



## 主要特色


文字預處理：包含清理聊天記錄中的無關資訊（例如貼圖、圖片等），將文字資料從 txt 格式轉換為 CSV 格式，以及移除停用詞。

數據增強：透過調整情緒得分來優化模型的輸入數據。

模型訓練：使用 BERT 模型對文本進行情緒分析，包括二分類和回歸任務的實現。

評估與分析：提供了工具來測試模型對 CSV 檔案中每筆資料的預測結果。

文字雲生成：基於文字資料生成文字雲，以直觀展示高頻詞彙。

情緒趨勢分析：繪製情緒分數隨時間變化的趨勢圖。

## 項目結構


```bash
Bert_Chinese_Jimmy/
├── data/ # 資料目錄，存放原始資料和處理後的資料
├── models/ # 模型目錄，存放訓練好的模型
├── preprocessing/ # 資料預處理腳本
│ ├── clean_chat_records.py # 清理聊天記錄，包括移除無關資訊如貼圖、圖片等
│ ├── CutData.py # 處理數據，如選取數據的一部分進行分析或訓練
│ ├── Data Augmentation.py # 數據增強，透過調整情緒得分來優化模型的輸入數據
│ ├── RemoveStopwordsAndCleanCSV.py # 移除停用詞並清理CSV數據，以便進一步分析
│ ├── txtToCSV.py # 將 txt 格式的聊天記錄轉換為 CSV 格式
│ └── chinese_text_frequency_analysis.py.py # 文本频率分析，生成高频词汇统计
├── training/ # 模型訓練與評估腳本
│ ├── bet.py # BERT 模型訓練腳本（二分類任務）
│ ├── Bet_regression.py # BERT 模型訓練腳本（迴歸任務）
│ ├── Caculate_senti_score_Bert.py # 使用BERT進行情緒分數計算
│ ├── Calculate_sentiment_Score_.py # 使用SnowNLP計算情緒得分
│ └── test.py # 測試腳本，進行模型預測
├── analysis/ # 資料分析與視覺化腳本
│ ├── chinese_text_frequency_analysis.py.py # 文本頻率分析，產生高頻詞彙統計
│ ├── EmotionTrendPlotter.py # 情緒分數隨時間變化趨勢分析
│ ├── generate_wordcloud.py # 生成詞雲腳本，視覺化高頻詞彙
│ ├── TestCSVtoevertScore.py # 針對CSV每列進行測試並給出情緒分數，用於產生熱力圖
└── README.md # 項目文檔

```


## 快速開始

準備數據：將您的原始聊天記錄資料放入 data/ 目錄中。

文字預處理：執行 preprocessing/ 目錄下的腳本來清理和轉換資料格式。

訓練模型：根據需求執行 training/ 目錄下的腳本來訓練模型。

評估與分析：使用 analysis/ 目錄下的腳本對模型進行評估和結果分析。
## 架構圖
![messageImage_1711458518577](https://github.com/9270123a/Bert_Chinese_Jimmy/assets/157206678/f1e271ae-6ccb-4992-b359-d60b0b24bf53)

## 生成文字雲

```bash
generate_wordcloud.py
```
![文字雲](https://github.com/9270123a/Bert_Chinese_Jimmy/assets/157206678/6c7f7fb5-ca42-4c01-a632-086c7ec11a13)

## 生成情感折線圖
```bash
EmotionTrendPlotter.py
```
![Figure_2](https://github.com/9270123a/Bert_Chinese_Jimmy/assets/157206678/90296c05-2a84-4e85-b9d9-23b06b5e6981)
## 回覆頻率折線圖
```bash
ChatFrequency.py
```

![jimmy](https://github.com/9270123a/Bert_Chinese_Jimmy/assets/157206678/2f0b1ed4-4cc9-40de-acca-e30ab9f19436)

## 如何貢獻
我們歡迎所有形式的貢獻，包括但不限於新功能的提議、錯誤修正、文件更新。請發送Pull Request或創建Issue與我們交流。

## 聯繫方式
若有任何問題或建議，請透過以下方式聯繫我們：

Email: 9270123s@gmail.com

## 致謝
感謝所有支持和參與本專案的人，特別是資料集的提供者以及開源社群的貢獻者。
