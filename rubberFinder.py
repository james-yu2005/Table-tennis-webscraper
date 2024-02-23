from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import pandas as pd

#checking if can access url
response = requests.get('https://www.pingpongdepot.com/rubber-2/')
if response.status_code != 200:
    print ("Could now fetch the page!")
    exit(1)
print("Successfully fetched the page!")

#searching for all article tags
soup = BeautifulSoup(response.content, 'html.parser') 
sections = soup.find_all('article')

#create arrays to store
indices = []
rubbers = []
prices = []
links = []

#search through article tag and look for specific attributes
for article in sections:
    rubber = article.attrs['data-name']
    rubbers.append(rubber)
    price = article.attrs['data-product-price']
    prices.append(price)
    index = article.attrs['data-position']
    indices.append(index)
    link = article.div.figure.a['href']
    links.append(link)
    
#create data frame with pandas
data_frame = pd.DataFrame({'Index#': indices, 'Rubber': rubbers,'Prices': prices, 'Links': links })
data_frame.Prices = pd.to_numeric(data_frame.Prices, errors='coerce')

#organize from least to most price and output csv file
sorted = data_frame.sort_values('Prices', ascending=True)
sorted.to_csv('Rubbers.csv', index = False, encoding = 'utf-8')
print('DataFrame is written to CSV File successfully.')

#outputting as excel file
file_name = 'Rubbers.xlsx'
sorted.to_excel(file_name)
print('DataFrame is written to Excel File successfully.')