import socket
import urllib.request
import urllib.parse
import urllib.error

# response = urllib.request.urlopen('https://www.python.org')
# print(response.read().decode('utf-8'))

# data参数
# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())


# print(type(response))  # 查看响应类型
# print(response.status)  # 查看响应码
# print(response.getheaders())
# print(response.getheader('Server'))  # 查看服务器类型

# error模块
try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print("TIME OUT")