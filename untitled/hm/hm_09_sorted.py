
# Python内置的sorted()函数就可以对list进行排序：
print(sorted([36, 5, -12, 9, -21]))


# 此外，sorted()函数也是一个高阶函数，
# 它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
print(sorted([36, 5, -12, 9, -21], key = abs))

"""
对比原始的list和经过key=abs处理过的list：

sorted()函数按照keys进行排序，并按照对应关系返回list相应的元素：

keys排序结果 => [5, 9,  12,  21, 36]
                |  |    |    |   |
最终结果     => [5, 9, -12, -21, 36]
"""



# 我们再看一个字符串排序的例子：
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
# 对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'
# 我们可以用一个key函数把字符串映射为忽略大小写排序即可
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower))


# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
print(sorted(['bob', 'about', 'Zoo', 'Credit'],
             key = str.lower, reverse = True))

"""
从上述例子可以看出，高阶函数的抽象能力是非常强大的，
而且，核心代码可以保持得非常简洁。
"""

# 练习：假设我们用一组tuple表示学生名字和成绩：
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# 请用sorted()对上述列表分别按名字排序：
def by_name(t):
    return t[0].lower()
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L1 = sorted(L, key = by_name)
print(L1)

# 请用sorted()对上述列表分别按成绩从高到低排序：
def by_score(t):
    return t[1]
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L1 = sorted(L, key = by_score, reverse = True)
print(L1)
