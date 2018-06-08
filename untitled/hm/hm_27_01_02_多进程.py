print()
"""
想要充分利用多核CPU资源，Python中大部分情况下都需要使用多进程，
Python中提供了multiprocessing这个包实现多进程。
multiprocessing支持子进程、进程间的同步与通信，提供了Process、Queue、Pipe、Lock等组件。
"""

"""
开辟子进程
multiprocessing中提供了Process类来生成进程实例

Process([group [, target [, name [, args [, kwargs]]]]])

group分组，实际上不使用
target表示调用对象，你可以传入方法的名字
args表示给调用对象以元组的形式提供参数，比如target是函数a，他有两个参数m，n，那么该参数为args=(m, n)即可
kwargs表示调用对象的字典
name是别名，相当于给这个进程取一个名字
"""

# 先来个小例子：
from multiprocessing import Process
import os
import time

# 子进程要执行的代码
# def run_proc(name):
#     i = 0
#     while i < 3:
#         print('Run child process %s (%s)...' % (name, os.getpid()))
#         time.sleep(2)
#         i = i + 1
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()  # 启动子进程
#     print('Child process end')

"""
根据运行结果可知，父进程运行结束后子进程仍然还在运行，这可能造成僵尸（ zombie）进程。

通常情况下，当子进程终结时，它会通知父进程，清空自己所占据的内存，并在内核里留下自己的退出信息。
父进程在得知子进程终结时，会从内核中取出子进程的退出信息。但是，如果父进程早于子进程终结，这可
能造成子进程的退出信息滞留在内核中，子进程成为僵尸（zombie）进程。当大量僵尸进程积累时，内存空间会被挤占。
"""

"""
有什么办法可以避免僵尸进程呢？
这里介绍进程的一个属性 deamon，当其值为TRUE时，其父进程结束，该进程也直接终止运行（即使还没运行完）。
所以给上面的程序加上p.deamon = true，看看效果。
"""

# 子进程要执行的代码
# def run_proc(name):
#     i = 0
#     while i < 3:
#         print('Run child process %s (%s)...' % (name, os.getpid()))
#         time.sleep(2)
#         i = i + 1
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     p.daemon = True  # 加入daemon (不要拼错了 daemon)
#     print('Child process will start.')
#     p.start()  # 启动子进程
#     print('Child process end')



"""
这是问题又来了，子进程并没有执行完，这不是所期望的结果。有没办法将子进程执行完后才让父进程结束呢？
这里引入p.join()方法，它使子进程执行结束后，父进程才执行之后的代码
"""
# 子进程要执行的代码
# def run_proc(name):
#     i = 0
#     while i < 3:
#         print('Run child process %s (%s)...' % (name, os.getpid()))
#         time.sleep(2)
#         i = i + 1
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     p.daemon = True  # 加入daemon (不要拼错了 daemon)
#     print('Child process will start.')
#     p.start()  # 启动子进程
#     p.join()   # 加入join方法
#     print('Child process end')


"""
将进程定义成类
通过继承Process类，来自定义进程类，实现run方法。实例p通过调用p.start()时自动调用run方法。
"""

# class MyProcess(Process):
#
#     def __init__(self, name):
#         Process.__init__(self)
#         self.name = name
#
#     def run(self):
#         i = 0
#         while i < 3:
#             print('Run child process %s (%s)...' % (self.name, os.getpid()))
#             time.sleep(2)
#             i = i + 1
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = MyProcess('test')
#     p.daemon = True  # 加入daemon (不要拼错了 daemon)
#     print('Child process will start.')
#     p.start()  # 启动子进程
#     p.join()   # 加入join方法
#     print('Child process end')



"""
创建多个进程
很多时候系统都需要创建多个进程以提高CPU的利用率，当数量较少时，可以手动生成一个个Process实例。
当进程数量很多时，或许可以利用循环，但是这需要程序员手动管理系统中并发进程的数量，有时会很麻烦。

这时进程池Pool就可以发挥其功效了。可以通过传递参数限制并发进程的数量，默认值为CPU的核数。
直接上例子：
"""

from multiprocessing import Process, Pool
import os, time

def run_proc(name):  # 定义一个函数用于进程调用
    for i in range(5):
        time.sleep(0.2)  # 休眠0.2秒
        print('Run child process %s (%s)' % (name, os.getpid()))
# 执行一次上面的这个run_proc函数总共用时需要 1秒的时间

if __name__ == '__main__':
    print('Run the main process (%s).' % (os.getpid()))
    mainStart = time.time()  # 记录主进程开始时间
    p = Pool(8)  # 开辟进程池 （如果注释掉这句，系统默认开辟四个 p = Pool(4) )
    for i in range(16):  # 开辟16个进程
        p.apply_async(run_proc, args=('Process' + str(i), ))  # 每个进程都调用了run_proc函数，
                                                              # args表示给该函数传递的参数。
    print('Waiting for all subprocesses done ...')
    p.close()
    p.join()  # 等待所有子进程执行完毕后，主进程才继续往下执行
    print('All subprocesses done')
    mainEnd = time.time()  # 记录主进程结束时间
    print('All process ran %0.2f seconds.' % (mainEnd-mainStart))  # 主进程执行时间


"""
这里进程池对并发进程的限制数量为8个，而程序运行时会产生16个进程，
进程池将自动管理系统内进程的并发数量，其余进程将会在队列中等待。
限制并发数量是因为，系统中并发的进程不是越多越好，并发进程太多，
可能使CPU大部分的时间用于进程调度，而不是执行有效的计算。

采用多进程并发技术时，就单个处理机而言，其对进程的执行是串行的。
但具体某个时刻哪个进程获得CPU资源而执行是不可预知的（如执行结果的开头部分，各进程的执行顺序不定），
这就体现了进程的异步性。

如果单个程序执行16次run_proc函数，那么它会需要至少16秒,通过进程的并发，这里只需要2.49秒，可见并发的优势。
"""
