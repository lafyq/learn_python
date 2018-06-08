# import os
#
# print('Process (%s) start...' % os.getpid())
#
# pid = os.fork()
#
# if pid == 0:
#     print('I am child process (%s) and my parent is %s' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s)' % (os.getpid(), pid))

print()
"""
上面代码无法再window下运行（Windows没有fork调用），贴出结果：
Process (876) start...
I (876) just created a child process (877).
I am child process (877) and my parent is 876.
"""


"""
由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。
multiprocessing模块就是跨平台版本的多进程模块。

multiprocessing模块提供了一个Process类来代表一个进程对象，
下面的例子演示了启动一个子进程并等待其结束：
"""
from multiprocessing import Process
import os

# 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()  # 启动子进程
#     p.join()  # 将子进程join，(即意味着要等待子进程运行结束后才能继续往下执行)
#     print('Child process end')


"""
Pool
如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
"""
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i, ))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')



print('*' * 80)

