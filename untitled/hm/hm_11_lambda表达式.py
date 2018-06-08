"""
关键字lambda表示匿名函数，冒号前面的x表示函数参数。
匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果
匿名函数lambda x: x * x实际上就是
    def f(x):
        return x * x
"""

L = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(L)  # [1, 4, 9, 16, 25, 36, 49, 64, 81]

# 此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
f = lambda x: x * x
print(f(5))  # 25

L = list(filter(lambda x: x % 2 == 0, range(1, 20)))
print(L)