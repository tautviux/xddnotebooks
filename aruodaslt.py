import selenium
import undetected_chromedriver as uc 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
import seaborn as sns
import requests as rq
import time # del sleep komandos


opcijos = Options()
opcijos.add_argument('--incognito')

driver = uc.Chrome(options=opcijos)

url = 'https://www.kauno.diena.lt'

driver.get(url)
time.sleep(3)

source = driver.page_source # pasiimam puslapio html koda


bs = BeautifulSoup(source, 'html.parser') #teoriskas isparsinome puslapio html
ResultsSet = bs.find_all('a', {'class':'articles-list-title'})
for elementas in ResultsSet:
  print('::ELEMENTAS::')
  print(elementas)
  print(elementas['href']) # ['href'] is atrinktos klases leidzia gauti linka(nuorada, adresa)
  print(elementas.text) #pasiekiame elementa esanti teksta siuo atveju straipsnio pavadinima


driver.close()
df = pd.DataFrame()
df.to_csv('afailo, csav pavadinimas')

