

class Fib2(object):
    def fibonacci(self, n):
        L = []
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
            L.append(a)
        return L

f = Fib2().fibonacci(10)
print(f)
print(f[5])


# Fib实例虽然能作用于for循环，看起来和list有点像，
# 但是，把它当成list来使用还是不行，比如，取第5个元素：
# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：

class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
f = Fib()
print(f[5])


class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start  # 这里是n.start  并不是 slice.start
            stop = n.stop  # # 这里是n.stop  并不是 slice.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:  # 注意这两
                    L.append(a)
                a, b = b, a + b  # 句代码的顺序
            return L

# f = Fib().fibonacci('这里要钉死一个参数')
f = Fib()
print(f[4:10])


"""
正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。比如定义Student类：
调用name属性，没问题，但是，调用不存在的score属性，就有问题了：
错误信息很清楚地告诉我们，没有找到score这个attribute。
要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，
那就是写一个__getattr__()方法，动态返回一个属性。修改如下：
"""

class Student(object):

    def __init__(self):
        self.name = "jack"

    def __getattr__(self, item):
        if item == 'score':
            return 99

# 当调用不存在的属性时，比如score，Python解释器会试图
# 调用__getattr__(self, 'score')来尝试获得属性，这样，我们就有机会返回score的值：
s = Student()
print(s.name, s.score)

"""注意，只有在没有找到属性的情况下，才调用__getattr__，
已有的属性，比如name，不会在__getattr__中查找。"""

