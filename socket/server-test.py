from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime

def main():
  server = socket(family=AF_INET, type=SOCK_STREAM)

  server.bind(('192.168.2.105', 8789))

  server.listen(512)

  print('服务器开始监听...')

  while True:
    client, addr = server.accept()
    
    print(str(addr) + '连接到了服务器.')
    # 5.发送数据
    client.send(str(datetime.now()).encode('utf-8'))
    # 6.断开连接
    client.close()

if __name__ == '__main__':
  main()