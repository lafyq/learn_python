from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr',
                       'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '-->', member, ',', member.value)

# value属性则是自动赋给成员的int常量，默认从1开始计数。

# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
from enum import Enum, unique

# @unique装饰器可以帮助我们检查保证没有重复值。
@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

# 访问这些枚举类型可以有若干种方法：
day1 = Weekday.Mon
print(day1)  # Weekday.Mon
print(Weekday.Tue)  # Weekday.Tue
print(Weekday['Tue'])  # Weekday.Tue
print(Weekday.Mon.value)  # 1
print(day1 == Weekday.Mon)  # True


"""  练习不会做  """
#
# class Gender(Enum):
#     Male = 0
#     Female = 1
#
# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = None
#         if gender == Gender.Male:
#             print(self.gender == Gender.Male.value)
#         if gender == Gender.Female:
#             print(self.gender == Gender.Female.value)
#         # else:
#         #     raise ValueError("gender must be Male or Female ！")
#
#     def __str__(self):
#         print(self.name, self.gender)
#
# s = Student("niefeng", "Male")
# s.__str__()
# print('Male' == Gender.Male)