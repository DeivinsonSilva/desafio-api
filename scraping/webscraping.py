from urllib.request import urlopen
from bs4 import BeautifulSoup
from django.db import models
import pandas as pd

'''
def RetornaDf():

    quote = []
    author = []
    for i in range(1, 11):
        html = urlopen(f'https://quotes.toscrape.com/page/{i}/')
        bs = BeautifulSoup(html, 'html.parser')
        quote += bs.find_all('span', {'class':'text'})
        author += bs.find_all('small', {'class':'author'})
  
    df = pd.DataFrame()
    df['author']=author
    df['quote']=quote

    for i in range(len(df)):
        df['author'][i]=author[i].text
        df['quote'][i]=quote[i].text

    return(df)

dataframe = RetornaDf()

#for i in range(len(dataframe)):
#    b = Quote(author=dataframe['author'][i], author_quote=dataframe['quote'][i])
#    b.save()
'''