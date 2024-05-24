#https://www.geeksforgeeks.org/python-convert-a-string-representation-of-list-into-list/#

import pandas as pd
import ast
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

nvidia_titles = []
nvidia_desc = []

AU_nvidia = pd.read_csv('data//Australia_nvidia.csv', on_bad_lines='warn')
AU_nvidia_finance = pd.read_csv('data//Australia_nvidia finance.csv', on_bad_lines='warn')
AU_nvidia_stock = pd.read_csv('data//Australia_nvidia stock.csv', on_bad_lines='warn')

US_nvidia = pd.read_csv('data//United States_nvidia.csv', on_bad_lines='warn')
US_nvidia_finance = pd.read_csv('data//United States_nvidia.csv', on_bad_lines='warn')
US_nvidia_stock = pd.read_csv('data//United States_nvidia.csv', on_bad_lines='warn')

UK_nvidia = pd.read_csv('data//United Kingdom_nvidia.csv', on_bad_lines='warn')
UK_nvidia_finance = pd.read_csv('data//United Kingdom_nvidia.csv', on_bad_lines='warn')
UK_nvidia_stock = pd.read_csv('data//United Kingdom_nvidia.csv', on_bad_lines='warn')

IN_nvidia = pd.read_csv('data//India_nvidia.csv', on_bad_lines='warn')
IN_nvidia_finance = pd.read_csv('data//India_nvidia.csv', on_bad_lines='warn')
IN_nvidia_stock = pd.read_csv('data//India_nvidia.csv', on_bad_lines='warn')

CH_nvidia = pd.read_csv('data//China_nvidia.csv', on_bad_lines='warn')
CH_nvidia_finance = pd.read_csv('data//China_nvidia.csv', on_bad_lines='warn')
CH_nvidia_stock = pd.read_csv('data//China_nvidia.csv', on_bad_lines='warn')

RU_nvidia = pd.read_csv('data//Russia_nvidia.csv', on_bad_lines='warn')
RU_nvidia_finance = pd.read_csv('data//Russia_nvidia.csv', on_bad_lines='warn')
RU_nvidia_stock = pd.read_csv('data//Russia_nvidia.csv', on_bad_lines='warn')

US_new_nvidia_news = pd.read_csv('data//US_nvidia_data.csv',on_bad_lines='warn')

all_data = pd.concat([AU_nvidia, AU_nvidia_finance, AU_nvidia_stock,US_nvidia,US_nvidia_finance,US_nvidia_stock,UK_nvidia,UK_nvidia_finance,UK_nvidia_stock,IN_nvidia,IN_nvidia_finance,IN_nvidia_stock, CH_nvidia,CH_nvidia_finance,CH_nvidia_stock,RU_nvidia,RU_nvidia_finance,RU_nvidia_stock,US_new_nvidia_news], ignore_index=True, axis=0)

for row in range(len(all_data)): 
    print(row)
    row_data = ast.literal_eval(all_data["content.results.main"][row])
    for site in row_data: 
        if "hour" in site["relative_publish_date"]: 
            nvidia_titles.append(site['title'])
        elif "minute" in site["relative_publish_date"]: 
            nvidia_titles.append(site['title'])

all_article_titles = list(set(nvidia_titles))

print(len(all_article_titles))

tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

total_headline_sentiment = 0 
# total_desc_sentiment = 0 


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



