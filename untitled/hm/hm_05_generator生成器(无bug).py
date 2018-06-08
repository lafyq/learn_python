print('-' * 50)
"""
对于普通的生成器，第一个next调用，相当于启动生成器，会从生成器函数的第一行代码开始执行，
直到第一次执行完yield语句（第4行）后，跳出生成器函数。

然后第二个next调用，进入生成器函数后，从yield语句的下一句语句（第5行）开始执行，
然后重新运行到yield语句，执行后，跳出生成器函数，

后面再次调用next，依次类推。下面是一个列子：
"""


def consumer():
    r = 'here'
    for i in range(3):
        yield r  # 我是第4行

        r = '200 ok ' + str(i)  # 我是第5行


c = consumer()  # 这里的意思是：在内存中开辟一个空间给这个生成器consumer
                # 并定义一个变量c去指向 生成器consumer的地址引用
                # 注意：仅仅是分配内存, 引用指向而已, 并没有启动生成器consumer


# 第一个next调用，相当于启动生成器，会从生成器函数的 第一行 代码开始执行
print(c.__next__())  # here

print(c.__next__())  # 200 ok 0
print(c.__next__())  # 200 ok 1

"""
了解了next()如何让包含yield的函数执行后，我们再来看另外一个非常重要的函数send(msg)。
其实next()和send()在一定意义上作用是相似的，
区别是send()可以传递yield表达式的值进去，而next()不能传递特定的值，只能传递None进去。
因此，我们可以看做c.next() 和 c.send(None) 作用是一样的。
需要提醒的是，第一次调用时，请使用next()语句或是send(None)，不能使用send发送一个非None的值，否则会出错的，
因为没有Python yield语句来接收这个值。

下面来着重说明下send执行的顺序。当第一次send（None）（对应11行）时，
启动生成器，从生成器函数的第一行代码开始执行，直到第一次执行完yield（对应第4行）后，跳出生成器函数。
这个过程中，n1一直没有定义。
下面运行到send（1）时，进入生成器函数，注意这里与调用next的不同。
这里是从第4行开始执行，把1赋值给n1，但是并不执行yield部分。
下面继续从yield的下一语句继续执行，然后重新运行到yield语句，执行后，跳出生成器函数。

即send和next相比，只是开始多了一次赋值的动作，其他运行流程是相同的。

"""

print("---" * 50)


def consumer():  # 有一个小坑：注意generator函数是没有 return 的
    r = 'here'
    while True:
        n1 = yield r  # 我是第4行
        if not n1:
            return
        print('[CONSUMER] Consuming %s...' % n1)
        r = '200 ok ' + str(n1)


def produce(c):
    c.send(None)  # 我是第11行
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r1 = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r1)
    c.close()


c = consumer()
produce(c)
