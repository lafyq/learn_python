# 闭包：我的理解就是返回一个函数（Closure）
# 并且相关参数和变量都保存在返回的函数中

# 通常情况下，定义一个求和函数
def calc_sum(*args):
    ax = 0
    for i in args[0]:
        # 注意args表示传入多个列表/元组，所以要用args[0]表示传入的第一个
        # 如果直接写args是会报错的
        # TypeError: unsupported operand type(s) for +: 'int' and 'list'
        ax = ax + i
    return ax
L = [1, 2, 3, 4, 5]
sum = calc_sum(L)
print(sum)


# 但是，如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？
# 可以不返回求和的结果，而是返回求和的 函数：
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args[0]:
            ax = ax + n
        return ax
    return sum
# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
L = [1, 2, 3, 4, 5]
f = lazy_sum(L)
print(f)  # <function lazy_sum.<locals>.sum at 0x000000DDE6D722F0>
# 调用函数f时，才真正计算求和的结果：
print(f())  # 15

"""
在这个例子中，我们在函数lazy_sum中又定义了函数sum，
并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，
这种称为“闭包（Closure）”的程序结构拥有极大的威力。
"""



"""
# 请再注意一点，当我们调用lazy_sum()时，
# 每次调用都会返回一个新的函数，即使传入相同的参数：
>>> f1 = lazy_sum(1, 3, 5, 7, 9)
>>> f2 = lazy_sum(1, 3, 5, 7, 9)
>>> f1==f2
False
# f1()和f2()的调用结果互不影响。
"""

# 另一个需要注意的问题是，
# 返回的函数并没有立刻执行，而是直到调用了f()才执行。
# 我们来看一个例子：
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()
# 上面的例子中，每次循环，都创建了一个新的函数，
# 然后，把创建的3个函数都返回了。fs[]里边存的是返回的那3个函数

# 你可能认为调用f1()，f2()和f3()结果应该是1，4，9，但实际是：
print(f1())  # 9
print(f2())  # 9
print(f3())  # 9
"""
全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。
等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9
# 返回闭包时牢记一点：
****** 返回函数不要引用任何循环变量，或者后续会发生变化的变量。
"""

# 如果一定要引用循环变量怎么办？
# 方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count():
    def f(j):
        def g():
            return j*j
        return g  # 这里要返回函数g()啊
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count()
print(f1())  # 1
print(f2())  # 4
print(f3())  # 9

"""                   容我做一下总结：返回函数 --> 返回未执行的函数（包括数据）的引用            """


def createCounter():
    def f():
        n = 0
        while True:
            n = n + 1
            yield n
    it = f()
    print(len(it))
    def counter():
        return next(it)
    return counter

f = createCounter()
print(f())
print(f())
print(f())
