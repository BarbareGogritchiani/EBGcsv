import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

file = open('boardGames.csv','w',encoding='utf-8_sig',newline='\n')
obj = csv.writer(file)
obj.writerow([ 'Title' , 'Price' , 'IMAGE_URL'])
page = 1
while page < 6:
    url = 'https://ebg.ge/catalog?s=board+games&t=buy&type=3&p=1' + str(page)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    sub_soup = soup.find('div', class_='product-bar')
    all_items = sub_soup.find_all('div', class_='col-sm-6 col-md-3 item_ebay')
    for each in all_items:
        img_url = each.img.attrs['src']
        title = each.find('div', class_='productCaption').a.p.text
        price = each.find('div', class_='product_prime_price').text
        obj.writerow([img_url,title,price])
    page += 1
    sleep(randint(15,20))