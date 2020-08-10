# 字符串
str1 = "I love fishc.com"
print(str1[:6])

# 字符串 大写变小写
str2 = "TONG"
print(str2.casefold())

# join拼接字符串  +(连接符)效率低
print('_'.join("FishC"))

# 格式化
str3 = "{0} love {1}.{2}".format("I", "FishC", "com")
print(str3)

# 位置参数
str4 = "{a} hate {b}.{c}".format(a="I", b="FishC", c="com")
print(str4)
