print()

"""
 管道（pipe）
The Pipe() function returns a pair of connection objects connected by
a pipe which by default is duplex (two-way).

pipe()函数返回由管道连接的 一对连接对象，该管道默认是双向的(双向的)。

For example:
"""

from multiprocessing import Process, Pipe

def child(conn):
    conn.send([12, {'name': 'yuan'}, 'hello'])
    response = conn.recv()
    print('child receive: ', response)
    conn.close()

if __name__ == '__main__':
    print('main start ...')

    parent_conn, child_conn = Pipe()  # 管道的一对（两个）对象

    p = Process(target=child, args=(child_conn, ))  # 创建进程
    p.start()  # 启动进程

    print('parent receive: ', parent_conn.recv())
    parent_conn.send('儿子你好！')
    p.join()

    print('\nmain end ...')


"""
Pipe（）返回的两个连接对象代表管道的两端。 每个连接对象都有send()和recv()方法（等等）。
 请注意，如果两个进程（或线程）尝试同时读取或写入管道的同一端，管道中的数据可能会损坏
"""