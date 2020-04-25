def func():
    print("hello, python !")
    print("this is my body !")


func()


def hello(person):
    print("{0}, 你好吗？".format(person))
    print("{}, what's your problem ?".format(person))


p = "Alice"
hello(p)
print(hello(p))
print(type(hello(p)))
print(type(type(hello(p))))
print("********************************************")


def caculate(a, b):
    print("begin to caculate two number's sum: ")
    return a + b


print(caculate(1, 2))

help(print)

print("********************************************")


def printNine():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(i * j, end=" ")
        print()
    return None


printNine()
print("********************************************")


def printLine(o):
    '''
    打印一行九九乘法表
    :return:
    '''
    for i in range(1, o + 1):
        print(o * i, end=" ")
    print()


def jiujiu():
    for o in range(1, 10):
        printLine(o)


jiujiu()

print("********************************************")


# 普通参数
def normal_para(one, two, three):
    print(one + two)
    return None


normal_para(1, 2, 3)

print("********************************************")


# 默认参数
def default_para(one, two, three=300):
    print(one + two + three)
    return None


default_para(100, 200)

print("********************************************")


# 关键字参数
def key_para(one, two, three):
    print(one + two)
    print(three)
    return None


key_para(three=30, two=20, one=10)

print("********************************************")

## str 字符串
# 表示文字信息
# 用单引号，双引号，三引号括起来
s = 'I love my country'
ss = "I love my family"
sss = '''
    What a nice day today !
    It's sunny !
'''

print(s)
print(ss)
print(sss)

print("********************************************")

# 转义字符， 用一个特色的方法表示出一系列不方便写出的内容，比如回车键，换行符，退格键
# 借助反斜杠（转义符号）
# 不同系统对换行操作有不同的表示
#  windows: \n
#  Linux: \r\n
# 使用单双引号嵌套
s = "let's to do much!"
print(s)
# 使用转义符号
s = "let\'s to do much!"
print(s)
s = 'let\'s do something happiness.'
print(s)

print("********************************************")

# 表示斜杠
dir = "c:/usr/desktop/document"

print(dir)

# 表示反斜杠
dir = "c:\\usr\\desktop\\document"
print(dir)

# 回车换行
s = "Ich \nlieb \njing"
print(s)

print("********************************************")

s = "Ich \r\nlieb \r\njing"
print(s)

# 常用的转义字符
s = "hello \
,python"

print(s)

# 格式化
# 把字符串按照一定的格式打印或者填充出来
# 格式化
    # 传统格式化
    # format()函数
s = "I love jing"
print(s)
