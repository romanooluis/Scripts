import urllib2
from bs4 import BeautifulSoup
import csv

lvcoc_url = "http://web.lehighvalleychamber.org/allcategories"
page = urllib2.urlopen(lvcoc_url)
soup = BeautifulSoup(page, "lxml")

url = "http://web.lehighvalleychamber.org"
cat_left = soup.find_all("div", class_='halfWidth left')
links_left = cat_left[0].find_all("a")
links_list = []
count = 0

with open('links.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    for links1 in links_left:
        lasturlpart = links1.get("href")
        fullurl = url + lasturlpart
        writer.writerow([fullurl])
        count = count + 1

print ("Enlaces de {} Categorias obtenidas".format(count))











