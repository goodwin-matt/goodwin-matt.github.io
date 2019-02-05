import requests
from bs4 import BeautifulSoup
import csv

page = requests.get('https://www.walmart.com/ip/Human-Anatomy-Physiology/262015750')
soup = BeautifulSoup(page.text, 'html.parser')
test =soup.find_all('span', class_="price-group")
m = test[0]
price = float(str(m.get('aria-label'))[1:])

fields=[price]
with open('anat_phys_book.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(fields)
