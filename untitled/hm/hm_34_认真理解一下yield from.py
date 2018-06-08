print()

"""
官方解释：

Python3.3版本的PEP 380中添加了yield from语法，允许一个generator生成器将其部分操作委派给另一个生成器。
其产生的主要动力在于使生成器能够很容易分为多个拥有send和throw方法的子生成器，像一个大函数可以分为多个子函数一样简单。
Python的生成器是协程coroutine的一种形式，但它的局限性在于只能向它的直接调用者yield值。
这意味着那些包含yield的代码不能像其他代码那样被分离出来放到一个单独的函数中。这也正是yield from要解决的。

虽然yield from主要设计用来向子生成器委派操作任务，但yield from可以向任意的迭代器委派操作；
对于简单的迭代器，yield from iterable本质上等于for item in iterable: yield item的缩写版，如下所示：
"""


def g(x):
    yield from range(x)


print(list(g(5)))


# 相当于
def g2(x):
    for item in range(x):
        yield item


print(list(g2(5)))

print('-' * 50)

"""
然而，不同于普通的循环，yield from允许子生成器直接从调用者接收其发送的信息或者抛出调用时遇到的异常，
并且返回给委派生产器一个值，如下所示：
"""


def accumulate():  # 子生成器(也可以指：迭代器)
    tally = 0
    while True:
        n = yield
        if n is None:
            return tally
        tally += n


def gather_tallies(tallies):  # 委派生成器（外部生成器），将累加操作任务委托给子生成器
    while True:
        tally = yield from accumulate()
        tallies.append(tally)


tallies = []

acc = gather_tallies(tallies)  # 简单理解就是创建委派生成器的对象
# （更详细的理解在generator生成器无bug.py）

next(acc)  # 使累加生成器准备好接受值
""" next(generator) 相当于 send(None), 启动生成器 """

for i in range(4):
    acc.send(i)  # 重头戏在这里！！！

acc.send(None)  # 结束第一次累加

"""
任何使用send()方法发给委派生产器（即外部生产器）的值被直接传递给迭代器。
    ** 如果send值是None，则调用子生成器的 next()方法；
    ** 如果不为None，则调用子生成器的 send()方法。"""

"""
    所以上面gather_tallies方法的执行流程如下：
        1、线程执行到 yield from accumulate()  阻塞，等待yield执行完成
            （即调用accumulate() 并且等到子生成器抛出StopIteration 或者 子生成器return）
        2、for循环执行，send 一个值给委派生成器gather_tallies, 他就直接将send来
            的东西send给子生成器accumulate

        3、子生成器accumulate执行，yield 返回一个 None，
        4、for循环继续执行，send一个值给委派生成器gather_tallies, 他就直接将send来
            的东西send给子生成器accumulate
        5、子生成器接收到一个值 n, 然后就从上次yield的地方继续执行
        ......反复 3—5 步
        6、直到子生成器accumulate抛出StopIteration 或者 子生成器return

"""

for i in range(5):
    acc.send(i)

acc.send(None)  # 结束第二次累加

print(tallies)




"""
总结如下： (最好看例子我的那个总结)
1. 迭代器（即可指子生成器）产生的值直接返还给调用者
2. 任何使用send()方法发给委派生产器（即外部生产器）的值被直接传递给迭代器。
    如果send值是None，则调用迭代器next()方法；如果不为None，则调用迭代器的send()方法。
    如果对迭代器的调用产生StopIteration异常，委派生产器恢复继续执行yield from后面的语句；
    若迭代器产生其他任何异常，则都传递给委派生产器。
3. 除了GeneratorExit 异常外的其他抛给委派生产器的异常，将会被传递到迭代器的throw()方法。
    如果迭代器throw()调用产生了StopIteration异常，委派生产器恢复并继续执行，其他异常则传递给委派生产器。
4. 如果GeneratorExit异常被抛给委派生产器，或者委派生产器的close()方法被调用，
    如果迭代器有close()的话也将被调用。如果close()调用产生异常，异常将传递给委派生产器。
    否则，委派生产器将抛出GeneratorExit 异常。
5. 当迭代器结束并抛出异常时，yield from表达式的值是其StopIteration 异常中的第一个参数。
6. 一个生成器中的return expr语句将会从生成器退出并抛出 StopIteration(expr)异常。

"""


# .......

# yield from 主要有什么用？
# yield from 主要有什么用？
# yield from 主要有什么用？

""" 1. 利用yield from从生成器读取数据 """
def reader():
    # 模拟从文件读取数据的生成器
    for i in range(4):
        yield '<< %s' % i

def reader_wrapper(g):
    # 循环迭代从reader产生的数据
    for v in g:
        yield v
"""
#我们可以用yield from语句替代reader_wrapper(g)函数中的循环，如下：
def reader_wrapper(g):
    yield from g
"""
wrap = reader_wrapper(reader())
for i in wrap:
    print(i)


""" 2.利用yield from语句向生成器（协程）传送数据  """

def writer():
    # 读取send传进的数据，并模拟写进套接字或文件
    while True:
        w = (yield )
        print('>> ', w)





