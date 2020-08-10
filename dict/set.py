# 集合 类似Java set数据结构

num = {1, 2, 3, 4, 5}
print(type(num))

# 数据元素唯一
num.add(1)
print(num)  # {1, 2, 3, 4, 5}

# 不可变集合
set1 = frozenset({1, 2, 3, 4, 5})
# set1.add(6) 直接报错
