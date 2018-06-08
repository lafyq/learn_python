print()
"""
如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，
比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，
可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。
JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。

JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：
{} -- dict
[] -- list
"string" -- str
1234.56 -- int或float
true/false -- True/False
null -- None

Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。
我们先看看如何把Python对象变成一个JSON：
"""
import json
d = dict(name='Bob', age=20, score=88)
temp = json.dumps(d)
print(temp)  # {"name": "Bob", "age": 20, "score": 88}

# dumps()方法返回一个str，内容就是标准的JSON。
# 类似的，dump()方法可以直接把JSON写入一个file-like Object。
# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，
# 前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
temp = json.loads(json_str)
print(temp)

"""由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str与JSON的字符串之间转换。"""

"""
JSON进阶
Python的dict对象可以直接序列化为JSON的{}，
不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化：
"""
import _json
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
# print(json.dumps(s))  # TypeError: Object of type 'Student' is not JSON serializable

"""
前面的代码之所以无法把Student类实例序列化为JSON，
是因为默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象。

可选参数default就是把任意一个对象变成一个可序列为JSON的对象，
我们只需要为Student专门写一个转换函数，再把函数传进去即可：
"""
def student2dict(std):
    return {'name': std.name, 'age': std.age, 'score': std.score}

# 看下面这一句话很重要：
"""这样，Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON："""

print(json.dumps(s, default=student2dict))

"""
不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。
我们可以偷个懒，把任意class的实例变为dict：

因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。
(也有少数例外，比如定义了__slots__的class。)
"""

print(json.dumps(s, default=lambda obj: obj.__dict__))


"""
同样的道理，如果我们要把JSON反序列化为一个Student对象实例，
loads()方法首先转换出一个dict对象，
然后，我们传入的object_hook函数负责把dict转换为Student实例：
"""
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

# 运行结果如下：
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
s = json.loads(json_str, object_hook=dict2student)
print(s)
print(s.name, s.age, s.score)
