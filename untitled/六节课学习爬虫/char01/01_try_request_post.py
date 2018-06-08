import requests

url = 'http://fanyi.baidu.com/?aldtype=16047#auto/zh'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}

query_strings = {
    'from': 'zh',
    'to': 'en',
    'query': '你好世界',
}

response = requests.post(url, data=query_strings, headers = headers)

print(response)

print(response.content.decode())
