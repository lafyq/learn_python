from queue import LifoQueue  # LIFO队列

lifoQueue = LifoQueue()
lifoQueue.put(1)
lifoQueue.put(2)
lifoQueue.put(3)
print('LIFO队列', lifoQueue.queue)
lifoQueue.get()  # 返回并删除队列尾部元素
lifoQueue.get()
print(lifoQueue.queue)
