import datetime


# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
def now():
    print(datetime.date.today())
# 不是这样 f = now()
f = now
f()

# 函数对象有一个__name__属性，可以拿到函数的名字：
print(now.__name__)  # now
print(f.__name__)  # now

"""
现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，
但又不希望修改now()函数的定义，这种在代码运行期间 动态增加功能的方式，
称之为“装饰器”（Decorator）。
"""


def log(func):
    def wrapper(*args, **kw):
        print("call %s():" % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print(datetime.date.today())

# 把@log放到now()函数的定义处，相当于执行了语句：
# now = log(now)

print("-" * 50)
now()



def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print("%s %s(): " % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log("execute")
def now():
    print(datetime.date.today())

# 上边@log("execute") 相当于 now = log('execute')(now)
# 我们来剖析上面的语句，首先执行log('execute')，返回的是decorator函数，
# 再调用返回的函数，参数是now函数，返回值最终是wrapper函数。
print("-" * 50)
now()

print(now.__name__)  # wrapper
# 后边会讲@functools.wraps




# 练习：请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
def metric(fn):
    def wrapper(*args, **kw):
        print('%s executed in %s ms' % (fn.__name__, 10.24))
        return fn(*args, **kw)
    return wrapper

@metric
def now():
    print(datetime.date.today())

now()