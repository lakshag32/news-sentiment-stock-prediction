#ideas on how to improve this: 
#1) scrape from multiple news data bases -- yahoo, google, etc.
#2) better sentiment analysis model for specifically news articles
#3) scrape more than just headlines and run analysis on that
#4) take news articles from multiple countries and translate? 
#5) take news from diferent locations: US, UK, Australia, etc. 
#5) add weighting to bigger news stations
#import what we need


#https://www.youtube.com/watch?v=rQXL9A0ST5k&t=181s
#https://www.geeksforgeeks.org/python-save-list-to-csv/


from requests_html import HTMLSession
import time 
import csv 
   
fields = ['Article Title'] 

url = "https://news.google.com/rss/search?q=Nvidia%20when%3A1h&hl=en-US&gl=US&ceid=US%3Aen"
s = HTMLSession()
r = s.get(url)

collected_article_titles = []
start_time = time.time()
while True: 
    if time.time()-start_time >= 1800: 
        start_time = time.time()
        for title in r.html.find('title'):
            collected_article_titles.append(title.text) #may contain some garbage
            print(title.text)


        with open('data', 'w') as f:
            
            # using csv.writer method from CSV package
            write = csv.writer(f)
            
            write.writerow(fields)
            write.writerows([collected_article_titles])


