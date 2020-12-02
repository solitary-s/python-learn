
class Person(object):

  __slots__ = ('_name', '_age', '_gender')
  
  def __init__(self, name, age):
    self._name = name
    self._age = age
  
  @property
  def name(self):
    return self._name
  
  @property
  def age(self):
    return self._age
  
  @age.setter
  def age(self, age):
    self._age = age

  def display(self):
    if self._age <= 16:
      print('%s在玩斗地主' % self._name)
    else:
      print('%s在玩飞行棋' % self._name)

def main():
  person = Person('tong', 12)
  person.display()
  person.age = 22
  person.display()
  # person.name = 'aloneness'
  person.display()
  person._gender = '男'
  print(person._gender)
  # person._is_gay = '否'



if __name__ == '__main__':
  main()