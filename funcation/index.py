
# 函数
def myFirstFuncation():
    print("这是我的第一个函数")


# 调用函数
myFirstFuncation()

# 函数文档


def exchangeRate(dollar):
    """美元 -> 人民币
    汇率为6.5
    """
    return dollar * 6.5


print(exchangeRate(10))
print(exchangeRate.__doc__)

# 关键字参数 默认参数


def saySomething(name, words, test="test"):
    print(name + '->' + words + '->' + test)


saySomething(words="hello", name="tong")

# 收集参数(可变参数) 可变参数最好放在最后面


def test(* params, extra="8"):
    print("收集参数是：", params)
    print("位置参数是：", extra)


test(1, 2, 3, 4, 5, 6, 7, 8)

# * 既可以打包又可以解包
a = [1, 2, 3, 4, 5, 6, 7, 8]
test(*a)

# 返回多值


def test1():
    return 1, '小甲鱼', 3.14


print(test1())  # (1, '小甲鱼', 3.14) 以元组的形式返回


# 闭包 如果在一个内部函数里，对在外部作用域的变量进行引用，那么内部函数就被认为是闭包
def funX(x):
    def funY(y):
        return x * y
    return funY


i = funX(8)
print(i(5))

print(funX(8)(5))


# lambda 表达式  冒号左边是参数，用逗号分隔，右边是返回值
def g(x): return 2 * x + 1


print(g(2))

# filter 过滤器
list1 = list(filter(lambda x: x % 2, range(10)))
print(list1)

# map 映射
list2 = list(map(lambda x: x * 2, range(10)))
print(list2)
