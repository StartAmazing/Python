# str 内置函数


# 字符串的查找
str = "hello, java, python and Scala"
print(str.find("Scala"))
# print(str.index("C++")) # value error
print(help(str.find))

# 判断类函数
print(str.islower())
# 判断是否全部是字母或汉字字符
print(str.isalpha())
print("Linus".isalpha())
print("你好".isalpha())

print( "-----------------------isdigit, isnumeric, isdecimal三个判断数字的函数（不建议使用，尽量使用正则表达式）--------------------")
# 总结
'''
    isdigit: Unicode数字，byte数字(单字节)，全角数字(双字节)
    False： 汉字数字
    Error： 无
'''
print("3".isdigit())
print("".isdigit())
print("三".isdigit())

'''
    isdecimal()
    True： Unicode数字，全角数字(双字节)
    False： 罗马数字，汉字数字
    Error：byte数字(单字节)
'''

'''
    isnumeric()
    True： Unicode数字，全角数字（双字节），罗马数字，汉字数字
    False：无
    Error：byte数字（单字节）
'''
print("三".isnumeric()) # true

# 内容判断类
print("-----------------------               内容判断类             --------------------")
# startwith / endwith: 是否以xxx开头或者结尾
print(help(str.startswith))
print("Alice".startswith("alic"))

# 操作类函数
print("-----------------------               操作类函数             --------------------")
# format格式化的
# strip: 这个函数主要作用是删除字符串两边的空格，其实这个函数允许你去定义删除字符串两边的哪个
# 字符，只不过如果不指定的话默认是空格。同样还有lstrip和rstrip,此处l和r分别表示左边右边，即删
# 除字符串左边或者右边指定的字符，默认空格。需要注意的是，此处的删除不是删除哪个一个，而是从头
# 开始符合条件的连续字符

c = "LLLLLLL love xiaojingyu       "
print(c)
print(c.strip())

# join函数，我们使用s1， s2， s3作为分隔符，把ss内的内容拼接在一起
print("------------------  join函数  ----------------")
s1 = "$"
s2 = "-"
s3 = " "
ss = ["Alice Smith", "Donald Knuth", "Krict Annie"]
print(s1.join(ss))
print(s2.join(ss))
print(s3.join(ss))