
# 元组 不可以修改 类似字符串
tuple1 = tuple(range(1, 10))
print(tuple1)

# ,逗号才是元组的标识
temp1 = (1)
print(type(temp1))  # <class 'int'>

temp2 = (1,)
print(type(temp2))  # <class 'tuple'>

# 元组的更新和删除，通过切片拼接
temp = (1, 2, 4)
temp = temp[:2] + (3,) + temp[2:]
print(temp)
