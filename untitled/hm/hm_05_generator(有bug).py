# import angel as angel
print()

def fib(max):
    n, a, b = 0, 1, 1  # n表示到第几天， a 表示第一天， b 表示第二天
    while n < max:
        print(a, end='\t')  # 输出第一天的数量（进入循环后表示输出第n天的数量）
        a, b = b, a + b
        n = n + 1
    return 'done'

print(fib(10))


# 传统求斐波那契数列方法
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

print("-" * 50)
def fibonacci2(n):
    a1 = 1
    a2 = 1
    i = 0
    while i < n:
        print(a1, end='\t')
        a1, a2 = a2, a1 + a2
        i += 1


print(fibonacci2(10))



# 使用generator生成器方式写斐波那契数列

def fibonacci3(n):
    a1 = 1
    a2 = 1
    i = 0
    while i < n:
        yield a1
        a1, a2 = a2, a1 + a2
        i += 1

it = fibonacci3(10)
for i in it:
    print(i, end='\t')

# print(next(it))  # 当已经调用完generator里边的东西的时候（即到了StopIteration）
                # 再次调用会报错 StopIteration

print()
print('--' * 30)






def triangel(n):
    L=[1]  #定义一个list[1]
    while True:
        yield L  #打印出该list

        L=[L[x]+L[x+1] for x in range(len(L)-1)]  #计算下一行中间的值（除去两边的1）
        # 上面计算第二行的时候有点难理解：L = []
        # 因为循环都已经是 for x in 0: 所以没有执行循环体内的东西，所以是空列表

        # 第三行： L = [2],  第四行： L = [3, 3],  第五行： L = [4, 6, 4], 以此类推...

        L.insert(0, 1)  #在开头插入1
        L.append(1)  #在结尾添加1
        if len(L)>10:  #仅输出10行
            break

#生成一个generator对象，然后通过for循环迭代输出每一行
a=triangel(10)
print(a)
for i in a:
    print(i)


for i in range(9):
    print(i, end=" ")





# 自己尝试一遍杨辉三角
def yanghui(n):
    L = [1]
    while True:
        yield L
        L = [L[x] + L[x + 1] for x in range(len(L) - 1)]
        L.insert(0, 1)
        L.append(1)
        n -= 1
        if n == 0:
            break
print()
g = yanghui(10)
for i in g:
    print(i)

