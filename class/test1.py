from time import sleep, time, localtime

class Clock(object):

  def __init__(self, hour=0, minute=0, second=0):
    self.hour = hour
    self.minute = minute
    self.second = second

  @classmethod
  def now(cls):
    ctime = localtime(time())
    return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

  def run(self):
    self.second += 1
    if self.second == 60:
      self.second = 0
      self.minute +=1
      if self.minute == 60:
        self.minute = 0
        self.hour += 1
        if self.hour == 24:
          self.hour = 0
  
  def show(self):
    return '%02d:%02d:%02d' %(self.hour, self.minute, self.second)

def main():
  while True:
    print(clock.show())
    sleep(1)
    clock.run()


if __name__ == '__main__':
  main()  