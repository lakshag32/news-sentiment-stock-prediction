
#Sources: https://www.youtube.com/watch?v=rQXL9A0ST5k
#https://github.com/kotartemiy/pygooglenews

from pygooglenews import GoogleNews
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import requests
from bs4 import BeautifulSoup
import re

#ideas on how to improve this: 
#1) scrape from multiple news data bases -- yahoo, google, etc.
#2) better sentiment analysis model for specifically news articles
#3) scrape more than just headlines and run analysis on that
#4) take news articles from multiple countries and translate? 
#5) add weighting to bigger news stations
#5) scrape with multiple search queries
#6) Scrape multilple topics on google news? 
#7) Web scrape youtube search results for Tesla


gn_US = GoogleNews(lang="en",country="US")
gn_IN = GoogleNews(lang="en",country="IN")
gn_AU = GoogleNews(lang="en",country="AU")

#18-19 to predict 20
TESLA_yest_news_US = gn_US.search(query="tesla", from_ ="2024-05-14", to_="2024-05-15")
TESLA_yest_news_IN = gn_IN.search(query="tesla", from_ ="2024-05-14", to_="2024-05-15")
TESLA_yest_news_AU = gn_AU.search(query="tesla", from_ ="2024-05-14", to_="2024-05-15")

yest_headlines_US = []
yest_headlines_IN = []
yest_headlines_AU = []
yest_headlines_UK = []

for item in TESLA_yest_news_US["entries"]: 
    yest_headlines_US.append(item["title"])

for item in TESLA_yest_news_IN["entries"]: 
    yest_headlines_IN.append(item["title"])

for item in TESLA_yest_news_AU["entries"]: 
    yest_headlines_AU.append(item["title"])

combined_list = yest_headlines_US+yest_headlines_IN+yest_headlines_AU + yest_headlines_UK
unique_list = list(set(combined_list))
print(len(unique_list))

tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

total_sentiment = 0 

for headline in unique_list:
    tokens = tokenizer.encode(headline, return_tensors='pt') #return pytorch tensor/s(?) from sentiment model output
    model_output_tensor = model(tokens)
    sentiment_rating = int(torch.argmax(model_output_tensor.logits))+1
    total_sentiment += sentiment_rating

avg_yesterday_TSLA_sentiment = total_sentiment/len(unique_list)
print(avg_yesterday_TSLA_sentiment)
