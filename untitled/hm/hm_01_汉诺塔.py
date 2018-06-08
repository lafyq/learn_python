# 定义一个全局变量 count 用来计数移动了多少次
count = 0


def move(n, from_tower, buffer_tower, to_tower):
    """
    所以说一共就三步：
        1、把 n-1 号盘子移动到缓冲区
        2、把1号从起点移到终点
        3、然后把缓冲区的n-1号盘子也移到终点

    :param n: 所要移动的盘子
    :param from_tower: 起点
    :param buffer_tower: 缓冲区
    :param to_tower: 终点
    :return:
    """

    if n == 1:
        # 修改全局变量 count
        global count
        count += 1

        print(from_tower, '-->', to_tower)
    else:
        move(n - 1, from_tower, to_tower, buffer_tower)
        move(1, from_tower, buffer_tower, to_tower)
        move(n - 1, buffer_tower, from_tower, to_tower)


move(5, 'a', 'b', 'c')
print("总共移动了 %d 次" % count)


# 自己练手
count2 = 0

def move(n, a, b, c):
    if n == 1:
        print('move: %s --> %s' % (a, c))
        global count2
        count2 += 1

    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


move(5, 'a', 'b', 'c')
print("总共移动了 %d 次" % count)