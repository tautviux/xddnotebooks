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

#driver = uc.Chrome(options=opcijos)
driver = webdriver.Chrome(options=opcijos)


url = 'https://autoplius.lt/skelbimai/naudoti-automobiliai'

driver.get(url)

time.sleep(30)

source = driver.page_source

bs = BeautifulSoup(source, 'html.parser')

ResultsSet = bs.find_all('div', {'class':'announcement-body'})

# print(len(ResultsSet))
# print(ResultsSet)
for skelbimas in ResultsSet:
    try:
        addres_element  = skelbimas.find('div', {'class':'announcement-title'})
        #print(addres_element)
        tag = addres_element.find('div', {'class':'announcement-parameters '})
        # linkas = tag['href']
        kaina1 = addres_element.find('div', {'class':'announcement-pricing-info'})
        parametrai = addres_element.find('div', {'class':'announcement-parameters '})
        # tekstą galima pasiekti ir per 
        # .contents atributą
        tekstas = tag.contents #jums gražina list objektą su teksto gabalais
        f = ''
        k = ''
        k2 = ''
        # for b in kaina1:
        #   k = k + str(b).strip()
        # kaina = k.replace('<span class="list-item-price-v2">', ', ')
        # for c in kainakvm1:
        #   k2 = k2 + str(c).strip()
        # kainakvm = k2.replace('<span class="price-pm-v2">', ', ')  
        # for i in tekstas:
        #   f = f + str(i).strip() # str kad garantuotai butu tekstas  
        # adresas = f.replace('<br/>', ', ')
        # tuo tarpu .text gražina contents tekstą kaip vientisą
        # tekstas = tag.text.strip() # string metodas, skirtas pašalinti tarpus iš pradžios bei pabaigos
        print("====SKELBIMAS====")
        print(tag, kaina1, parametrai)
    except:
        pass
  
driver.close()


# jūsų atrankoje, kiek automobilių buvo au atomatu, mech, kokios jų buvo vidutinės kainos?
#advanced: su pie plot atvaizduokite gamintojų užimamą rinkos dalį (5 didžiausi + visi kiti)
