import pandas as pd 
import random 

df_lists= []
for i in range(5): 
    m_list =  random.sample(range(1, 50), 7)
    df = pd.DataFrame(m_list)
    df_lists.append(df)

all_data = pd.concat(df_lists, ignore_index=True, axis=0)

df.to_csv('test1.csv', index=False)
all_data.to_csv('test2.csv', index=False)

