#https://oxylabs.io/blog/how-to-scrape-google-search-results?utm_source=youtube&utm_medium=organic_video&utm_content=How%20to%20Scrape%20Google%20Search%20Results:%20A%20Step-by-Step%20Guide?utm_source=youtube&utm_medium=organic_video&utm_content=How%20to%20Scrape%20Google%20Search%20Results:%20Python%20Tutorial
#https://oxylabs.io

import requests
from pprint import pprint
import pandas as pd
import time

# payload = {
#     'source': 'google_search',
#     'query': 'shoes',
#     'domain': 'de',
#     'geo_location': 'Germany',
#     'locale': 'en-us',
#     'parse': True,
#     'start_page': 1,
#     'pages': 5,
#     'limit': 10,
# }

queries = ['nvidia yahoo','products nvidia','nvidia company', 'nvidia buy or sell', 'nvidia bad or good', 'nvidia ai', 'nvidia report', 'nvidia Q1']
# countries = ["United States",'Australia',"United Kingdom", "India"]
countries = ["United States"]

list_of_dfs = []
for country in countries: 
    for query in queries: 
        payload = {
            "source": "google_search",
            "query": query,
            "parse": True,
            "context": [
                {
                    "key": "tbm",
                    "value": "nws"
                }
            ],
            'geo_location': country,
            'locale': 'en-us',
            "pages": 14,
            "limit": 10,
        }

        # Get response.
        response = requests.request(
            'POST',
            'https://realtime.oxylabs.io/v1/queries',
            auth=('LorenzoThePasta', '=362f5JPNFahs_Y'),
            json=payload,
        )
        
        time.sleep(2)

        if response.status_code != 200:
            print("Error - ", response.json())

        # pprint(response.json())

        data = response.json()
        df = pd.json_normalize(data['results'])
        list_of_dfs.append(df)

all_data = pd.concat(list_of_dfs, ignore_index=True, axis=0)
all_data.to_csv('US_nvidia_data.csv', index=False)
