#https://www.geeksforgeeks.org/python-convert-a-string-representation-of-list-into-list/#

import pandas as pd
import ast
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

nvidia_finance_titles = []
nvidia_stock_titles = []
nvidia_titles = []

nvidia_finance_desc = []
nvidia_stock_desc = []
nvidia_desc = []

nvidia_df = pd.read_csv("data//nvidia.csv")
nvidia_stock_df = pd.read_csv("data//nvidia_stock.csv")
nvidia_finance_df = pd.read_csv("data//nvidia_finance.csv")

for row in range(len(nvidia_df)): 
    row_data = ast.literal_eval(nvidia_df["content.results.main"][row])
    for site in row_data: 
        if "hour" in site["relative_publish_date"]: 
            nvidia_titles.append(site['title'])
            nvidia_desc.append(site["desc"])
        elif "minute" in site["relative_publish_date"]: 
            nvidia_titles.append(site['title'])
            nvidia_desc.append(site["desc"])

for row in range(len(nvidia_stock_df)): 
    row_data = ast.literal_eval(nvidia_stock_df["content.results.main"][row])
    for site in row_data: 
        if "hour" in site["relative_publish_date"]: 
            nvidia_stock_titles.append(site['title'])
            nvidia_stock_desc.append(site["desc"])

        elif "minute" in site["relative_publish_date"]: 
            nvidia_stock_titles.append(site['title'])
            nvidia_stock_desc.append(site["desc"])

for row in range(len(nvidia_finance_df)): 
    row_data = ast.literal_eval(nvidia_finance_df["content.results.main"][row])
    for site in row_data: 
        if "hour" in site["relative_publish_date"]: 
            nvidia_finance_titles.append(site['title'])
            nvidia_finance_desc.append(site["desc"])

        elif "minute" in site["relative_publish_date"]: 
            nvidia_finance_titles.append(site['title'])
            nvidia_finance_desc.append(site["desc"])

all_article_titles = nvidia_titles + nvidia_finance_titles + nvidia_stock_titles
all_article_descs = nvidia_desc + nvidia_finance_desc + nvidia_stock_desc

tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

total_headline_sentiment = 0 
total_desc_sentiment = 0 


for headline in all_article_titles:
    tokens = tokenizer.encode(headline, return_tensors='pt') #return pytorch tensor/s(?) from sentiment model output
    model_output_tensor = model(tokens)
    sentiment_rating = int(torch.argmax(model_output_tensor.logits))+1
    total_headline_sentiment += sentiment_rating

# for desc in all_article_descs:
#     tokens = tokenizer.encode(desc, return_tensors='pt') #return pytorch tensor/s(?) from sentiment model output
#     model_output_tensor = model(tokens)
#     sentiment_rating = int(torch.argmax(model_output_tensor.logits))+1
#     total_desc_sentiment += sentiment_rating

avg_NVIDIA_headline_sentiment = total_headline_sentiment/len(all_article_titles)
# avg_NVIDIA_desc_sentiment = total_desc_sentiment/len(all_article_titles)

print(avg_NVIDIA_headline_sentiment)
# print(avg_NVIDIA_desc_sentiment)



