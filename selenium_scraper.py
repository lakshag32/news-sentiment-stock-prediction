#https://www.youtube.com/watch?v=NB8OceGZGjA&t=1569s
#https://www.youtube.com/watch?v=ztbFY_kL4jI&t=898s
#https://www.selenium.dev/documentation/
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

companies = [] 

driver.get("https://www.google.com/search?q=nvidia&sca_esv=8d9cbe235051cbdc&tbm=nws&prmd=nsivmbt&source=lnt&tbs=qdr:d&sa=X&ved=2ahUKEwif4JaTxKqGAxUVADQIHdNpAVkQpwV6BAgBEAg&biw=1232&bih=616&dpr=1.5")
driver.implicitly_wait(2)

input_elements = driver.find_elements(By.XPATH,'//div[@class="n0jPhd ynAwRc MBeuO nDgy9d"]')

print(len(input_elements))
for element in input_elements: 
    print(element.text)