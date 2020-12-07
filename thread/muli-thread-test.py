from random import randint
from threading import Thread
from time import time, sleep

def download(filename):
  print('开始下载%s...' % filename)
  time_to_download = randint(5, 10)
  sleep(time_to_download)
  print('%s下载完成, 耗费了%d秒' % (filename, time_to_download))

def main():
  start = time()
  p1 = Thread(target=download, args=('python从入门到放弃.pdf',))
  p1.start()
  p2 = Thread(target=download, args=('Peking.docx',))
  p2.start()
  p1.join()
  p2.join()
  end = time()
  print('总共耗费了%.3f秒.' % (end - start))

if __name__ == '__main__':
  main()