print("-" * 50)
"""
偏函数
阅读: 214533
Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）。
要注意，这里的偏函数和数学意义上的偏函数不一样。
在介绍函数参数的时候，我们讲到，通过设定参数的默认值，可以降低函数调用的难度。
而偏函数也可以做到这一点。举例如下：

"""

# int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：
"""注意：这里的按十进制转换指的是：传入的东西，按照十进制转换成int（十进制）类型"""
print(int('12345'))

# 但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换：
print(int('12345', base=8))
print(int('12345', 16))

"""
假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，
于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去：

"""
def int2(x, base=2):
    return int(x, base)

# 这样，我们转换二进制就非常方便了：
# print(int2('12345'))  # 错误做法
"""注意：这里的按二进制转换指的是：传入的东西，按照二进制转换成int（十进制）类型"""

print(int2('10010101'))

# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，
# 可以直接使用下面的代码创建一个新的函数int2：
import functools
int2_func = functools.partial(int, base=2)
print(int2_func('10010101'))

"""
创建偏函数时，实际上可以接收 函数对象、*args和**kw这3个参数
"""
print("*" * 50)
int2 = functools.partial(int, base=2)
print(int2('10010'))
# 相当于
kw = {'base': 2 }
print(int('10010', **kw))

print("*" * 50)
max2 = functools.partial(max, 10)
# 实际上会把10作为*args的一部分自动加到左边，也就是：
print(max2(5, 6, 7))
# 相当于
print(max(10, 5, 6, 7))

"""
小结
当函数的参数个数太多，需要简化时，使用functools.partial可以创建
一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
"""
