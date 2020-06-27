from math import hypot

class Vector():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    '''
    把一个对象用字符串的形式表达出来得以辨认，如果没有实现__repr__()方法的话
    打印出来的就是内存地址，类似这样    <Vector object at 0x10e100070>
    __repr__和__str__的区别在于，后者是在str()函数被使用，或是在print函数打
    印一个对象的时候才能被调用，并且它返回的字符串对终端用户更加友好，如果一
    个对象没有实现__str__函数，那么Python在需要调用它的时候，解释器会用
    __repr__代替
    '''
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    '''
    如果没有对类实现这个方法，那么为了判断一个值x是真还是假，python会尝试调用
    __len__()方法。若返回为0，那么bool返回False,其他情况返回True
    '''
    def __bool__(self):
        # return bool(abs(self))
        return bool(self.x or self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scanlar):
        return Vector(self.x * scanlar, self.y * scanlar)

print("-------------------special method-------------------")
v1 = Vector(2, 4)
v2 = Vector(2, 1)
v3 = v1 + v2
print(v3)

v4 = v3 * 3
print(v4)

print(abs(v4))

print(bool(v4))