import urllib.request
import urllib.parse
import json

content = input("请输入需要翻译的内容：")

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

data = {}
data['type'] = 'AUTO'
data['i'] = content
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['client'] = 'fanyideskweb'
data['salt'] = '15970269375930'
data['sign'] = 'c332a0e3d660934f878ddb59066a3a3c'
data['lts'] = '1597026937593'
data['bv'] = '7b07590bbf1761eedb1ff6dbfac3c1f0'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_REALTlME'

data = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request(url, data)
req.add_header('Referer', 'http://fanyi.youdao.com/')
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36')
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')
# print(html)
target = json.loads(html)
print("翻译结果： %s" % (target['translateResult'][0][0]['tgt']))
