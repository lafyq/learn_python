import requests

url = 'https://www.baidu.com/'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}

response = requests.get(url, headers = headers)
print(response)

"""获取相应回来的网页的具体内容"""
"""第一种方法："""
# response.encoding = 'utf-8'
#
# print(response.text)

"""第二种方法"""
# print(response.content.decode('utf-8'))

print(response.content.decode('utf-8'))



