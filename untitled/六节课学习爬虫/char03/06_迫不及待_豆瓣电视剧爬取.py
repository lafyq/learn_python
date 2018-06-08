import requests
import json
from retrying import retry


class DoubanSpider(object):

    def __init__(self):
        self.temp_url = 'https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?os=ios&for_mobile=1&start={}&count=18&loc_id=108288&_=0'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
            'Referer': 'https://m.douban.com/tv/japanese'
        }

    @retry(stop_max_attempt_number=3)
    def _parse_url(self, url):
        print('*' * 100)
        response = requests.get(url, headers=self.headers, timeout=3)
        return response

    def parse_url(self, url):
        try:
            response = self._parse_url(url)
        except:
            response = None
        return response

    def get_content_list(self, response):  # 提取数据
        dict_data = json.loads(response.content.decode('utf-8'))
        # print(dict_data)
        content_list = dict_data["subject_collection_items"]
        total = dict_data['total']
        return content_list, total

    def save_content_list(self, content_list):
        with open('douban_film.txt', 'a', encoding='utf-8') as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write('\n')

    def run(self):
        num = 0
        total = 100
        # 1.start_url开始爬取的url
        while num < total + 18:
            url = self.temp_url.format(num)

            # 2.发送请求，获取响应
            response = self.parse_url(url)

            # 3.提取数据
            content_list, total = self.get_content_list(response)

            # 4.保存
            self.save_content_list(content_list)

            # 5.构造下一页的url地址， 循环2-5步
            num += 18

if __name__ == '__main__':
    spider = DoubanSpider()
    spider.run()