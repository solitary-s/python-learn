from time import time
from threading import Thread

import requests

count = 1

class DownloadHandler(Thread):
  def __init__(self, url):
    super().__init__()
    self.url = url
  
  def run(self):
    filename = self.url[self.url.rfind('/') + 1:]
    global count
    resp = requests.get(self.url)
    with open('%s.jpg' % count, 'wb') as f:
      f.write(resp.content)
    count += 1

def main():
  resp = requests.get('http://api.tianapi.com/topnews/index?key=e98b7cb4d50ec9215b4c0db9d1646e98')
  data_model = resp.json()

  for mm_dict in data_model['newslist']:
    url = mm_dict['picUrl']
    if url != '':
      DownloadHandler(url).start() 

if __name__ == '__main__':
  main()

  