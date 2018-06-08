

# def trim(s):
#     begin = None
#     end = None
#     flag = False
#     for i in s:
#         if not flag:
#             if i == ' ':
#                 pass
#             else:
#                 begin = s.index(i)
#                 flag = True
#         else:
#             if i == ' ':
#                 end = s.index(i)  # end会等于0，因为index返回的是第一次出现的字符
#                 break
#     return s[begin:end]
#
# s = "   adsf   s"
# print(trim(s))



# def trim(s):
#     begin = None
#     count = 0
#     end = None
#     flag = False  # 用False表示还没有出现过非空字符
#     for i in s:
#         if not flag:
#             # 一直遍历空字符，直到出现非空字符运行下面else
#             if i == ' ':
#                 continue
#             # 第一次出现非空字符
#             else:
#                 begin = s.index(i)
#                 flag = True
#         else:
#             count += 1  # 计算字符串的长度
#             if i == ' ':  # 第二次出现空字符
#                 break
#     end = begin + count
#     return s[begin:end]
#
# s = "   hello world！"
# print(trim(s))

"""
忙活了一下午，却没有找到正确的姿势

"""


# 貌似下面这个才是正确的姿势吧！！！！
def trim2(s):
    if s[:1] != ' ' and s[-1:] != ' ':
        # 第一个不是空格且倒数第一个也不是空格时返回s
        return s
    elif s[:1] == ' ':
        # s[0]处是空格，则从s[1]处开始取值
        # 此处切掉s[0]处的空格，s = s[1:]
        return trim2(s[1:])
    else:
        # s[-1]处是空格
        # 切掉s[-1]处的空格，取到倒数第二个，s = s[:-1]
        return trim2(s[:-1])

s = "   hello world！"
print(trim2(s))



L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print('L[0:3] =', L[0:3])
print('L[:3] =', L[:3])
print('L[1:3] =', L[1:3])
print('L[-2:] =', L[-2:])

R = list(range(100))
print('R[:10] =', R[:10])
print('R[-10:] =', R[-10:])
print('R[10:20] =', R[10:20])
print('R[:10:2] =', R[:10:2])
print('R[::5] =', R[::5])