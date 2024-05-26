#https://www.geeksforgeeks.org/python-convert-a-string-representation-of-list-into-list/#

import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import tqdm

companies = ["nvidia","tesla",'apple','amd','alibaba','google','microsoft']

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


# nvidia_titles = list(set(nvidia_titles))
# tesla_titles = list(set(tesla_titles))
# amd_titles = list(set(amd_titles))
# apple_titles = list(set(apple_titles))

# print(len(nvidia_titles))
# print(len(tesla_titles))
# print(len(amd_titles))
# print(len(apple_titles))

# tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
# model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

# total_nvidia_headline_sentiment = 0 
# total_tesla_headline_sentiment = 0 
# total_amd_headline_sentiment = 0 
# total_apple_headline_sentiment = 0 

# for headline in nvidia_titles:
#     tokens = tokenizer.encode(headline, return_tensors='pt') #return pytorch tensor/s(?) from sentiment model output
#     model_output_tensor = model(tokens)
#     sentiment_rating = int(torch.argmax(model_output_tensor.logits))+1
#     total_nvidia_headline_sentiment += sentiment_rating

# for headline in tesla_titles:
#     tokens = tokenizer.encode(headline, return_tensors='pt') #return pytorch tensor/s(?) from sentiment model output
#     model_output_tensor = model(tokens)
#     sentiment_rating = int(torch.argmax(model_output_tensor.logits))+1
#     total_tesla_headline_sentiment += sentiment_rating

# for headline in amd_titles:
#     tokens = tokenizer.encode(headline, return_tensors='pt') #return pytorch tensor/s(?) from sentiment model output
#     model_output_tensor = model(tokens)
#     sentiment_rating = int(torch.argmax(model_output_tensor.logits))+1
#     total_amd_headline_sentiment += sentiment_rating

# for headline in apple_titles:
#     tokens = tokenizer.encode(headline, return_tensors='pt') #return pytorch tensor/s(?) from sentiment model output
#     model_output_tensor = model(tokens)
#     sentiment_rating = int(torch.argmax(model_output_tensor.logits))+1
#     total_apple_headline_sentiment += sentiment_rating

# avg_nvidia_headline_sentiment = total_nvidia_headline_sentiment/len(nvidia_titles)
# avg_tesla_headline_sentiment = total_tesla_headline_sentiment/len(tesla_titles)
# avg_amd_headline_sentiment = total_amd_headline_sentiment/len(amd_titles)
# avg_apple_headline_sentiment = total_apple_headline_sentiment/len(apple_titles)



# # avg_NVIDIA_desc_sentiment = total_desc_sentiment/len(all_article_titles)

# print(f"Nvidia Sentiment: {avg_nvidia_headline_sentiment}") #  
# print(f"Tesla Sentiment: {avg_tesla_headline_sentiment}") #  
# print(f"amd Sentiment: {avg_tesla_headline_sentiment}") # 
# print(f"apple Sentiment: {avg_apple_headline_sentiment}") # 


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



