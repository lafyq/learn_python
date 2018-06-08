print()

'''
queue is especially useful in threaded programming
when information must be exchanged safely between multiple threads.

创建一个“队列”对象

import queue
q = queue.Queue(maxsize = 10)
queue.Queue类即是一个队列的同步实现。队列长度可为无限或者有限。可通过Queue的构造函数的可选参数
maxsize来设定队列长度。如果maxsize小于1就表示队列长度无限。

将一个值放入队列中
q.put(10)
调用队列对象的put()方法在队尾插入一个项目。
put()有两个参数，第一个item为必需的，为插入项目的值；第二个block为可选参数，默认为1。
如果队列当前为空且block为1，put()方法就使调用线程暂停,直到空出一个数据单元。
如果block为0，put方法将引发Full异常。

将一个值从队列中取出
q.get()
调用队列对象的get()方法从队头 删除并返回 一个项目。
可选参数为block，默认为True。如果队列为空且block为True，get()就使调用线程暂停，直至有项目可用。
如果队列为空且block为False，队列将引发Empty异常。

'''



'''
join() 阻塞进程，直到所有任务完成，需要配合另一个方法task_done。

    def join(self):
     with self.all_tasks_done:
      while self.unfinished_tasks:
       self.all_tasks_done.wait()

task_done() 表示某个任务完成。每一条get语句后需要一条task_done。


'''
import queue
q = queue.Queue(5)
q.put(10)
q.put(20)
print(q.get())
q.task_done()  # 注释掉本行，程序将不会结束。
print(q.get())
q.task_done()  # 注释掉本行，程序将不会结束。

q.join()

print("ending!")

"""注释掉上面那些task_done其中一个都不会运行到ending!
   也就是说不会出现 "Process finished with exit code 0"
"""
