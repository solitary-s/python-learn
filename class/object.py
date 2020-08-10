class Turtle:
    color = 'green'
    weight = 10

    def climb(self):
        print("我正在很努力地向前爬...")


# 实例化
tt = Turtle()
print(type(tt))
print(tt.color)
print(tt.climb())

# 构造方法  __init__


class Potato:
    def __init__(self, name):
        self.name = name

    def kick(self):
        print("我叫%s" % self.name)


p = Potato("土豆")
p.kick()
print(p.name)

# 私有 成员变量前加上 __  实际上加入 _Person__name 就可以访问


class Person:
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name


p = Person('小甲鱼')
print(p._Person__name)


# 继承， Python支持多继承
