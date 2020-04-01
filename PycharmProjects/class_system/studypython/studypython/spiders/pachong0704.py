import urllib.request
import urllib.response
import urllib.error
try:
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36'}

    response = urllib.request.Request('http://python.org/',headers = headers)
    html = urllib.request.urlopen(response)
    result = html.read().decode("UTF-8")

except urllib.error.URLError as e:
    if hasattr(e,'reason'):
        print("错误原因是："+str(e.reason))
except urllib.error.HTTPError as e:
    if hasattr(e,'code'):
        print("错误状态码："+e.code)

# print(result)
print(result)

try:
    a = 10
    b = '10'
    c = a+ b
except Exception as e:
    print('错误信息：',e)

