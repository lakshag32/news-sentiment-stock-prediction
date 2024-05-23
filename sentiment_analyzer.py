#https://www.geeksforgeeks.org/python-convert-a-string-representation-of-list-into-list/#

import pandas as pd
import ast

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
        print(site["relative_publish_date"])
        if "hour" in site["relative_publish_date"]: 
            nvidia_titles.append(site['title'])
            nvidia_desc.append(site["desc"])
        elif "minute" in site["relative_publish_date"]: 
            nvidia_titles.append(site['title'])
            nvidia_desc.append(site["desc"])

for row in range(len(nvidia_stock_df)): 
    row_data = ast.literal_eval(nvidia_stock_df["content.results.main"][row])
    for site in row_data: 
        print(site["relative_publish_date"])
        if "hour" in site["relative_publish_date"]: 
            nvidia_stock_titles.append(site['title'])
            nvidia_stock_desc.append(site["desc"])

        elif "minute" in site["relative_publish_date"]: 
            nvidia_stock_titles.append(site['title'])
            nvidia_stock_desc.append(site["desc"])

for row in range(len(nvidia_finance_df)): 
    row_data = ast.literal_eval(nvidia_finance_df["content.results.main"][row])
    for site in row_data: 
        print(site["relative_publish_date"])
        if "hour" in site["relative_publish_date"]: 
            nvidia_finance_titles.append(site['title'])
            nvidia_finance_desc.append(site["desc"])

        elif "minute" in site["relative_publish_date"]: 
            nvidia_finance_titles.append(site['title'])
            nvidia_finance_desc.append(site["desc"])

all_article_titles = nvidia_titles + nvidia_finance_titles + nvidia_stock_titles
all_article_descs = nvidia_desc + nvidia_finance_desc + nvidia_stock_desc
