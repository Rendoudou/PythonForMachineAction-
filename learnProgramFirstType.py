"""
# Python学习 函数编写部分
# editor doudou
# date 17 02 2020
# ver 01 初次学习，抄录编辑。0217
# ver 02 add new cycle content.0219
"""

import sys

#
# Fibonacci Sequence
# 斐波那契数列输出
# para @amountNeeded (int) 需要的斐波那契数列长度
# out  @seqOut (list) 返回斐波那契数列
#
def Fibonacci(amountNeeded: int) -> list:
    if type(amountNeeded) == int:
        i = 0
        a, b = 0, 1
        seqOut = []
        while i < amountNeeded:
            a, b = b, a + b
            seqOut = seqOut + [a]
            i += 1
        return seqOut
    else:
        return []

    pass


#
# Condition Control
# 条件控制
# para @amountNeeded (int) 需要的斐波那契数列长度
# out  @seqOut (list) 返回斐波那契数列
#
def demoConditionControl(counterIn: int) -> dict:
    a = 0
    outDict = {}

    while a < counterIn:
        if a % 2 == 0:
            outDict[a] = 'is even'
        elif a % 2 != 0:
            outDict[a] = 'is odd'
        else:
            break
        a += 1
    print(outDict)
    # if语句的嵌套
    """
    if condition1:
        if condition2:
        elif (condition3):
        else:
    elif (condition4):
    else:
    """
    return outDict


#
# Condition Control
# 条件控制
# para @setNumber (int) 预设值数字
# out  @seqOut (list) 返回斐波那契数列
#
def guessNumberGame(setNumber: int) -> (int, list):
    guess = None
    guessTimeCount = 0
    guessList = []
    print("开始猜数字游戏！")

    while guess != setNumber:
        guess = int(input('请输入一个您猜测的数字：'))
        guessTimeCount += 1
        guessList.append(guess)
        if guess == setNumber:
            break
        elif guess > setNumber:
            print("偏大")
        else:
            print("偏小")
    print(f'猜对了！ 你猜测了{guessTimeCount}次')

    return guessTimeCount, guessList


#
# Cycle Control
# 循环语句
# para @inRange (int) 输入数字范围
# out  @counterSum (int) 输出总数
#
def cycleStatements(inRange: int) -> int:
    tempK = 0

    # while 语句
    while tempK < 10:
        tempK += 1
    # for 语句
    for tempK in range(10):
        pass
    # 求和1~100
    counter = 1
    counterSum = 0
    while counter <= inRange:
        counterSum += counter
        counter += 1
    print(f'1到{inRange}的和是 {counterSum}')

    return counterSum


# 无限循环
def foreverCycleFunction() -> bool:
    var = 1

    while var == 1:
        number = int(input("请输入一个数字："))
        print(f'你输入了数字 {number}')

    return True


# 无限循环搭配 else (新内容)
def whileCycleWithElse() -> bool:
    number = int(input("请输入一个数字："))

    while number < 10:
        number = int(input(f'你输入的数字是 {number}，它小于 10。请再输入一个数字：'))
    else:
        print(f'你输入的数字是 {number},退出循环。')

    return True


# 无限循环加入break
def whileCycleWithBreak() -> bool:
    flag = 1

    while flag:
        if int(input("请输入一个数字：")) > 10:
            print("while中的break")
            break

    return True


#
# For Function
# 循环语句 For
# para @inRange (int) 输入数字范围
# out  @counterSum (int) 输出总数
#
def forFunction():
    """
    typedef
        for <variable> in <sequence>:
            <statements>
        else:  # 如果
            <statements>
    :return:
    """
    print(type(range(0, 5, 1)))  # <class range>

    for temp in []:
        print(temp)
    else:
        print("没有经过循环。")

    for temp in range(20):
        print(temp)
    else:
        print("没有经过循环。")

    """
        range函数：生成数列
        range(5), range(0,5), range(0,5,1)
    """

    """
        break & continue & 循环中的else语句            
    """
    return


# 循环语句与else
def forElseFunction(inRange: int) -> bool:
    for temp in range(2, inRange):
        for i in range(2, temp):  # else语句在穷尽列表（for循环）或者
            # 条件变为false(while循环)时执行
            if temp % i == 0:
                print(f'{temp} = {i} * {int(temp / i)}')
                break
        else:
            print(f'{temp}是质数。')

    return True


#
# Wait Function
# while 等待键盘中断 <ctrl + c>
# para @void
# out  @void
#
def waitForStop():
    while True:
        pass
    pass


#
# Minimum Class
#
class emptyClass:

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
            print(next(getListIter))
        except StopIteration:
            sys.exit("error happen")

    pass


#
# Debug
# 调试用函数
#
if __name__ == '__main__':

    buildIter()

    forElseFunction(10)

    forFunction()

    whileCycleWithBreak()  # while循环中加入break

    whileCycleWithElse()  # while循环与else搭配

    cycleStatements(10)  # 循环语句

    guessNumberGame(23)  #

    demoConditionControl(10)

    # print(Fibonacci.__annotations__)
    print(Fibonacci(20))
    listFibo = Fibonacci(10)
    for j in range(len(listFibo)):
        if j == len(listFibo) - 1:
            print(listFibo[j], end='')
        else:
            print(listFibo[j], end=', ')

    pass  # pass语句是空语句，是为了保持程序结构的完整性
