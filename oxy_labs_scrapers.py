#https://oxylabs.io/blog/how-to-scrape-google-search-results?utm_source=youtube&utm_medium=organic_video&utm_content=How%20to%20Scrape%20Google%20Search%20Results:%20A%20Step-by-Step%20Guide?utm_source=youtube&utm_medium=organic_video&utm_content=How%20to%20Scrape%20Google%20Search%20Results:%20Python%20Tutorial
#https://oxylabs.io

import requests
from pprint import pprint
import pandas as pd

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

payload = {
    "source": "google_search",
    "query": "nvidia finance",
    "parse": True,
    "context": [
        {
            "key": "tbm",
            "value": "nws"
        }
    ],
    "start_page": 2,
    "pages": 14,
    "limit": 10,
}

# payload = {
#     "source": "bing",
#     "url": "https://www.bing.com/news/search?q=nvidia&FORM=HDRSC7",
#     "limit": 30,
# }

# Get response.
response = requests.request(
    'POST',
    'https://realtime.oxylabs.io/v1/queries',
    auth=('LorenzoThePasta', '=362f5JPNFahs_Y'),
    json=payload,
)

if response.status_code != 200:
    print("Error - ", response.json())
    exit(-1)

pprint(response.json())

data = response.json()
df = pd.json_normalize(data['results'])
df.to_csv('nvidia_finance.csv', index=False)