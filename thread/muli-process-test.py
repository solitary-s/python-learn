from multiprocessing import Process
from os import getpid
from time import sleep, time
from random import randint

def download_task(filename):
  print('启动下载进程，进程号[%s].' % getpid())
  print('开始下载%s...' % filename)
  time_to_download = randint(5, 10)
  sleep(time_to_download)
  print('%s下载完成, 耗费了%d秒' % (filename, time_to_download))

def main():
  start = time()
  p1 = Process(target=download_task, args=('python从入门到放弃.pdf',))
  p1.start()
  p2 = Process(target=download_task, args=('Peking.docx',))
  p2.start()
  p1.join()
  p2.join()
  end = time()
  print('总共耗费了%.2f秒.' % (end - start))

if __name__ == '__main__':
  main()
