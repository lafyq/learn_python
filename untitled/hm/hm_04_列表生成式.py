import os

print([x * x for x in range(1, 11) if x % 2 == 0])
print([x + y for x in 'ABC' for y in 'XYZ'])
print([d for d in os.listdir('.')])

# 要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 可以用list(range(1, 11))：
# 刚刚踩的坑（注意不是中括号）：print(list[range(1, 11)])
print(list(range(1, 11)))

# 要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
print("")
print("-" * 50)
print("使用循环输出[1x1, 2x2, 3x3, ..., 10x10]：")

list1 = []
for x in range(1, 11):
    list1.append(x * x)
print(list1)

# 但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
print("")
print("-" * 50)
print("使用列表生成式输出[1x1, 2x2, 3x3, ..., 10x10]：")

list2 = [x * x for x in range(1, 11)]

print(list2)

# 列表生成式非常方便，for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
print("")
print("-" * 50)
print("使用列表生成式输出1--100 并筛选出仅偶数的平方：")

list3 = [x * x for x in range(1, 11) if x % 2 == 0]

print(list3)

# 还可以使用两层循环，可以生成全排列：
print("")
print("-" * 50)
print("使用列表生成式 生成全排列：")

list4 = [m + n for m in "ABC" for n in "XYZ"]
print(list4)

# 还可以列出当前目录下的所有文件和目录名：
print("")
print("-" * 50)
print("使用列表生成式 列出当前目录下的所有文件和目录名：")

list5 = [d for d in os.listdir('.')] # os.listdir可以列出文件和目录, '.'表示当前目录
print(list5)


# 练手小题，将L1中所有字符串变成小写并输出（非字符串不用）
print("")
print("-" * 50)
print("练手小题，使用列表生成式 将L1中所有字符串变成小写并输出（非字符串不用）：")
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print("L1 =", L1)
print("L2 =", L2)