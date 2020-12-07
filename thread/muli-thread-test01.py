from random import randint
from threading import Thread
from time import time, sleep

class DownloadTask(Thread):
  def __init__(self, filename):
    super().__init__()
    self._filename = filename
  
  def run(self):
    print('开始下载%s...' % self._filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成, 耗费了%d秒' % (self._filename, time_to_download))

def main():
  start = time()
  p1 = DownloadTask('Python从入门到放弃.pdf')
  p1.start()
  p2 = DownloadTask('Peking.pdf')
  p2.start()
  p1.join()
  p2.join()
  end = time()
  print('总共耗费了%.2f秒.' % (end - start))

if __name__ == '__main__':
  main()