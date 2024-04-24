#!/bin/python3
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
# opcijos.add_argument('--incognito')
# opcijos.add_argument('--headless')

driver = uc.Chrome(options=opcijos)
# driver = webdriver.Chrome(options=opcijos)


url = 'https://www.aruodas.lt/butai/puslapis/2/'

driver.get(url)

time.sleep(20)

source = driver.page_source

bs = BeautifulSoup(source, 'html.parser')

ResultsSet = bs.find_all('div', {'class':'advert-flex'})

# print(len(ResultsSet))
# print(ResultsSet)
for skelbimas in ResultsSet:
    try:
        addres_element  = skelbimas.find('div', {'class':'list-adress-v2'})
        #print(addres_element)
        tag = addres_element.find('h3').find('a', href=True)
        linkas = tag['href']
        kaina1 = addres_element.find('span', {'class':'list-item-price-v2'})
        kainakvm1 = addres_element.find('span', {'class':'price-pm-v2'})
        # tekstą galima pasiekti ir per 
        # .contents atributą
        tekstas = tag.contents #jums gražina list objektą su teksto gabalais
        f = ''
        k = ''
        k2 = ''
        for b in kaina1:
          k = k + str(b).strip()
        kaina = k.replace('<span class="list-item-price-v2">', ', ')
        for c in kainakvm1:
          k2 = k2 + str(c).strip()
        kainakvm = k2.replace('<span class="price-pm-v2">', ', ')  
        for i in tekstas:
          f = f + str(i).strip() # str kad garantuotai butu tekstas  
        adresas = f.replace('<br/>', ', ')
        # tuo tarpu .text gražina contents tekstą kaip vientisą
        # tekstas = tag.text.strip() # string metodas, skirtas pašalinti tarpus iš pradžios bei pabaigos
        print("====SKELBIMAS====")
        print(linkas, adresas, kaina, kainakvm)
    except:
        pass
  
driver.close()