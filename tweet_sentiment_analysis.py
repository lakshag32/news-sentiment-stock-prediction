#https://remarkablemark.org/blog/2020/08/26/python-iterate-csv-rows/
#https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character
import csv
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import tqdm

filename = 'tweets3.csv'
tweets = []

with open(filename, 'r',encoding="utf8") as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        tweets.append(row[1])

tweets = list(set(tweets))
print(len(tweets))

tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

total_company_sentiment = 0

for tweet in tweets: 
    tokens = tokenizer.encode(tweet, return_tensors='pt') #return pytorch tensor/s(?) from sentiment model output
    model_output_tensor = model(tokens)
    sentiment_rating = int(torch.argmax(model_output_tensor.logits))+1
    total_company_sentiment += sentiment_rating

avg_company_sentiment = total_company_sentiment/len(tweets)
print(f"nvidia twitter sentiment: {avg_company_sentiment}")





