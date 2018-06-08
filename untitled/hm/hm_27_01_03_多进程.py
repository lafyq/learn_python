from multiprocessing import Queue

print()
"""
Multiprocessing Lock
当多个进程需要访问共享资源的时候，Lock可以用来避免访问的冲突。
主要用到了lock.acquire() 和lock.release()
"""

import multiprocessing
import sys
import time

# def work_with(lock, file):
#     with lock:
#         fs = open(file, 'a+')
#         fs.write('Lock acquired via with\n')
#         fs.close()
#
# def work_no_with(lock, file):
#     lock.acquire()
#     try:
#         fs = open(file, 'a+')
#         fs.write('Lock acquired directly\n')
#         fs.close()
#     finally:
#         lock.release()
#
# if __name__ == '__main__':
#
#     file = 'D:/pro_test.txt'
#
#     lock = multiprocessing.Lock()
#
#     w = multiprocessing.Process(target=work_with, args=(lock, file))
#     nw = multiprocessing.Process(target=work_no_with, args=(lock, file))
#
#     w.start()
#     nw.start()
#
#     w.join()
#     nw.join()


# def work_with(lock, file):
#     with lock:
#         fs = open(file, 'a')
#         for i in range(5):
#             fs.write('Lock acquired via with --- (%s)\n' % (i, ))
#             print('Lock acquired via with')
#             time.sleep(0.2)
#         fs.close()
#
# def work_no_with(lock, file):
#     lock.acquire()
#     try:
#         fs = open(file, 'a')
#         for i in range(5):
#             fs.write('Lock acquired directly --- (%s)\n' % (i,))
#             print('Lock acquired directly')
#             time.sleep(3)
#         fs.close()
#     finally:
#         lock.release()
#
#
# if __name__ == '__main__':
#
#     file = 'D:/pro_test.txt'
#
#     lock = multiprocessing.Lock()
#
#     w = multiprocessing.Process(target=work_with, args=(lock, file))
#     nw = multiprocessing.Process(target=work_no_with, args=(lock, file))
#
#     w.start()
#     nw.start()
#
#     w.join()
#     nw.join()



"""
Multiprocessing Semaphore
Semaphore用来控制对共享资源的访问数量，例如池的最大连接数。
"""

# def worker(s, i):
#     s.acquire()
#     print(multiprocessing.current_process().name + ' acquire')
#     time.sleep(i)
#     print(multiprocessing.current_process().name + ' release')
#     s.release()
#
# if __name__ == '__main__':
#
#     s = multiprocessing.Semaphore(2)  # 控制进程池的最大连接数
#                                       # 也即是说，最多能同时acquire()两个，在没有release（）之前
#                                       # 其他进程不能被创建
#     for i in range(5):
#         p = multiprocessing.Process(target=worker, args=(s, i*5))
#         p.start()


"""
Multiprocessing Event
Event用来实现进程间同步通信。
"""

# def wait_for_event(e):
#     """Wait for the event to be set before doing anything"""
#     print("wait for event: starting ")
#     e.wait()
#     print('wait for event: e.is_set() --> ', str(e.is_set()))
#
# def wait_for_event_timeout(e, t):
#     """Wait t seconds and then timeout"""
#     print('wait_for_event_timeout: starting')
#     e.wait(t)
#     print('wait_for_event_timeout: e.is_set()->', str(e.is_set()))
#
# if __name__ == '__main__':
#     e = multiprocessing.Event()
#
#     w1 = multiprocessing.Process(name='block', target=wait_for_event, args=(e, ))
#     w1.start()
#
#     w2 = multiprocessing.Process(name='non-block', target=wait_for_event_timeout, args=(e, 2))
#
#     w2.start()
#
#     time.sleep(3)
#
#     e.set()  # 可以理解为唤醒
#     print('main event is set')

"""
event.is_set()：   返回event的状态值True或者False；

event.wait()：    如果 event.is_set()==False将阻塞线程；

event.set()：     设置event的状态值为True，所有阻塞池的线程激活进入就绪状态，等待操作系统调度；
"""



"""
Multiprocessing Queue and Pipe
Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
"""

from multiprocessing import Process, Queue
import random
# 写数据进程执行的代码
def write(q):
    for value in ['A', 'B', 'C']:
        print('put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    while True:
        value = q.get(True)
        print('Get %s from queue...' % value)

if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q, ))
    pr = Process(target=read, args=(q, ))

    pw.start()
    pr.start()

    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止
    pr.terminate()
