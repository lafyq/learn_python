from bs4 import BeautifulSoup
with open('D:/Python学习的项目存放/玩耍/wyy/day_01/day01_2_1/web/new_index.html') \
        as wb_data:
    soup = BeautifulSoup(wb_data, 'lxml')
    # print(soup)
    images = soup.select('body > div.main-content > ul > li > img')
    titles = soup.select('body > div.main-content > ul > li > div.article-info > h3 > a')
    cates = soup.select('body > div.main-content > ul > li > div.article-info > p.meta-info')
    descs = soup.select('body > div.main-content > ul > li > div.article-info > p.description')
    rates = soup.select('body > div.main-content > ul > li > div.rate > span')
    # print(images, titles, cates, descs, rates, sep='\n--------------------------\n')

info = []

for image, title, cate, desc, rate in zip(images, titles, cates, descs, rates):
    data = {
        'image': image.get('src'),
        'title': title.get_text(),
        'cate': list(cate.stripped_strings),
        'rate': rate.get_text()
    }
    # print(data)
    info.append(data)

for i in info:
    # 以下各种获取错误方法：i[rate], i.rate, i.rate.value
    if float(i['rate']) > 3:
        print(i)



"""
body > div.main-content > ul > li:nth-child(1) > img
body > div.main-content > ul > li:nth-child(1) > div.article-info > h3 > a
body > div.main-content > ul > li:nth-child(1) > div.article-info > p.meta-info > span:nth-child(2)
body > div.main-content > ul > li:nth-child(1) > div.article-info > p.description
body > div.main-content > ul > li:nth-child(1) > div.rate > span
"""