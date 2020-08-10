# 字典
dict1 = {'1': 'a', '2': 'b', '3': 'c'}
print(dict1)
print(dict1['2'])

# 空字典
empty = {}
print(type(empty))

# 创建
dict((('F', 70), ('i', 105)))
dict(one=1, two=2, three=3)

# 内置方法
# 用来创建并返回一个新的字典
dict2 = {}
dict2 = dict2.fromkeys((1, 2, 3), ('one', 'two', 'three'))
print(dict2)

# keys(), values() 和 items()
dict3 = {}
dict3 = dict3.fromkeys(range(10), 'good')
print(dict3.keys())
print(dict3.values())
print(dict3.items())
