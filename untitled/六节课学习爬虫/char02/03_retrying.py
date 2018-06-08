import requests
from retrying import retry

url = 'www.baidu.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}


@retry(stop_max_attempt_number=3)
def _parse_url(url):
    print('*' * 100)
    response = requests.get(url, headers=headers, timeout=3)
    return response


def parse_url(url):
    try:
        response = _parse_url(url)
    except:
        response = None
    return response

if __name__ == '__main__':
    response = parse_url(url)
    print(response)