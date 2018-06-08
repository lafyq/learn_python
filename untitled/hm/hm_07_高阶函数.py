from functools import reduce


def add(a, b, f):
    print(eval("a %s b" % f))

print(add(6, 2, '**'))

print(eval("1 + 1"))


"""
map()函数接收两个参数，一个是函数，一个是Iterable，
map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
"""
# 举例说明，比如我们有一个函数f(x)=x2，要把这个函数作用在一个list
# [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下：
def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(r)  这样并不能输出r，因为返回的Iterator是惰性序列
# 惰性序列只能通过next()获取下一个值 blabla...
# 所以我们将Iterator转换成list后再print一下就不用循环那么麻烦
print(list(r))


"""
再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
这个函数必须接收 两个 参数，
reduce把'结果'(已经function过的)继续和序列的下一个元素(未function过的)做累积计算
"""

# 比方说对一个序列求和，就可以用reduce实现：
def add(x, y):
    return x + y

r = reduce(add, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(r)

# 但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579
def fn(x, y):
    return x * 10 + y

r = reduce(fn, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(r)

# 对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数：
def fn(x, y):
    return x * 10 + y

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

r = reduce(fn, map(char2num, '13579'))
print(r)



# 练习：利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

def normalize(name):
    return name[0].upper() + name[1:].lower()

r = map(normalize, ['adam', 'LISA', 'barT'])
print(list(r))

# Python提供的sum()函数可以接受一个list并求和，
# 请编写一个prod()函数，可以接受一个list并利用reduce()求积：
# 学到lambda表达式再回来做

def prod(L):
    # 学到lambda表达式再回来做
    return reduce(lambda x, y: x * y, L)
print("*" * 4)
print(prod([1,2,3,4]))
# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

def str2float(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

def fn(x, y):
    return x * 10 + y


def damand(s):
    i = s.index(".")
    s1 = s[:i]
    s2 = s[i+1:]
    print(s1, s2)
    r = reduce(fn, map(str2float, s1)) + reduce(fn, map(str2float, s2)) * (0.1 ** len(s2))
    return r

print(damand('123.456'))
