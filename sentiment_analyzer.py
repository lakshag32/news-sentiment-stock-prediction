#https://www.geeksforgeeks.org/python-convert-a-string-representation-of-list-into-list/#

import pandas as pd
import ast
# first_page_data = ast.literal_eval(pd.read_csv("google.csv")["content.results.main"][0])
# for item in first_page_data:
#     print(item["title"])

google_titles = []
bing_titles = []

google_df = pd.read_csv("google.csv")
bing_df = pd.read_csv("bing.csv")


for row in range(len(google_df)): 
    row_data = ast.literal_eval(google_df["content.results.main"][row])
    for site in row_data: 
        print(site["title"])
        google_titles.append(site['title'])

for row in range(len(bing_df)): 
    row_data = ast.literal_eval(bing_df["content.results.main"][row])
    for site in row_data: 
        print(site["title"])
        bing_titles.append(site['title'])

print(len(list(set(bing_titles))))