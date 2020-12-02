from math import sqrt

class Triangle(object):
  def __init__(self, a, b, c):
    self._a = a
    self._b = b
    self._c = c

  @staticmethod
  def is_valid(a, b, c):
    return a + b > c and b + c > a and a + c > b

  def perimeter(self):
    return self._a + self._b + self._c
  
  def area(self):
    half = self.perimeter() / 2
    return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))

def main():
   a, b, c = 1, 4, 5
   if Triangle.is_valid(a, b, c):
     t = Triangle(a, b, c)
     print(t.perimeter())
     print(t.area())
   else:
     print('无法构成三角形')

if __name__ == '__main__':
  main()