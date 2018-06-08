print()
"""
很多时候，数据读写不一定是文件，也可以在内存中读写。

StringIO顾名思义就是在内存中读写str。

要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：
"""
from io import StringIO

f = StringIO()

f.write('hello')
f.write(' ')
f.write('world!')

print(f.getvalue())  # getvalue()方法用于获得写入后的str。

"""
要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：
"""
from io import StringIO
f = StringIO('Hello!\nHi!\nGoodBye!')
while True:
    s = f.readline()
    if s == '':  # 这里补充一个知识点：None和空字符串的区别（见下一节）
        break
    print(s.strip())