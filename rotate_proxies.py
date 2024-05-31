#modified from: https://selmiabderrahim.medium.com/nordvpn-servers-instead-of-python-requests-proxies-works-for-selenium-urllib-mechanize-31ebd8f9cdac

import os
import random
import time
import requests
windows_countries = ['United States']#, 'Canada','United Kingdom', 'South Africa', 'India', 'Australia']

current_dir = os.getcwd()

def rotate_proxy():
    os.chdir("C:\\Program Files\\NordVPN\\")
    server = f"nordvpn -c -g {random.choice(windows_countries)}"
    print(server)
    os.system(server)
    time.sleep(10)
    os.chdir(current_dir)