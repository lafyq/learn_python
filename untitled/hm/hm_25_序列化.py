print()
"""
在程序运行的过程中，所有的变量都是在内存中,
我们把变量从内存中变成可存储或传输的过程称之为 序列化
在Python中叫pickling，在其他语言中也被称之为serialization...都是同一个意思

序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。

反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

Python提供了pickle模块来实现序列化。
"""

import pickle
d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)
# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
# 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
f = open('D:/test.txt', 'wb')
pickle.dump(d, f)
f.close()

# 看看写入的dump.txt文件，一堆乱七八糟的内容，这些都是Python保存的对象内部信息。
"""
当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，
然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法
从一个file-like Object中直接反序列化出对象。

我们打开另一个Python命令行来反序列化刚才保存的对象：
"""
f = open('D:/test.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)

"""
简而言之：对象-->序列化-->东东西西-->反序列化-->对象
下一课的 JSON 才是重点
"""