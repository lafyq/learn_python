import asyncio


"""
asyncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持。

asyncio的编程模型就是一个消息循环。我们从asyncio模块中直接获取一个EventLoop的引用，
然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。
"""


@asyncio.coroutine
def hello():
    print('Hello World!')
    # 异步调用asyncio.sleep(1)
    r = yield from asyncio.sleep(1)
    print("Hello again!")

# 获取EventLoop:
# loop = asyncio.get_event_loop()

"""
@asyncio.coroutine把一个generator标记为coroutine类型，
然后，我们就把这个coroutine扔到EventLoop中执行。
"""

# 执行coroutine
# loop.run_until_complete(hello())
# loop.close()

"""
hello()会首先打印出Hello world!，然后，yield from语法可以让我们方便地调用另一个generator。
由于asyncio.sleep()也是一个coroutine，所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环。
当asyncio.sleep()返回时，线程就可以从yield from拿到返回值（此处是None），然后接着执行下一行语句。

把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，
而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。
"""

import threading
import asyncio

@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread)
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread)

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

"""
观察执行过程：
Hello world! (<_MainThread(MainThread, started 140735195337472)>)
Hello world! (<_MainThread(MainThread, started 140735195337472)>)
(暂停约1秒)
Hello again! (<_MainThread(MainThread, started 140735195337472)>)
Hello again! (<_MainThread(MainThread, started 140735195337472)>)

由打印的当前线程名称可以看出，两个coroutine是由同一个线程并发执行的。

也就是说：线程去执行coroutine --> 碰到阻塞 --> 让他塞着，去轮询下一个coroutine

"""

#
#
# print('-' * 50)
#
# import threading
# import asyncio
#
# @asyncio.coroutine  # 用来标识这个函数是一个协程对象
# def hello():
#     for i in range(1, 5):
#         for j in range(1, 5):
#             # print('Hello world ! (%s)(%s)' % (i, j))
#             # print('Hello python ! (%s)(%s)' % (i, j))
#             # yield from asyncio.sleep(1)
#             # print('Hello world hi ! (%s)(%s)' % (i, j))
#             # print('Hello python hi ! (%s)(%s)' % (i, j))
#             pass
#
# # loop = asyncio.get_event_loop()  # 创建一个eventloop
# #
# # tasks = [hello(), hello()]
# #
# # loop.run_until_complete(asyncio.wait(tasks))  # 将协程加入到eventloop
# #
# # loop.close()
#
# def hello2():
#     pass
#
# hello2()
#
#
# def a():
#     for i in range(1, 10):
#         # print('i am a()! (%s)' % (i,))
#         yield i
#         # print('i am a() hi ! (%s)' % (i, ))
#
# for i in a():
#     pass
#
# """
# @asyncio.coroutine 把一个generator标记为coroutine类型，
# 然后，我们就把这个coroutine扔到EventLoop中执行。
# """
#
#
# """
# 我们用asyncio的异步网络连接来获取sina、sohu和163的网站首页：
# """
#
# import asyncio
#
# @asyncio.coroutine
# def wget(host):
#     print('wget %s ...' % host)
#     connect = asyncio.open_connection(host, 80)
#     reader, writer = yield from connect
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#
#         print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
#
#     writer.close()
#
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()