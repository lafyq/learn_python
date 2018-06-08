print()

"""
None 和 空字符串('') 的区别

区别：
None是一个空的对象，代表什么都没有。
而''，是一个字符串对象，代表一个空的字符串。

有一个需要注意的点：''空字符串 和 ' '空格字符串是两个完全不同的概念！！！
"""

a='abc'
b= None
# print(a + b)  # 会报错TypeError: must be str, not NoneType
#  因为，NoneType不允许和str进行+连接

a='abc'
b= ''
print(a + b, len(a+b))  # abc 3

