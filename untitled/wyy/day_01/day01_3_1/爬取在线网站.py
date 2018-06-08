from bs4 import BeautifulSoup
import requests
import time

url = 'https://www.tripadvisor.cn/'

def get_attractions(url, data=None):
    wb_data = requests.get(url)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    imgs = soup.select('img.photo_image')
    # imgs = soup.select('lazyImgs[data]')
    country = soup.select('ul.tiles.easyClear > li > div.title > a.countryName')
    city = soup.select('ul.tiles.easyClear > li > div.title > a.cityName')
    target = []
    for co, ci in zip(country, city):
        tmp = {
            co.get_text(): ci.get_text()
        }
        target.append(tmp)
    print(target)

get_attractions(url)