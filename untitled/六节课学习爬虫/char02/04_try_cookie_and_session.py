import requests

login_url = 'http://www.aizhigu.com.cn/login.php'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}


data = {
    'user_name': '122wre123@qq.com',
    'user_pwd': 'clawer123'
}

# 实例化一个session
session = requests.session()

# 使用session发送post请求获取cookie
# 服务器设置在本地的cookie会存储在session中
session.post(login_url, data=data, headers=headers)


url = 'http://www.aizhigu.com.cn/member.php?act=order_list&type=cancel'

response = session.get(url, headers=headers, timeout=3)

with open('test.html', 'w', encoding='utf-8') as f:
    f.write(response.content.decode('utf-8'))