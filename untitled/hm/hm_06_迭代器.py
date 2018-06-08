# 小结
# 凡是可作用于for循环的对象都是Iterable类型；
#
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
#
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
#
# Python的for循环本质上就是通过不断调用next()函数实现的，例如：

# 具体可以看廖雪峰老师 迭代器教程
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143178254193589df9c612d2449618ea460e7a672a366000

# 以下这个for循环
for x in [1, 2, 3, 4, 5]:
    pass

# 完全等价于下面这段代码

# 1.首先获得Iterator对象
it = iter([1, 2, 3, 4, 5])

# 2.循环
while True:
    try:
        # 获得下一个值
        x = next(it)

    except StopIteration:
        # 遇到 StopIteration 就退出循环
        break
        