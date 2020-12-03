from abc import ABCMeta, abstractmethod
from random import randint, randrange

class Fighter(object, metaclass=ABCMeta):

  __slots__ = ('_name', '_hp')

  def __init__(self, name, hp):
    self._name = name
    self._hp = hp

  @property
  def name(self):
    return self._name
  
  @property
  def hp(self):
    return self._hp
  
  @hp.setter
  def hp(self, hp):
    self._hp = hp if hp >= 0 else 0
  
  @property
  def alive(self):
    return self._hp > 0

  @abstractmethod
  def attack(self, other):
    pass

class Ultraman(Fighter):
  __slots__ = ('_name', '_hp', '_mp')

  def __init__(self, name, hp, mp):
    super().__init__(name, hp)
    self._mp = mp
  
  def attack(self, other):
    other.hp -= randint(15, 25)

  def magic_attack(self, others):
    """魔法攻击
    :param others: 被攻击的群体
    :return: 使用魔法成功返回True否则返回False
    """
    if self._mp >= 20:
        self._mp -= 20
        for temp in others:
            if temp.alive:
                temp.hp -= randint(10, 15)
        return True
    else:
        return False
  
  def huge_attack(self, other):
    if self._mp >= 50:
      self._mp -= 50
      injury = other.hp * 3 // 4
      injury = injury if injury >= 50 else 50
      other._hp -= injury
      return True
    else:
      self.attack(other)
      return False
  
  def resume(self):
    incr_mp = randint(1, 10)
    self._mp += incr_mp
    return incr_mp

  def __str__(self):
    return '~~~%s奥特曼~~~\n' % self._name + \
      '生命值：%d\n' % self._hp + \
      '魔法值：%d\n' % self._mp 

class Monster(Fighter):
  __slots__ = ('_name', '_hp')

  def attack(self, other):
    other.hp -= randint(10, 20)
  
  def __str__(self):
    return '~~~%s小怪兽~~~\n' % self._name + \
        '生命值: %d\n' % self._hp


def is_any_alive(monsters):
  for monster in monsters:
    if monster.alive:
      return True
  return False

def select_alive_one(monsters):
  monsters_len = len(monsters)
  while True:
    index = randrange(monsters_len)
    monster = monsters[index]
    if monster.alive:
      return monster

def display_info(ultraman, monsters):
  print(ultraman)
  for monster in monsters:
    print(monster, end='')

def main():
  u = Ultraman("alonenss", 1000, 120)
  m1 = Monster("ab", 250)
  m2 = Monster("cd", 500)
  m3 = Monster("ef", 750)
  ms = [m1, m2, m3]
  fight_round = 1
  # print(u.alive)
  # print(ms)
  while u.alive and is_any_alive(ms):
    print('==========第%02d回合==========' % fight_round)
    m = select_alive_one(ms)
    skill = randint(1, 10)
    if skill <= 6:
      print('%s使用了普通攻击打了%s' % (u.name, m.name))
      u.attack(m)
      print('%s的魔法值回复了%d点' % (u.name, u.resume()))
    elif skill <= 9:
      if u.magic_attack(ms):
        print('%s使用了魔法攻击.' % u.name)
      else:
        print('%s使用魔法失败.' % u.name)
    else:
      if u.huge_attack(m):
        print('%s使用究极必杀技打了%s' % (u.name, m.name))
      else:
        print('%s使用了普通攻击打了%s' % (u.name, m.name))
        print('%s的魔法值回复了%d点' % (u.name, u.resume()))
    if m.alive:
      print('%s回击了%s.' % (m.name, u.name))
      m.attack(u)
    display_info(u, ms)
    fight_round += 1
  print('\n===========战斗结束==========')
  if u.alive:
    print('奥特曼获得了胜利')
  else:
    print('小怪兽胜利')

if __name__ == '__main__':
  main()
