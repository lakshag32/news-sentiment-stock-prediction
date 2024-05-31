#https://www.geeksforgeeks.org/python-convert-a-string-representation-of-list-into-list/#

import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import tqdm

companies = ["nvidia","tesla",'apple','amd','alibaba','google','microsoft','facebook','AMC']
tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
    
for company in companies: 
    company_data = pd.read_csv(f"{company}_headlines.csv")        
    company_headlines = list(set(company_data['0'].tolist()))

    total_company_sentiment = 0
    
    for headline in company_headlines: 
        tokens = tokenizer.encode(headline, return_tensors='pt') #return pytorch tensor/s(?) from sentiment model output
        model_output_tensor = model(tokens)
        sentiment_rating = int(torch.argmax(model_output_tensor.logits))+1
        total_company_sentiment += sentiment_rating
    
    avg_company_sentiment = total_company_sentiment/len(company_headlines)
    print(f"{company} sentiment with {len(company_headlines)} headlines: {avg_company_sentiment}")



