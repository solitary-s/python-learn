class CapStr(str):
    # __new__实例化第一个调用的方法，很少重写，使用python默认方案就行
    def __new__(cls, string):
        string = string.upper()
        return str.__new__(cls, string)


a = CapStr("I love python")

print(a)
