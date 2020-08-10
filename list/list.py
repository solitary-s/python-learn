
# 列表 可以是任意类型
number = [1, 2, 3, 4, 5]
print(number)

# 添加一个元素
number.append('tong')
print(number)

# 添加多个元素
number.extend([7, 8])
print(number)

# 插入元素
number.insert(0, 0)
print(number)

# 获取元素
print(number[0])

# 互换位置
number[0], number[2] = number[2], number[0]
print(number)

# remove 删除指定元素，如果没有报错
number.remove('tong')
print(number)

# del 删除指定index  del 列表名，直接删除整个列表
del number[0]
print(number)

# pop() 弹出指定index 默认是最后一个
number.pop()
print(number)

# 列表分片
num = number[1:3]
print(num)

# 列表进阶
list1 = list(range(1, 10))

# 第三个参数 步长
print(list1[::2])

# 翻转
print(list1[::-1])
