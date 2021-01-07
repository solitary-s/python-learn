from abc import ABCMeta, abstractmethod

class Employee(object, metaclass=ABCMeta):
  def __init__(self, name):
    self._name = name

  @property
  def name(self):
    return self._name
  
  @abstractmethod
  def get_salary(self):
    pass

class Manager(Employee):

  def get_salary(self):
    return 15000.0

class Programmer(Employee):
  def __init__(self, name, work_hours=0):
    super().__init__(name)
    self._work_hours=work_hours

  @property
  def work_hours(self):
    return self._work_hours

  @work_hours.setter
  def work_hours(self, work_hours):
    self._work_hours = work_hours
  
  def get_salary(self):
    return self._work_hours * 150.0

class Saleman(Employee):
  def __init__(self, name, sales=0):
    super().__init__(name)
    self._sales = sales

  @property
  def sales(self):
    return self._sales
  
  @sales.setter
  def sales(self, sales):
    self._sales = sales

  def get_salary(self):
    return 1200 + self._sales * 0.05

def main():
  emps = [Manager('tong1'), Programmer('aloneness1'), Saleman('salitary1'),
          Manager('tong2'), Programmer('aloneness2')]

  for emp in emps:
    if isinstance(emp, Programmer):
      emp.work_hours = int(input('请输入%s本月的工作时间' % emp.name))
    elif isinstance(emp, Saleman):
      emp.sales = int(input('请输入%s本月的销售额' % emp.name))
    print('%s本月的工资为%s' %(emp.name, emp.get_salary()))

if __name__ == '__main__':
  main()