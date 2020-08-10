# import funcation
import sys
import color as c
# import funcation

# 搜索路径
print(sys.path)


# funcation.myFirstFuncation()


def test():
    c.printColor()


# 确保文件单独运行的时才会执行test()函数
if __name__ == '__main__':
    test()
