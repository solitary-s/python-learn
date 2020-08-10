try:
    f = open('record.txt')
    sum = 1 + '2'
    print(f.read())
    f.close()
except (OSError, TypeError) as reason:
    print("打开文件错误\n" + str(reason))
finally:
    f.close()


# with语句
try:
    with open('data.txt', 'w') as f:
        for line in f:
            print(line)
except OSError as reason:
    print("出错了" + str(reason))
