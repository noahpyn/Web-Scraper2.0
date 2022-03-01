# web scraping multiple pages

from bs4 import BeautifulSoup
import requests 
url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
count = 1

# iterate through each link and only get integers of each page

for i in items:
    itemName = i.find('h4', class_='card-title').text.strip('\n')
    itemPrice = i.find('h5').text
    print('%s Price: %s, Item Name: %s' % (count, itemPrice, itemName))
    count = count + 1
pages = soup.find('ul', class_='pagination')
urls = []
links = pages.find_all('a', class_='page-link')
for link in links:
    pageNum = int(link.text) if link.text.isdigit() else None
    if pageNum != None:
        x = link.get('href')
        urls.append(x)
print(urls)

# create new request and scrape the page 
count = 1
for i in  urls:
    newUrl = url + i 
    response = requests.get(newUrl)

# paste in existing scraper 
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

# iterate through each link and scrape every page on webpage.

    for i in items:
        itemName = i.find('h4', class_='card-title').text.strip('\n')
        itemPrice = i.find('h5').text
        print('%s Price: %s, Item Name: %s' % (count, itemPrice, itemName))
        count = count + 1 
        