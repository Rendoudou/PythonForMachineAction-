"""
# Python学习 操作函数部分
# editor doudou
# data 13 02 2020
# ver 01 初次学习，抄录编辑。0213
# ver 02 file format.0219
"""


#
# 算数运算符
#
def mathematicsOperator():
    a = 21
    b = 10
    c = 0

    c = a + b
    print("1 - c 的值为：", c)

    c = a - b
    print("2 - c 的值为：", c)

    c = a * b
    print("3 - c 的值为：", c)

    c = a / b
    print("4 - c 的值为：", c)

    c = a % b
    print("5 - c 的值为：", c)

    # 修改变量 a 、b 、c
    a = 2
    b = 3
    c = a ** b
    print("6 - c 的值为：", c)

    a = 10
    b = 5
    c = a // b
    print("7 - c 的值为：", c)
    pass


#
# 测试比较关系运算符
#
def compareOperator():
    a = ['a', 'v', 's']
    print(type(a))
    print(type(a), end="")
    # if (n := len(a)) > 3:
    if len(a) > 3:
        print("n大于3")
    else:
        print("n小于等于3")

    pass


#
# 赋值运算符
#
def assignmentOperator():
    a = 21
    b = 10
    c = 0

    c = a + b
    print("1 - c 的值为：", c)

    c += a
    print("2 - c 的值为：", c)

    c *= a
    print("3 - c 的值为：", c)

    c /= a
    print("4 - c 的值为：", c)

    c = 2
    c %= a
    print("5 - c 的值为：", c)

    c **= a
    print("6 - c 的值为：", c)

    c //= a
    print("7 - c 的值为：", c)

    pass


#
# 位运算符
#
def bitOperator():
    a = 60  # 60 = 0011 1100
    b = 13  # 13 = 0000 1101
    c = 0

    c = a & b  # 12 = 0000 1100
    print("1 - c 的值为：", c)

    c = a | b  # 61 = 0011 1101
    print("2 - c 的值为：", c)

    c = a ^ b  # 49 = 0011 0001
    print("3 - c 的值为：", c)

    c = ~a  # -61 = 1100 0011
    print("4 - c 的值为：", c)

    c = a << 2  # 240 = 1111 0000
    print("5 - c 的值为：", c)

    c = a >> 2  # 15 = 0000 1111
    print("6 - c 的值为：", c)

    pass


#
# 逻辑运算符
# and 返回其中一个，只有两者都为非0时才返回非0，本质就是&&(C)	  布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。
# or 返回可能有的非零值，本质为||(C)    布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。
# not true得到false,false得到true
#
def logicOperator():
    a = 10
    b = 20

    if a and b:
        print("a and b 的返回值是", a and b, " 1 - 变量 a 和 b 都为 true")
    else:
        print("a and b 的返回值是", a and b, " 1 - 变量 a 和 b 有一个不为 true")

    if a or b:
        print("a or b 的返回值是", a or b, " 2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
    else:
        print("a or b 的返回值是", a or b, " 2 - 变量 a 和 b 都不为 true")

    # 修改变量 a 的值
    a = 0
    if a and b:
        print("a and b 的返回值是", a and b, " 3 - 变量 a 和 b 都为 true")
    else:
        print("a and b 的返回值是", a and b, " 3 - 变量 a 和 b 有一个不为 true")

    if a or b:
        print("a or b 的返回值是", a or b, " 4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
    else:
        print("a or b 的返回值是", a or b, " 4 - 变量 a 和 b 都不为 true")

    if not a and b:
        print("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
    else:
        print("5 - 变量 a 和 b 都为 true")

    pass


#
# 成员运算符
# in 如果在指定的序列中找到值返回true，否则返回false
# not in  如果在指定的序列中没有找到值返回 True，否则返回 False
#
def memberOperator():
    lista = [1, 2, 3, '2', 'a', 5]
    listB = [1, 2, 2, 3, 1, 2, 3, 1, 2, 3, 1, 3, 1, 2, 3, 1, 3, 2, 1]
    n = listB.pop()
    print(listB)
    print(n)
    if 'a' in lista:
        print("a在列表lista中。")
    else:
        print("a不在列表lista中。")

    if 'a' not in lista:
        print("a不在列表lista中。")
    else:
        print("a在列表lista中。")

    pass


#
# 身份运算符
# is 	  is 是判断两个标识符是不是引用自一个对象
# is not  	is not 是判断两个标识符是不是引用自不同对象
# added id()函数：id()函数可以用来获取对象内存地址
#
def identityOperator():
    a = 20
    b = 20

    print("a的地址位", id(a))
    print("b的地址位", id(b))

    if a == b:
        print("1 - a 和 b 有相同的标识")
    else:
        print("1 - a 和 b 没有相同的标识")

    if id(a) == id(b):
        print("2 - a 和 b 有相同的标识")
    else:
        print("2 - a 和 b 没有相同的标识")

    # 修改变量 b 的值
    b = 30

    print("a的地址位", id(a))
    print("b的地址位", id(b))

    if a == b:
        print("3 - a 和 b 有相同的标识")
    else:
        print("3 - a 和 b 没有相同的标识")

    if a != b:
        print("4 - a 和 b 没有相同的标识")
    else:
        print("4 - a 和 b 有相同的标识")

    pass


#
# python运算符优先级
# 不需要死记硬背
# and 的优先级比较高
#
def priorityOperator():
    a = 20
    b = 10
    c = 15
    d = 5
    e = 0

    e = (a + b) * c / d  # ( 30 * 15 ) / 5
    print("(a + b) * c / d 运算结果为：", e)

    e = ((a + b) * c) / d  # (30 * 15 ) / 5
    print("((a + b) * c) / d 运算结果为：", e)

    e = (a + b) * (c / d)  # (30) * (15/5)
    print("(a + b) * (c / d) 运算结果为：", e)

    e = a + (b * c) / d  # 20 + (150/5)
    print("a + (b * c) / d 运算结果为：", e)

    x = True
    y = False
    z = False
    print("x or y : ", x or y)
    print("y and z : ", y and z)
    print("x or y and z : ", x or y and z)

    if x or y and z:
        print("yes")
    else:
        print("no")

    pass


#
# debugMode
# prepare for debug itself
#
if __name__ == '__main__':

    pass
