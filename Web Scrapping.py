import requests
from bs4 import BeautifulSoup
import pandas as pd
Text=[]

res = requests.get('https://en.wikipedia.org/wiki/Machine_learning')
soup = BeautifulSoup(res.text, 'lxml')
soup.select('mw-headline')
for i in soup.select('.mw-headline'):
    print(i.text)

    Text.append(i.text)
for i in soup.select('.mw-headline'):
    print(i.text)

    Text.append(i.text)