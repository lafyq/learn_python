from bs4 import BeautifulSoup
import requests
import time

url = 'http://zh.58.com/diannao/0/?PGTID=0d35fe52-0038-e149-47bb-4144bfd125e5&ClickID=2'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text, 'lxml')

# #infolist > div.infocon.bizads.\31 2 > table > tbody > tr > td.img > a > img

# #jingzhun > tbody > tr:nth-child(1) > td.t.t_b > a
titles = soup.select('#jingzhun > tbody > tr > td.img > a > img')
print(len(titles))
for i in titles:
    print(i)
