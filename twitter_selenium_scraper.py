#https://www.youtube.com/watch?v=NB8OceGZGjA&t=1569s
#https://www.youtube.com/watch?v=ztbFY_kL4jI&t=898s
#https://www.selenium.dev/documentation/
#https://stackoverflow.com/questions/52876136/google-search-next-pages-using-selenium

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd
import requests
from rotate_proxies import rotate_proxy
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service,options=chrome_options)

companies = ["nvidia","tesla",'apple','amd','alibaba','google','microsoft','facebook','AMC']

username ='@mrcuberlg'
password = 'hello1234'

tweet_data = [] 
while True: 
        try: 
            rotate_proxy()
            driver.get("https://x.com/i/flow/login")
            break
        except:
            print("helo")
            continue
        
time.sleep(10)

def login():
    username_textbox = driver.find_element(By.XPATH, "//input[contains(@class,'r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7')]")
    username_textbox.send_keys(username)

    next_button = driver.find_elements(By.XPATH, "//button[contains(@class,'css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-ywje51 r-184id4b r-13qz1uu r-2yi16 r-1qi8awa r-3pj75a r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l')]")[0]
    next_button.click()
    time.sleep(10)
    password_textbox = driver.find_element(By.XPATH,"//input[contains(@class,'r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7')]")
    password_textbox.send_keys(password)

    login_button = driver.find_element(By.XPATH,"//button[contains(@class,'css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-19yznuf r-64el8z r-1fkl15p r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l')]")
    login_button.click()

login()

time.sleep(10)

while True: 
    try: 
        rotate_proxy()
        url = "https://x.com/search?f=live&q=%22nvidia%22%20lang%3Aen&src=typed_query"
        driver.get(url)
        break
    except:
        print("helo")
        continue

time.sleep(10)

while True: 
    tweets = driver.find_elements(By.XPATH,"//div[contains(@data-testid,'tweetText')]")
    for tweet in tweets: 
        fixed_tweet = tweet.text.replace("\n"," ")
        tweet_data.append(fixed_tweet)
    
    df = pd.DataFrame(tweet_data)
    df.to_csv("tweets3.csv",mode='a',header=False)

    #retry button class: class="css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-2yi16 r-1qi8awa r-3pj75a r-1loqt21 r-o7ynqc r-6416eg r-1vtznih r-1ny4l3l"
    
    tweet_data = []

    while True: 
        try:
            rotate_proxy()
            break
        except:
            print("hello")
            continue
        
    driver.refresh()

    time.sleep(30)