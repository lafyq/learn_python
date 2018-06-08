"""
在Python中，只要是可迭代对象，无论有无下标，都可以迭代
那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的 Iterable类型判断：
# >>> from collections import Iterable
# >>> isinstance('abc', Iterable) # str是否可迭代
# True
# >>> isinstance([1,2,3], Iterable) # list是否可迭代
# True
# >>> isinstance(123, Iterable) # 整数是否可迭代
# False
"""
print("em....")
print("hello python!")

# 迭代一个str
print()
print("-" * 50)
print("尝试迭代一个str(字符串)：", end="\t")
for ch in "ABC":
    print(ch, end="\t")

# 迭代一个列表
print("")
print()
print("-" * 50)
print("尝试迭代一个list(列表)：", end="\t")
for i in [1, 2, 3]:
    print(i, end="\t")

# 如果要对list实现类似Java那样的下标循环怎么办？
# Python内置的enumerate函数可以把一个list变成索引-元素对，
# 这样就可以在for循环中同时迭代索引和元素本身：
print("")
print()
print("-" * 50)
print("尝试迭代一个list(列表)，并输出下标：", end="\t")
for i, value in enumerate(['A', 'B', 'C']):  # enumerate：[ɪˈnju:məreɪt] 枚举
    print(i, ":", value, end="\t")

# 迭代一个字典
print("")
print()
print("-" * 50)
print("尝试迭代一个dict(字典)：", end="\t")
for key, value in {'a': 1, 'b': 2, 'c': 3}.items():  # 注意这里有个items()
    print(key, ":", value, end="\t")

print("")
print()
print("-" * 50)
print("尝试迭代一个dict(字典)的key：", end="\t")
for key in {'a': 1, 'b': 2, 'c': 3}.keys():
    print(key, end="\t")

print("")
print()
print("-" * 50)
print("尝试迭代一个dict(字典)的value：", end="\t")
for value in {'a': 1, 'b': 2, 'c': 3}.values():
    print(value, end="\t")



print()
print()
print("-" * 50)
print("-" * 50)
# 查找一个list中的最大值和最小值
def findMinAndMax(L):
    if L != []:
        min_int = L[0]
        max_int = L[0]
        for i in L:
            if min_int > i:
                min_int = i
            if max_int < i:
                max_int = i
        return (min_int, max_int)
    else:
        return (None, None)

    # return (min(L), max(L))

print(findMinAndMax([1,2,3,4,5]))

