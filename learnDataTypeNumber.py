'''
# Python学习 数据类型部分
# start 2020 0214
# ver 01
'''

import  random


#
# 基本数据操作，实例，赋值，删除引用
# 数值类型 整形，浮点型，复数类型
#
def basicTest():
    var1 = 0x10
    var2 = 0o20
    print(id(var1))
    del var1 #解除对var1的引用
    #print(id(var1))
    print(id(var2))
    return


#
# exchange data type
# python 数据类型转换
#
def exchangeDataType(dataIn, aimType):
    if aimType == 1:
        return int(dataIn)
    else :
        if aimType == 2:
            return float(dataIn)
        else:
            if aimType == 3:
                return complex(dataIn)
    return False


#
# mathematical
# python 数字运算
#
def mathematicalForPython():

    print(17 / 3) #除法 返回浮点数
    print(17 // 3) #除法 返回向下取整的结果，不一定是整数类型
    print(17 % 3) #取余操作
    print(17 ** 3) #幂运算
    #在交互模式中，最后被输出的表达式结果被赋值给变量 _ 。
    # “_”下划线是一个变量
    '''
    #数学函数
    abs(x) 返回数字的绝对值
    ceil(x) 返回数字的上入整数，例如math.ceil(4.1)= 5
    cmp(x,y) 比较函数 Python 3 已废弃，使用 (x>y)-(x<y) 替换。
    exp(x) 返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
    fabs(x) 返回浮点数类型
    floor(x) 返回数字的下舍整数，如math.floor(4.9)返回 4
    log(x)
    log10(x)
    max(x1,x2)
    min(x1.x2)
    modf(x) 返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
    pow(x,y) 返回 x**y
    round(x[,n]) 返回浮点数 x 的四舍五入值，如给出 n 值，则代表舍入到小数点后的位数。
                 其实准确的说是保留值将保留到离上一位更近的一端。数据截取用模块，精度不高
    sqrt(x) 求平方根
    '''
    return


#
# Python random
# python 随机数运算
#
def randomData():
    #random.choice(seq)
    dataOut = random.choice(range(10)) #从序列中随机选择一个元素
    print(dataOut)

    #random.randrange ([start,] stop [,step])方法返回指定递增基数集合中的一个随机数，基数默认值为1。
    #start - - 指定范围内的开始值，包含在范围内。
    #stop - - 指定范围内的结束值，不包含在范围内。
    #step - - 指定递增基数。
    # 从 1-100 中选取一个奇数
    print("randrange(1,100, 2) : ", random.randrange(1, 100, 2))
    # 从 0-99 选取一个随机数
    print("randrange(100) : ", random.randrange(100))

    #random.random()
    print(random.random()) #随机生成下一个实数，它在[0,1)范围内。

    #random.seed() 随机数种子生成器，类似C
    random.seed()

    #random.shuffle(lst)将序列的所有元素随机排序
    list = [20, 16, 10, 5]
    random.shuffle(list)
    print("随机排序列表 : ", list)
    random.shuffle(list)
    print("随机排序列表 : ", list)

    #random.uniform(x,y) uniform() 方法将随机生成下一个实数，它在 [x,y] 范围内
    print("uniform(5, 10) 的随机浮点数 : ", random.uniform(5, 10))
    print("uniform(7, 14) 的随机浮点数 : ", random.uniform(7, 14))

    return


#
# Python String
# python 字符串
#
def stringPython():
    var1 = 'Hello World!'
    var2 = "Runoob"

    print("var1[0]: ", var1[0])
    print("var2[1:5]: ", var2[1:5])
    print("已更新字符串 : ", var1[:6] + 'Runoob!') #字符串拼接

    #Python字符串格式化
    print("我叫 %s 今年 %d 岁!" % ('小明', 10))

    #Python三引号 python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符
    para_str = """这是一个多行字符串的实例
    多行字符串可以使用制表符
    TAB ( \t )。
    也可以使用换行符 [ \n ]。
    """
    print(para_str)

    #f-string

    #数字格式化
    return


#
# Python L
# python 列表
#
def listPython():
    '''
    序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。
    Python有6个序列的内置类型，但最常见的是列表和元组。
    序列都可以进行的操作包括索引，切片，加，乘，检查成员。
    此外，Python已经内置确定序列的长度以及确定最大和最小的元素的方法。
    列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。
    列表的数据项不需要具有相同的类型
    创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可
    '''

    return


'''
# debug mode
# 调试模块
'''
if __name__ == '__main__':
    dict = {'name':'Runoob:', 'url':'www.baidu.com'}
    print(f'what is {dict["name"]} {dict["url"]}')
    para_str1 = '丹丹'
    para_str2 = "萝莉"
    print(f'你在说什么？ {para_str1 + "是大美女"}')
    print('你在说什么？' + para_str1 + "是大美女")

    x  = 1
    print(f'{x+1}')
    print(f'{x+1=}')  # Python 3.8

    pass
