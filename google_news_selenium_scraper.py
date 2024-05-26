#https://www.youtube.com/watch?v=NB8OceGZGjA&t=1569s
#https://www.youtube.com/watch?v=ztbFY_kL4jI&t=898s
#https://www.selenium.dev/documentation/
#https://stackoverflow.com/questions/52876136/google-search-next-pages-using-selenium

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd
from tqdm import tqdm

companies = ["nvidia","tesla",'apple','amd','alibaba','google','microsoft','facebook','AMC',]
countries =[] 

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

for company in companies: 
    queries = [f'{company}',f'{company}+yahoo',f'products+{company}',f'{company}+company', f'{company}+buy+or+sell', f'{company}+bad+or+good', f'{company}+ai', f'{company}+report', f'{company}+Q1',f'{company}+stock+split',f'{company}+finance']
    headlines = []

    for query in queries: 
        driver.get(f"https://www.google.com/search?q={query}&sca_esv=8d9cbe235051cbdc&tbm=nws&prmd=nsivmbt&source=lnt&tbs=qdr:d&sa=X&ved=2ahUKEwif4JaTxKqGAxUVADQIHdNpAVkQpwV6BAgBEAg&biw=1232&bih=616&dpr=1.5")
        
        
        while True: 
            time.sleep(2) #change to 4 or greater for actual
            titles = driver.find_elements(By.XPATH,'//div[@class="n0jPhd ynAwRc MBeuO nDgy9d"]')

            for title in titles: 
                headlines.append(title.text)

            try:
                driver.find_element(By.XPATH,"//*[contains(local-name(), 'span') and contains(text(), 'Next')]").click()
            except:
                break

    df = pd.DataFrame(headlines)
    df.to_csv(f"{company}_headlines.csv", index=False)
    