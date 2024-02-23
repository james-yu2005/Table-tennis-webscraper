from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import pandas as pd

#checking if can access url
response = requests.get('https://www.pingpongdepot.com/?gad_source=1&gclid=CjwKCAiA_tuuBhAUEiwAvxkgTkf2PZQDyfDrrlzGQ8zI_Tjk8X3rj3RlxXC01hu54yzszwwqUcdw-xoCLpoQAvD_BwE')
if response.status_code != 200:
    print ("Could now fetch the page!")
    exit(1)
print("Successfully fetched the page!")

#searching for all article tags
soup = BeautifulSoup(response.content, 'html.parser') 
sections = soup.find_all('article')

#create arrays to store
saleNames = []
prices = []

#search through article tag and look for specific attributes
for article in sections:
    price = article.attrs['data-product-price']
    prices.append(price)
    saleName = article.attrs['data-product-title']
    saleNames.append(saleName)
    
#create data frame with pandas 
data_frame = pd.DataFrame({'Name of Sale': saleNames,'Prices': prices })
data_frame.Prices = pd.to_numeric(data_frame.Prices, errors='coerce')

#sort from least price to most price and print in csv file
sorted = data_frame.sort_values('Prices', ascending=True)
sorted.to_csv('Table_Tennis_Sales.csv', index = False, encoding = 'utf-8')
print('DataFrame is written to CSV File successfully.')

#outputting as excel file
file_name = 'Table_Tennis_Sales.xlsx'
sorted.to_excel(file_name)
print('DataFrame is written to Excel File successfully.')