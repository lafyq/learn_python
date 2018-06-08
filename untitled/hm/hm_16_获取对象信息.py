# 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()

print(hasattr(obj, 'x'))  # 有属性'x'吗？
print(hasattr(obj, 'y'))  # 有属性'y'吗？
print(setattr(obj, 'y', 19))  # 设置一个属性'y'
print(hasattr(obj, 'y'))  # 有属性'y'吗？
print(getattr(obj, 'y'))  # 获取属性'y'
print(obj.y)  # 获取属性'y'

# 如果试图获取不存在的属性，会抛出AttributeError的错误：

"""
也可以获得对象的方法：

>>> hasattr(obj, 'power') # 有属性'power'吗？
True
>>> getattr(obj, 'power') # 获取属性'power'
<bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
>>> fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
>>> fn # fn指向obj.power
<bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
>>> fn() # 调用fn()与调用obj.power()是一样的
81
"""

"""
如果能写 sum = obj.x + obj.y
就不要写 sum = getattr(obj, 'x') + getattr(obj, 'y')  这么复杂

一个正确的用法的例子如下：
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
假设我们希望从文件流fp中读取图像，
我们首先要判断该fp对象是否存在read方法，
如果存在，则该对象是一个流，如果不存在，则无法读取。
hasattr()就派上了用场。
"""



