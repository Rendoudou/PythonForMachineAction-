"""
# Python学习 迭代器与生成器
# editor doudou
# data 20 02 2020
# ver 01 初次学习，抄录编辑。0220
# learn https://blog.csdn.net/mieleizhi0522/article/details/82142856/
"""

import sys


#
# Fibonacci
# 斐波那契用迭代器实现
# para @n: int 希望得到的数列长度
# out  @迭代器 a
#
def fibonacciIter(n: int):
    a, b, count = 0, 1, 0

    while True:
        if count >= n:
            break
        yield a  # 返回一个迭代器，内容有a
        a, b = b, a + b
        count = count + 1
    pass


#
# 得到斐波那契数列并输出
# para @n: int 希望得到的数列长度
# out  @none
#
def getFibonacci(n: int):
    g = fibonacciIter(n)  # 得到第一个生成器（迭代器）

    while True:
        try:
            print(next(g))  # 从迭代器上次停止的地方继续执行
        except StopIteration:
            sys.exit("no more space")

    pass


#
# Iter 迭代器
# 迭代的两个基本方法 iter() 与 next()
# 迭代器是一个可以记住遍历的位置的对象
# 迭代器对象从集合的第一个元素开始访问，直到所有元素被访问结束。迭代器只能往前不会后退。
# 字符串，列表或元组对象都可用于创建迭代器
# para @void
# out  @void
#
def buildIter():
    listTemp = [1, 2, 3, 4]

    getListIter = iter(listTemp)
    for i in range(len(listTemp)):
        print(next(getListIter))

    for x in getListIter:
        print(x)

    while True:
        try:
            print(f'{next(getListIter)} ', end="")
        except StopIteration:
            sys.exit("error happen")

    pass


#
# help learn iterator
#
def foo():

    print("starting...")
    while True:
        res = yield 4
        print("res:", res)

    pass


#
# 使用方法一
#
def useFoo1():

    g = foo()
    print(next(g))
    print("*" * 20)
    print(next(g))

    pass


#
# 使用方法一
#
def useFoo2():

    g = foo()
    print(next(g))
    print("*" * 20)
    print(g.send(10))

    pass


#
# debug mode
#
if __name__ == '__main__':

    useFoo1()
    useFoo2()
    getFibonacci(10)

    pass
