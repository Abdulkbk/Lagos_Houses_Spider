from itertools import count
import scrapy
import csv

# https://nigeriapropertycentre.com/for-sale/houses/detached-duplexes/lagos/agege/showtype

# https://nigeriapropertycentre.com/for-sale/houses/detached-duplexes/lagos/showtype?n=amity+estate

            

house_types = ['detached-uplexes', 'Semi-detached-Duplexes', 'Detached-bungalows', 'Semi-detached-Bungalows', 'Terraced-Bungalows', 'Terraced-Duplexes', 'Block-of-Flats']

normal_residents = ['Agbara-Igbesa', 'Agege', 'Ajah', 'Alimosho', 'Amuwo-Odofin', 'Apapa', 'Ayobo', 'Badagry', 'Egbe', 'Ejigbo', 'Eko-Atlantic-City', 'Epe', 'Gbagada', 'Ibeju', 'Ibeju' 'Lekki', 'Idimu', 'Ifako-Ijaiye', 'Iganmu', 'Ijaiye', 'Ijede', 'Ijesha', 'Ikeja', 'Ikorodu', 'Ikotun', 'Ikoyi', 'Ilashe', 'Ilupeju', 'Ipaja', 'Isheri', 'Isheri-North', 'Isolo', 'Itire', 'Ketu', 'Kosofe', 'Lagos-Island', 'Lekki', 'Magodo', 'Maryland', 'Mushin', 'Ogudu', 'Ojo', 'Ojodu', 'Ojota', 'Oke-Odo', 'Orile', 'Oshodi', 'Shomolu', 'Surulere', 'victoria-island', 'Yaba']

vip_residents = ['Airport Road', 'Amity Estate', 'Baruwa Estate', 'Beachwood Estate', 'Beckley Estate', 'Choice Estate', 'Citiview Estate', 'Cooperative Estate', 'Cornerstone Estate', 'Destiny Homes Estate', 'Divine Estate', 'Eko Akete Estate', 'Eleko Beach', 'Fidiso Estate', 'Genesis Estate', 'Gracias Emerald Estate', 'Greenfield Estate', 'Heritage Estate', 'Iroko Estate', 'Jonathan Estate', 'Jubilee Estate', 'Lekki Epe International Airport', 'Maplewood Estate', 'Maruwa Estate', 'Opic Estate', 'Otedola Estate', 'Rufus Laniyan Estate', 'Santos Valley Estate', 'Shagari Estate', 'Sparklight Estate']

def generateUrls(htypes, nr, vr):

    urls = []

    for i in htypes:
        for j in nr:
            u1 = f'https://nigeriapropertycentre.com/for-sale/houses/{i}/lagos/{j}/showtype'
            urls.append(u1)
        for k in vr:
            l = k.replace(' ', '+')
            u2 = f'https://nigeriapropertycentre.com/for-sale/houses/{i}/lagos/showtype?n={l}'
            urls.append(u2)

    return urls

# loo = 'https://nigeriapropertycentre.com/for-sale/houses/detached-duplexes/lagos/showtype?n=sparklight+estate'

# print(loo.split('/')[5])

def write_row(el):
    with open('lagos_houses.csv', 'a', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        # header = ['bedrooms', 'bathrooms', 'toilets', 'parking_space', 'type', 'town', 'state', 'price']
        writer.writerow(el)
    


class HousesSpider(scrapy.Spider):
    name = "houses"


    start_urls = generateUrls(house_types, normal_residents, vip_residents)

    def parse(self, response):
        for el in response.xpath('//div[@itemprop="itemListElement"]'):
            beds = el.xpath('.//ul[@class="aux-info"]/li[1]/span/text()').get()
            bathrooms = el.xpath('.//ul[@class="aux-info"]/li[2]/span/text()').get()
            toilets = el.xpath('.//ul[@class="aux-info"]/li[3]/span/text()').get()
            parking_space = el.xpath('.//ul[@class="aux-info"]/li[4]/span/text()').get()
            title = response.url.split('/')[5]
            state = 'lagos'
            price = el.xpath('.//span[@class="pull-sm-left"]/span[2]/text()').get().replace(',', '')
            write_row([beds, bathrooms, toilets, parking_space, title, state, price])

            print([beds, bathrooms, toilets, parking_space, title, state, price])
    







