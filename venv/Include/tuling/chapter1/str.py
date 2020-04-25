# 传统格式化，使用%进行格式化
# %(百分号)也叫占位符
'''
    %s: 字符串
    %r: 字符串，但是使用repr而不是str
    %c: 整数转换为单个字符
    %d: 十进制整数
    %u: 无符号整数
    %o: 表示八进制
    %x: 十六进制，字母为小写（x为小写）
    %X: 十六进制，字母为大写（X为小写）
    %e; 浮点数（e为小写），例如 2.87e+12
    %E: 浮点数（E为大写），例如 2,87E+12
    %f, %F: 浮点数十进制形式
    %g, %G: 十进制形式浮点数或者指数浮点自动转换
    格式字符前出现整数表示次占位符所占位置的宽度
    格式字符前出现'-'表示左对齐
    格式字符前出现'+'表示右对齐
    0位数不足用'0'补齐
    width表示宽度
    pricision表示精度

'''
s = 'I love %s'
print(s % '小鲸鱼')
print("I love %s" % ' 杨景云')
# 占位符一般只能被被同类型替换，或者替换类型能被转换成占位符类型
print("I love %s" % 100)

s = "I'm %d years old";
print(s % 17)
# print(s%'Alice') ×

s = 'I am %.2fkKG, and %.2fm Height'
print(s % (55.4, 1.80))

print("*******************************************************")

# format格式化
# 使用函数形式进行格式化，代替以前的百分号
# 不指定位置，按顺序读取
s = '{} {}!'
print(s.format("hello", "world"))

s = '{} {}!'.format("hello", "world")
print(s)

# 设置指定位置
s = '{1} {0}!'.format("hello", "world")
print(s)
s = '{1} {1}!'.format("world", "world")
print(s)

#使用命名参数
s = "我们是{school_name}, 我们的网址是{url}, {teacher}最帅"
print(s.format(school_name='清华大学', url="www.baidu.com", teacher='liucanlie'))

# 通过字典设置参数需要解包
# 使用命名参数
s = "我们是{school_name}, 我们的网址是{url}, {teacher}最帅"
s_dict = {"school_name": "清华大学", \
          "url":"www.baidu.com", \
          "teacher":"liucanlie"}
# **是解包操作
print(s.format(**s_dict))

# 对数字格式化需要用到
s = "Alice is {:.2f}m height, {:.2f}kg weight. "
print(s.format(165.2, 45.124))

# str内置函数
s = "hello, world!"
help(str)