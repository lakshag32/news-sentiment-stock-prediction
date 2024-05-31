import time
import pandas as pd

data = []

for i in range(100): 
    data.append(i)
    df = pd.DataFrame(data=data)
    time.sleep(5)
    df.to_csv("tweets.csv",mode='a',header=False)
    print(type(df))
