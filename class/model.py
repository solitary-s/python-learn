
class Student(object):

  __sex = '男'

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def study(self, course_name):
    print("%s正在学习%s." %(self.name, course_name))

  def watch_movie(self):
    if (self.age > 16):
      print('%s在看鬼灭之刃.' %self.name)
    else:
      print('%s在看火影忍者.' %self.name)

def main():
  stu1 = Student("tong", 23)
  stu1.study("python")
  stu1.watch_movie()
  print(stu1._Student__sex)

  stu2 = Student("aloneness", 12)
  stu2.study("why is a man")
  stu2.watch_movie()

if __name__ == '__main__':
  main()