import requests
from bs4 import BeautifulSoup
from csv import writer

headers = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29"
url = "https://www.makaan.com/listings?beds=2&propertyType=apartment&budget=2500000,12000000&listingType=buy&pageType=CITY_URLS&cityName=Pune&cityId=21&templateId=MAKAAN_CITY_LISTING_BUY"
response = requests.get(url, headers)

soup = BeautifulSoup(response.content, "html.parser")
lists = soup.find_all('div', class_="infoWrap")

with open('realestate.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Locality', 'Price', 'Area']
    thewriter.writerow(header)

    for list in lists:
        title = list.find('a', class_="typelink").text
        locality = list.find('span', itemprop="addressLocality").text
        price = list.find('span', itemprop="offers").text
        area = list.find('td', class_="lbl rate").text
        info = [title, locality, price, area]
        thewriter.writerow(info)
    
    

    
