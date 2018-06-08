import json
import requests

url = 'https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_japanese_hot/items?os=ios&for_mobile=1&start=0&count=18&loc_id=108288&_=1527502389950'

headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Referer': 'https://m.douban.com/tv/japanese',
}

response = requests.get(url, headers=headers)

# print(response.content.decode('utf-8'))

# 获取响应的json数据
json_str = response.content.decode('utf-8')

# 尝试将json_str转换成字典
ret_dict = json.loads(json_str)
print(ret_dict)  # 打印字典


"""
ensure_ascii=False  # 能够让文本不以ascii编码写入（即用要写入的字符串原来的编码写入）
indent=2  # 表示子节点在父节点的基础上缩进2个空格
"""
with open('douban_test.txt', 'w', encoding='utf-8') as f:
    f.write(json.dumps(ret_dict, ensure_ascii=False, indent=2))