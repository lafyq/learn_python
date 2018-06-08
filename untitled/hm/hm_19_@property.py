print()

"""
在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，
但是，没办法检查参数，导致可以把成绩随便改.
这显然不合逻辑。为了限制score的范围，
可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，
这样，在set_score()方法里，就可以检查参数：
"""
class Student(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


"""但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单
** Python内置的@property装饰器就是负责把一个方法变成属性调用的：
"""

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

"""
@property的实现比较复杂，我们先考察如何使用。
把一个getter方法变成属性，只需要加上@property就可以了，
此时，@property本身又创建了另一个装饰器@score.setter，
负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：
"""
s = Student()
s.score = 60  # 实际转化为s.set_score(60)
"""注意赋值是 s.score = 60 而不是 s.score(60)、s.set_score(60)"""
print(s.score)  # 实际转化为s.get_score()

# s.score = 101  # 输入一个错误的分数会被验证条件拦截并抛出异常

"""  还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：  """

"""  小结
@property广泛应用在类的定义中，可以让调用者写出简短的代码，
同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。
"""


# 练习：请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise ValueError("width must be an integer!")
        if width < 0:
            raise ValueError("width must > 0 !")
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise ValueError("height must be an integer")
        if height < 0:
            raise ValueError("height must > 0 !")
        self._height = height

    @property
    def resolution(self):
        return self._width * self._height

