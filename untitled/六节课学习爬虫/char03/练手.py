import requests
import json
from retrying import retry

class Train(object):

    def __init__(self):
        self.url = 'https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?os=ios&for_mobile=1&start={}&count=18&loc_id=108288&_=0'
        self.headers = {
            'Referer': 'https://m.douban.com/tv/american',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',

        }

    @retry(stop_max_attempt_number=3)
    def _parse_url(self, url):
        response = requests.get(url, headers=self.headers, timeout=3)
        return response

    def parse_url(self, url):
        try:
            response = self._parse_url(url)
        except:
            response = None
        return response

    def get_content_list(self, response):
        res_dict = json.loads(response.content.decode('utf-8'))
        content_list = res_dict["subject_collection_items"]
        total = res_dict['total']
        return content_list, total

    def save_content_list(self, content_list):
        with open('test.txt', 'a', encoding='utf-8') as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write('\n')



    def run(self):
        num = 0
        total = 100

        # 获取url
        url = self.url.format(num)

        while num < total + 18:

            # 解析url,请求响应
            response = self.parse_url(url)

            # 处理数据
            content_list, total = self.get_content_list(response)

            # 保存数据
            self.save_content_list(content_list)

            # 循环
            num += 18

if __name__ == '__main__':
    t = Train()
    t.run()