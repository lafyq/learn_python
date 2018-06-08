from bs4 import BeautifulSoup

with open('D:/Python学习的项目存放/玩耍/wyy/day_01/day01_2_1_homework/1_2_homework_required/index.html') \
        as wb_data:
    soup = BeautifulSoup(wb_data, 'lxml')
    # print(soup)
    images = soup.select('body > div > div > div.col-md-9 > div > div > div > img')
    prices = soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right')
    titles = soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a')
    reviews = soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right')
    grades_crawler = soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2) > span ')
    print(grades_crawler)  # 上一行是抓取所有的星星描述
    grades = []  # 设置一个空列表
    while len(grades_crawler) != 0:  # 循环长度不为零
        e = grades_crawler[0:5]  # 提取星星描述前五个元素（也就是一个商品的星级）
        grades.append(e)  # 把这五个商品星级的列表作为一个元素插入grades列表中
        del grades_crawler[0:5]  # 删除掉已抓取过的描述列表的前五个元素
    # print(grades)





for title, image, review, price, grade in zip(titles, images, reviews, prices, grades):
    star = []
    b = str(grade)  # 字符串化列表
    c = b.replace('<span class="glyphicon glyphicon-star"></span>', '★')  # 将描述实五角星的替换为图案
    d = c.replace('<span class="glyphicon glyphicon-star-empty"></span>', '☆')  # 将描述虚五角星的替换为图案
    star.append(d)  # 将转化完的结果逐个插入列表star中
    data = {
        'title': title.get_text(),
        'image': image.get('src'),
        'review': review.get_text(),
        'price': price.get_text(),
        'grade': ''.join(star).replace('[', '').replace(']', '').replace(',', '').replace(' ', '')
    }
    print(data)


"""
图片地址：body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > img
价格：body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > div.caption > h4.pull-right
商品标题：body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > div.caption > h4:nth-child(2) > a
评分量：body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > div.ratings > p.pull-right
评分星级：body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > div.ratings > p:nth-child(2) > span:nth-child(5)
"""