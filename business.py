import urllib2
from bs4 import BeautifulSoup
import csv

with open('links.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for link in reader:
        lvcoc_url = link[0]
        print (link[0])
        page = urllib2.urlopen(lvcoc_url)
        soup = BeautifulSoup(page, "lxml")
        main_container = soup.find_all('div', {'class': 'ListingResults_All_CONTAINER ListingResults_Level2_CONTAINER'})
        with open('business.csv', 'wb') as csvfile:
            count = 0
            writer = csv.writer(csvfile)
            for item in main_container:
                name= item.find('span',{'itemprop': "name"})
                name_txt = name.text
                street_address = item.find('span', {'itemprop':"street-address"})
                if street_address is None:
                    address = "None"
                else:
                    address = street_address.text
                description = item.find('div', {'class':"ListingResults_Level2_DESCRIPTIONBOX"})
                if description is None:
                    description_txt = "None"
                else:
                    description_txt = description.text
                phone = item.find('div', {'class':"ListingResults_Level2_PHONE1"})
                if phone is None:
                    phone_txt = "NO PHONE"
                else:
                    phone_txt = phone.text
                url = item.find('span', {'class': "ListingResults_Level2_VISITSITE"})
                if url is None:
                    website = "NO WEBSITE"
                else:
                    website = url.a.get("href")
                writer.writerow([name_txt.encode('utf-8')] + [address.encode('utf-8')] + [website.encode('utf-8')] + [phone_txt.encode('utf-8')] + [description_txt.encode('utf-8')])
                count = count + 1
                print (count)





