"""
Python内建的filter()函数用于过滤序列。

和map()类似，filter()也接收一个函数和一个序列。
 和map()不同的是，filter()把传入的函数依次作用于每个元素，
 然后根据返回值是True还是False决定保留还是丢弃该元素。

"""
# print(2 % 5)  # 2
# print(3 % 5)  # 3

# 筛选出一个列表中的所有奇数（删除偶数，保留奇数）
def is_odd(n):
    return n % 2 == 1
    # flag = n % 2 == 1
    # print(flag, end='\t')
    # return flag


res = list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(res)

# 把一个列表中的空字符串删掉
def not_empty(s):
    return s and s.strip()



"""
短路求值是现代编程语言里通用的逻辑运算符求值策略。

Python 里
s and s.strip()

# 等同于
s.strip() if s else s
return s and s.strip()

# 就等同于
if s:  # 如果s有值并且不为None
　　 return s.strip()
else:
　　 return s


# a = ''  或者  a = None  只有这两种情况才会输出false (注意''并不等于' ')

if a:
    print('true')
else:
    print('false')

"""


res = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
print(res)
"""
# 简单描述一下上面代码的执行流程：   ----其实就是构造一个generator, 然后往里边丢 函数 和 变量

# 其实也就相当于下面这段代码
L = ['A', '', 'B', None, 'C', '  ']
def running(L):
    def not_empty(s):
        return s and s.strip()
    for i in L:
        if not_empty(i):
            yield i
        else:
            continue

print(list(running(L)))

# 第一步：构造一个generator， 把not_empty函数 和 ['A', '', 'B', None, 'C', '  ']变量 都丢进去
# 然后执行代码
#   注意：上面not_empty返回的是三种情况：(这里最好看回去上一个全文注释)
#       1.去掉两边空格后的s  2.空字符串''  3.None值  
#
# 第二步：根据第一步返回的结果（也就是经过not_empty函数处理过的元素）进行判断（True or False）是否要留下这个元素
#   也就是： 留下并返回 = (flag if not_empty返回的结果==True else False)   # 伪代码

# 第三步：
#   重复上面一二两步

# 其实可以更简单
# 这个理解的话就是：对经过lambda表达式的出来过的元素进行判断（上面的第二步）
# res = list(filter(lambda s: s and s.strip(), ['A', '', 'B', None, 'C', '  ']))



"""



print('-' * 50)

# 使用filter求素数（埃拉托色尼筛选法）
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0



"""
这里 return lambda x: x % n > 0 的含义
调用_not_divisible(n)时，返回的是另一个函数：
def fn(x):
    return x % n > 0  # 这里的n 就是调用 _not_divisible传进去的n

下面的primes中每次循环都会创建新的fn函数
"""

def primes():
    yield 2
    it = _odd_iter()  # 初始化一个generator
    while True:
        n = next(it)  # 返回generator的第一个对象
        yield n
        it = filter(_not_divisible(n), it)  # 构造generator


"""
简单描述一下上面primes的执行流程：  注意：primes是一个generator函数



"""

# 剧透lambda表达式用法
# a = lambda x: x * x
# print(a(2))


"""

# 调用下边的f先, 就算是不断的调用f


it = _odd_iter()

def temp_generator(it):
    
    lambda_list = [
        lambda x: x % 3 > 0,
        lambda x: x % 5 > 0,
        lambda x: x % 7 > 0,
        lambda x: x % 11 > 0,
        lambda x: x % 13 > 0  # ....不一一列举
    ]
    for a in it:  # 遍历it生成器
        
        flag = True
        
        for lam in lambda_list:
            if not lam(a):  # 看是否符合(只要有一个不符合直接 break)
                flag = False
                break
                
        if flag:
            list.append(lambda_func)  
            # 如果正在遍历的it里边的 a这个元素符合上面所有lambda表达式，就将这个lambda加入到lambda_list中

            lambda_func = yield a  # 暂停并返回 a
        
    print('.........')



def f(lambda_func):
    a = t.send(lambda_func)



"""


"""
# 因为为了完成_not_divisible的调用，n的值已经传进来了。
#据我理解，这个结果是
    ...filter((lambda x: x % 7 >0), filter((lambda x: x % 5 >0),
            filter((lambda x: x % 3 >0),  it)))
        # 其实就是不断地往it指向的那个generator里边丢算法（或者说是函数），
          只有都符合里边所有的算法，才yield返回到这里 去和这个filter里边的算法进行筛选
          （也就是说哦，假如it指向的那个generator会一直自己循环，直到都符合之前往里丢的算法（函数）
            也就是直到 能够返回序列的第一个对象（n = next(it)）
            才会yield暂停（不要用中断这个词）并返回 n，如果不符合是不会yield暂停并返回的）
            （by the way, 上面循环我们始终是在操作一个generator（也就是说一块内存），
              而这个generator里边每一次yield暂停并返回意味着generator方法的局部变量，
              指针信息，运行环境（也叫上下文） 都保存起来，直到下一次调用next方法恢复，
              注意，指针信息是被保存下来的，所以并不会出现从头再遍历一遍这个generator，
              也就是说下一次next是上一次next的相邻元素...差不多是这个意思吧！！）

              所以上面 n = next(it) 是获取刚刚加入到 it指向的generator中的元素


"""

        # 相当于下面这两句代码
        # fn = _not_divisible(n)
        # it = filter(fn, it)

        # 友情提示一下：
        # print(2 % 5)  # 2
        # print(3 % 5)  # 3


for i in primes():
    if i > 1000:
        break
    print(i, end=' ')




# 理解了上面的思路之后尝试自己写一遍
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisable(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        if n > 100:
            break
        yield n
        it = filter(_not_divisible(n), it)

print()
print('*' * 50)
for i in primes():
    print(i, end=' ')
