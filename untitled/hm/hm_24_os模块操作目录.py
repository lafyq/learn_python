print()

import os
print(os.name)  # 操作系统类型
# 如果是posix，说明系统是Linux、Unix或Mac OS X，
# 如果是nt，就是Windows系统。

# 其实可以用：print(os.uname()) 来显示更完整的信息的
# 注意uname()函数在Windows上不提供，也就是说，
# os模块的某些函数是跟操作系统相关的。

"""
...因为os模块的某些函数是跟操作系统相关的，所以在这里演示不了

不过下边的内容也记一下吧！！！
"""

# 最后看看如何利用Python的特性来过滤文件。
# 比如我们要列出当前目录下的所有目录，只需要一行代码：
print([x for x in os.listdir('.') if os.path.isdir(x)])

# 要列出所有的.py文件，也只需一行代码：
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])


# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，
# 并打印出相对路径。

"""有个补充：os 和 os.path，os模块包括os.path，但是里边的方法有所不同的针对性
            os主要是执行一些动作（比如说，列出某个目录下的所有文件）
            os.path主要做一些判断（比如说判断当前目录下的这个东西是不是一个文件）"""
def search(d, t):
    for file in os.listdir(d):  # 遍历该目录下的所有东西
        if os.path.isfile(d + '/' + file):  # 如果这是一个文件
            if t in file:  # 如果file包含内容 t
                print(file, '-->', d + '/' + file)  # 输出文件名，并打印相对路径
        else:
            # 如果不是文件，那么就是目录啦，就对这个目录递归调用search
            search(d + '/' + file, t)

if __name__ == "__main__":
    search(os.path.abspath('.'), 'xml')