from bs4 import BeautifulSoup
import requests
import time


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}

proxies = {"http": "http://121.69.29.162:8118"}

url = 'https://weheartit.com/inspirations/anime?page='

data = []

def get_images(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')

    images = soup.select(
        '#main-container > div.grid-responsive > div.col.span-content > div > div > div > div > div > a > img')
    for image in images:
        data.append(image)
    print('now in ', url[-1])

for i in range(1, 3):
    get_images(url + str(i))
    time.sleep(2)

print(data)


#main-container > div.grid-responsive > div.col.span-content > div > div > div:nth-child(2) > div > div > a > img
