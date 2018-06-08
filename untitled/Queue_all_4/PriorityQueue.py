from queue import PriorityQueue  # 优先队列

priorityQueue = PriorityQueue()  # 创建优先队列对象
priorityQueue.put(3)  # 插入元素
priorityQueue.put(78)  # 插入元素
priorityQueue.put(100)  # 插入元素
print(priorityQueue.queue)  # 查看优先级队列中的所有元素
priorityQueue.put(1)  # 插入元素
priorityQueue.put(2)  # 插入元素
print('优先级队列:', priorityQueue.queue)  # 查看优先级队列中的所有元素
priorityQueue.get()  # 返回并删除优先级最低的元素
print('删除后剩余元素', priorityQueue.queue)
priorityQueue.get()  # 返回并删除优先级最低的元素
print('删除后剩余元素', priorityQueue.queue)  # 删除后剩余元素
priorityQueue.get()  # 返回并删除优先级最低的元素
print('删除后剩余元素', priorityQueue.queue)  # 删除后剩余元素
priorityQueue.get()  # 返回并删除优先级最低的元素
print('删除后剩余元素', priorityQueue.queue)  # 删除后剩余元素
priorityQueue.get()  # 返回并删除优先级最低的元素
print('全部被删除后:', priorityQueue.queue)  # 查看优先级队列中的所有元素
