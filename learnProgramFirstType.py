"""
# Python学习 函数编写部分
# editor doudou
# date 17 02 2020
# ver 01 初次学习，抄录编辑。0217
"""


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
# para @
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


#
# Debug
# 调试用函数
#
if __name__ == '__main__':

    cycleStatements(10)

    guessNumberGame(23)

    demoConditionControl(10)

    # print(Fibonacci.__annotations__)
    print(Fibonacci(20))
    listFibo = Fibonacci(10)
    for j in range(len(listFibo)):
        if j == len(listFibo) - 1:
            print(listFibo[j], end='')
        else:
            print(listFibo[j], end=', ')

    pass
