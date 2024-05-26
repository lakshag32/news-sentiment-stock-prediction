#https://www.youtube.com/watch?v=NB8OceGZGjA&t=1569s
#https://www.youtube.com/watch?v=ztbFY_kL4jI&t=898s
#https://www.selenium.dev/documentation/
#https://stackoverflow.com/questions/52876136/google-search-next-pages-using-selenium

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

companies = ["nvidia","tesla",'apple','amd','alibaba','google','microsoft','facebook','AMC',]

username ='@mrcuberlg'
password = 'hello1234'

driver.get("https://x.com/i/flow/login")

time.sleep(5)

def login():
    username_textbox = driver.find_element(By.XPATH, "//input[contains(@class,'r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7')]")
    username_textbox.send_keys(username)

    next_button = driver.find_elements(By.XPATH, "//button[contains(@class,'css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-ywje51 r-184id4b r-13qz1uu r-2yi16 r-1qi8awa r-3pj75a r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l')]")[0]
    next_button.click()

    time.sleep(5)

    password_textbox = driver.find_element(By.XPATH,"//input[contains(@class,'r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7')]")
    password_textbox.send_keys(password)

    login_button = driver.find_element(By.XPATH,"//button[contains(@class,'css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-19yznuf r-64el8z r-1fkl15p r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l')]")
    login_button.click()

login()

time.sleep(5)

for company in ["nvidia"]: #companies: 
    queries = [f'{company}']#,f'{company}+yahoo',f'products+{company}',f'{company}+company', f'{company}+buy+or+sell', f'{company}+bad+or+good', f'{company}+ai', f'{company}+report', f'{company}+Q1',f'{company}+stock+split',f'{company}+finance']
    tweets = []
    for query in queries:
        url = f"https://x.com/search?q={query}&src=typed_query&f=live"
        driver.get(url)

        time.sleep(10)

        driver.stop_client()


