f = open("cat_200_300.jpg")

# 文件打开
g = open("record.txt")

# 文件读取
text = g.read()
print(text)
g.close()

# 文件写入
w = open("record.txt", 'w')
w.write("写入数据")
w.close()
