import pymongo

client = pymongo.MongoClient('127.0.0.1', 27017)
walden = client['walden']
sheet_tab = walden['sheet_tab']

path = 'D:/BaiduNetdiskDownload/Python实战：：四周实现爬虫系统/课程资料/课程源码及作业参考答案/Plan-for-combating-master/week2/2_1/2_1code_of_video/walden.txt'

with open(path, 'r') as f:
    lines = f.readlines()
    for index, line in enumerate(lines):
        data = {
            'index': index,
            'line': line,
            'words': len(line.split())
        }
        sheet_tab.insert_one(data)

for item in sheet_tab.find({'words': {'$lt': 5}}):
    print(item)