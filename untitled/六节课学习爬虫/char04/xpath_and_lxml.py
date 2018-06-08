import requests
from lxml import etree

url = 'https://www.x.com.cn/nan/'


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        }

response = requests.get(url, headers=headers)
html_str = response.content.decode('gbk')

# print(html_str)

element = etree.HTML(html_str)
# print(element)  # element对象：<Element html at 0x7f8ebbf52408>

"""这里的xpath要根据url的preview或者response来写，不要根据inspect，可以两个对照着来写"""
# img_list = element.xpath('//ul[@class="dl_right_cp_ul"]//img/@src')
# print(img_list)

# 需求：将商品的标题、价格、图片爬取
title_list = element.xpath('//ul[@class="dl_right_cp_ul"]//p[@class="cp_name"]/a/text()')
price_list = element.xpath('//ul[@class="dl_right_cp_ul"]//p[@class="cp_gm_bt"]/span/text()')
img_list = element.xpath('//ul[@class="dl_right_cp_ul"]//img/@src')

list = []
for title, price, img in zip(title_list, price_list, img_list):
    dict = {
        'title': title,
        'price': price[:-1],
        'img': img
    }
    print(dict)

