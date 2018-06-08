print()

"""
Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。

绝大多数情况下，我们只需要使用threading这个高级模块。

启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：
"""

import time, threading

# 新线程执行的代码：
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

"""
由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，
Python的threading模块有个current_thread()函数，它永远返回当前线程的实例。
主线程实例的名字叫MainThread，子线程的名字在创建时指定，我们用LoopThread命名子线程。
名字仅仅在打印时用来显示，完全没有其他意义，如果不起名字Python就自动给线程命名为Thread-1，Thread-2……
"""


import time, threading

# 假定这是你的银行存款:
balance = 0

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(1000000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)  # 竟然不是 0 ！！！

"""
我们定义了一个共享变量balance，初始值为0，并且启动两个线程，先存后取，
理论上结果应该为0，但是，由于线程的调度是由操作系统决定的，
当t1、t2交替执行时，只要循环次数足够多，balance的结果就不一定是0了。

原因是因为高级语言的一条语句在CPU执行时是若干条语句，即使一个简单的计算：
    balance = balance + n
也分两步：
    1、计算balance + n，存入临时变量中；
    2、将临时变量的值赋给balance。
也就是可以看成：
    x = balance + n
    balance = x

究其原因，是因为修改balance需要多条语句，而执行这几条语句时，
线程可能中断，从而导致多个线程把同一个对象的内容改乱了。

如果我们要确保balance计算正确，就要给change_it()上一把锁，
当某个线程开始执行change_it()时，我们说，该线程因为获得了锁，
因此其他线程不能同时执行change_it()，只能等待，
直到锁被释放后，获得该锁以后才能改。由于锁只有一个，无论多少线程，
同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突。
创建一个锁就是通过threading.Lock()来实现：

"""

import time, threading

# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()
def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(1000000):
        # 先获取锁
        lock.acquire()
        try:
            # 放心操作吧！！！
            change_it(n)
        finally:
            # 最后要释放锁
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)  # 终于是 0 了！！！

"""
当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，
然后继续执行代码，其他线程就继续等待直到获得锁为止。
获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。
所以我们用try...finally来确保锁一定会被释放。

锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行，
坏处当然也很多，
    1.首先是阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了。
    2.其次，由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，
         可能会造成死锁，导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止。
"""
