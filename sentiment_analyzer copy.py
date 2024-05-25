#https://www.geeksforgeeks.org/python-convert-a-string-representation-of-list-into-list/#

import pandas as pd
import ast
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

nvidia_titles = []
tesla_titles = []
amd_titles = []
apple_titles = []

nvidia_data = pd.read_csv("nvidia_first_20.csv")
tesla_data = pd.read_csv("tesla_first_20.csv")
amd_data = pd.read_csv("amd_first_20.csv")
apple_data = pd.read_csv("apple_first_20.csv")


for row in range(len(nvidia_data)): 
    row_data = ast.literal_eval(nvidia_data["content.results.main"][row])
    for site in row_data: 
        if "hour" in site["relative_publish_date"]: 
            print(site)
            nvidia_titles.append(site['title'])
        elif "minute" in site["relative_publish_date"]: 
            nvidia_titles.append(site['title'])

for row in range(len(tesla_data)): 
    row_data = ast.literal_eval(tesla_data["content.results.main"][row])
    for site in row_data: 
        if "hour" in site["relative_publish_date"]: 
            print(site)
            tesla_titles.append(site['title'])
        elif "minute" in site["relative_publish_date"]: 
            tesla_titles.append(site['title'])

for row in range(len(amd_data)): 
    row_data = ast.literal_eval(amd_data["content.results.main"][row])
    for site in row_data: 
        if "hour" in site["relative_publish_date"]: 
            print(site)
            amd_titles.append(site['title'])
        elif "minute" in site["relative_publish_date"]: 
            amd_titles.append(site['title'])

for row in range(len(apple_data)): 
    row_data = ast.literal_eval(apple_data["content.results.main"][row])
    for site in row_data: 
        if "hour" in site["relative_publish_date"]: 
            print(site)
            apple_titles.append(site['title'])
        elif "minute" in site["relative_publish_date"]: 
            apple_titles.append(site['title'])

nvidia_titles = list(set(nvidia_titles))
tesla_titles = list(set(tesla_titles))
amd_titles = list(set(amd_titles))
apple_titles = list(set(apple_titles))

print(len(nvidia_titles))
print(len(tesla_titles))
print(len(amd_titles))
print(len(apple_titles))

tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

total_nvidia_headline_sentiment = 0 
total_tesla_headline_sentiment = 0 
total_amd_headline_sentiment = 0 
total_apple_headline_sentiment = 0 

for headline in nvidia_titles:
    tokens = tokenizer.encode(headline, return_tensors='pt') #return pytorch tensor/s(?) from sentiment model output
    model_output_tensor = model(tokens)
    sentiment_rating = int(torch.argmax(model_output_tensor.logits))+1
    total_nvidia_headline_sentiment += sentiment_rating

for headline in tesla_titles:
    tokens = tokenizer.encode(headline, return_tensors='pt') #return pytorch tensor/s(?) from sentiment model output
    model_output_tensor = model(tokens)
    sentiment_rating = int(torch.argmax(model_output_tensor.logits))+1
    total_tesla_headline_sentiment += sentiment_rating

for headline in amd_titles:
    tokens = tokenizer.encode(headline, return_tensors='pt') #return pytorch tensor/s(?) from sentiment model output
    model_output_tensor = model(tokens)
    sentiment_rating = int(torch.argmax(model_output_tensor.logits))+1
    total_amd_headline_sentiment += sentiment_rating

for headline in apple_titles:
    tokens = tokenizer.encode(headline, return_tensors='pt') #return pytorch tensor/s(?) from sentiment model output
    model_output_tensor = model(tokens)
    sentiment_rating = int(torch.argmax(model_output_tensor.logits))+1
    total_apple_headline_sentiment += sentiment_rating

avg_nvidia_headline_sentiment = total_nvidia_headline_sentiment/len(nvidia_titles)
avg_tesla_headline_sentiment = total_tesla_headline_sentiment/len(tesla_titles)
avg_amd_headline_sentiment = total_amd_headline_sentiment/len(amd_titles)
avg_apple_headline_sentiment = total_apple_headline_sentiment/len(apple_titles)



# avg_NVIDIA_desc_sentiment = total_desc_sentiment/len(all_article_titles)

print(f"Nvidia Sentiment: {avg_nvidia_headline_sentiment}") #  
print(f"Tesla Sentiment: {avg_tesla_headline_sentiment}") #  
print(f"amd Sentiment: {avg_tesla_headline_sentiment}") # 
print(f"apple Sentiment: {avg_apple_headline_sentiment}") # 


"""
Log to check if this works: 

Day: 5/27/2024
    Stock: Nvidia
        Prediction: 
        Actual: 
    Stock: Tesla
        Prediction: 
        Actual: 
    Stock: AMD
            Prediction: 
            Actual: 
    Stock: Apple
            Prediction: 
            Actual: 

Day: 5/27/2024
    Stock: Nvidia
        Prediction: 
        Actual: 
    Stock: Tesla
        Prediction: 
        Actual: 
    Stock: AMD
            Prediction: 
            Actual: 
    Stock: Apple
            Prediction: 
            Actual: 

Day: 5/27/2024
    Stock: Nvidia
        Prediction: 
        Actual: 
    Stock: Tesla
        Prediction: 
        Actual: 
    Stock: AMD
            Prediction: 
            Actual: 
    Stock: Apple
            Prediction: 
            Actual: 

Day: 5/27/2024
    Stock: Nvidia
        Prediction: 
        Actual: 
    Stock: Tesla
        Prediction: 
        Actual: 
    Stock: AMD
            Prediction: 
            Actual: 
    Stock: Apple
            Prediction: 
            Actual: 
        
Day: 5/27/2024
    Stock: Nvidia
        Prediction: 
        Actual: 
    Stock: Tesla
        Prediction: 
        Actual: 
    Stock: AMD
            Prediction: 
            Actual: 
    Stock: Apple
            Prediction: 
            Actual: 
        
Day: 5/27/2024
    Stock: Nvidia
        Prediction: 
        Actual: 
    Stock: Tesla
        Prediction: 
        Actual: 
    Stock: AMD
            Prediction: 
            Actual: 
    Stock: Apple
            Prediction: 
            Actual: 
"""



