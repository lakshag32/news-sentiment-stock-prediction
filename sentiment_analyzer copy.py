#https://www.geeksforgeeks.org/python-convert-a-string-representation-of-list-into-list/#

import pandas as pd
import ast
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

nvidia_titles = []
nvidia_desc = []

df2 = pd.read_csv('United States_nvidia2.csv')
df1 = pd.read_csv('United States_nvidia.csv')
all_data = pd.read_csv("data3.csv")

# concatenating df1 and df2 along rows
# all_data = pd.concat([data1, data2], axis=0)

for row in range(len(all_data)): 
    row_data = ast.literal_eval(all_data["content.results.main"][row])
    for site in row_data: 
        if "hour" in site["relative_publish_date"]: 
            print(site)
            nvidia_titles.append(site['title'])
            nvidia_desc.append(site['desc'])
        elif "minute" in site["relative_publish_date"]: 
            nvidia_titles.append(site['title'])
            nvidia_desc.append(site['desc'])


all_article_titles = list(set(nvidia_titles))
print(len(all_article_titles))

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



