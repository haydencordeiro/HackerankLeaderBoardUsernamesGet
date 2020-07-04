
import time
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options # firefox
from selenium.webdriver.chrome.options import Options  # chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import json
import pandas as pd
import xlrd

driver = ''


def Login():
    global driver
    chrome_options = Options()
    chrome_options.add_argument("user-data-dir=HackerRankLeaderBoard")
    driver = webdriver.Chrome(options=chrome_options)


n = int(input('enter no of pages of leader board :'))
data = []
Login()
for i in range(1, n+1):
    driver.get(
        'https://www.hackerrank.com/contests/cod-it/leaderboard/{}'.format(i))
    time.sleep(5)
    a = driver.find_elements_by_xpath(
        '//a[@class="cursor leaderboard-hackername rg_5"]')
    for j in a:
        data.append(j.text)

df = pd.DataFrame(data, columns=['Username'])
df.to_excel('output.xlsx')
