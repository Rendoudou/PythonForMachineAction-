"""
# Python学习 数据类型部分
# editor doudou
# date 14 02 2020
# ver 01 初次学习，抄录编辑。0214
"""

import random


#
# 基本数据操作，实例，赋值，删除引用
# 数值类型 整形，浮点型，复数类型
#
def basicTest():
    var1 = 0x10
    var2 = 0o20
    print(id(var1))
    del var1  # 解除对var1的引用
    # print(id(var1))
    print(id(var2))
    pass


#
# exchange data type
# python 数据类型转换
#
def exchangeDataType(dataIn, aimType):
    if aimType == 1:
        return int(dataIn)
    else:
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
    print(17 / 3)  # 除法 返回浮点数
    print(17 // 3)  # 除法 返回向下取整的结果，不一定是整数类型
    print(17 % 3)  # 取余操作
    print(17 ** 3)  # 幂运算
    # 在交互模式中，最后被输出的表达式结果被赋值给变量 _ 。
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
    pass


#
# Python random
# python 随机数运算
#
def randomData():
    # random.choice(seq)
    dataOut = random.choice(range(10))  # 从序列中随机选择一个元素
    print(dataOut)

    # random.randrange ([start,] stop [,step])方法返回指定递增基数集合中的一个随机数，基数默认值为1。
    # start - - 指定范围内的开始值，包含在范围内。
    # stop - - 指定范围内的结束值，不包含在范围内。
    # step - - 指定递增基数。
    # 从 1-100 中选取一个奇数
    print("randrange(1,100, 2) : ", random.randrange(1, 100, 2))
    # 从 0-99 选取一个随机数
    print("randrange(100) : ", random.randrange(100))

    # random.random()
    print(random.random())  # 随机生成下一个实数，它在[0,1)范围内。

    # random.seed() 随机数种子生成器，类似C
    random.seed()

    # random.shuffle(lst)将序列的所有元素随机排序
    listTemp1 = [20, 16, 10, 5]
    random.shuffle(listTemp1)
    print("随机排序列表 : ", listTemp1)
    random.shuffle(listTemp1)
    print("随机排序列表 : ", listTemp1)

    # random.uniform(x,y) uniform() 方法将随机生成下一个实数，它在 [x,y] 范围内
    print("uniform(5, 10) 的随机浮点数 : ", random.uniform(5, 10))
    print("uniform(7, 14) 的随机浮点数 : ", random.uniform(7, 14))

    pass


#
# Python String
# python 字符串
#
def stringPython():
    var1 = 'Hello World!'
    var2 = "Runoob"

    print("var1[0]: ", var1[0])
    print("var2[1:5]: ", var2[1:5])
    print("已更新字符串 : ", var1[:6] + 'Runoob!')  # 字符串拼接

    # Python字符串格式化
    print("我叫 %s 今年 %d 岁!" % ('小明', 10))

    # Python三引号 python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符
    para_str = """这是一个多行字符串的实例
    多行字符串可以使用制表符
    TAB ( \t )。
    也可以使用换行符 [ \n ]。
    """
    print(para_str)

    # f-string

    # 数字格式化
    pass


#
# Python List
# python 列表
#
def listPython():
    """
    序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。
    Python有6个序列的内置类型，但最常见的是列表和元组。
    序列都可以进行的操作包括索引，切片，加，乘，检查成员。
    此外，Python已经内置确定序列的长度以及确定最大和最小的元素的方法。
    列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。
    列表的数据项不需要具有相同的类型
    创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可
    """
    list1Temp = ['Google', 'Runoob', 1997, 2000]
    list2 = [1, 2, 3, 4, 5]
    list3 = ["a", "b", "c", "d"]

    print("list1[0]: ", list1Temp[0])
    print("list2[1:5]: ", list2[1:5])
    if "a" in list3:
        print('a在list3中。')
    # updata list
    # 列表的成员是可变的，而字符串中是不可变的
    list1Temp[2] = 'doudou'
    print(list1Temp[2])
    print(list1Temp[0:3])  # list1[0] list1[1] list1[2]
    # list.append()方法
    # del 可以用来删除列表中的某一个元素，成为新的列表
    del list1Temp[2]
    print(list1Temp)

    if 3 in list1Temp:
        print(True)
    for temp in list1Temp:
        print(temp)
    print(len(list1Temp))
    print(list1Temp + list2)
    print(list1Temp * 4)
    print(list1Temp[-1])
    # 列表函数和方法
    len(list1Temp)
    max(list1Temp)
    min(list1Temp)
    tempSeq = ('dou', 'dan', '在', '一', '起')  # 元组
    tempList = list(tempSeq)
    print(tempList)  # 元组转化为列表
    tempList.append('233333')
    '''
        list.append(obj) 在列表末尾添加新对象
        list.count(obj) 统计某个对象在列表中出现的次数
        list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
        list.index(obj) 从列表中找出某个值第一个匹配项的索引位置，查找索引值
        list.insert(index, obj) 将对象插入列表
        list.pop([index=-1]) 移除列表中的一个元素，默认是对后一个，并返回该元素的值
        list,remove(obj) 移除列表中的第一个匹配项
        list.reverse() 反向列表中的元素
        list.sort(key = None, reverse = False) 对原列表进行排序
        list.clear() 情况列表
        list.copy() 复制列表
    '''
    # 嵌套列表
    # listAdd = [list1Temp, list2, list3]

    pass


#
# Python Tuple
# python 元组
# 元组和列表类似，都是线性表。唯一不同的是，Python的元组被赋值后所存储的数据
# 不能被程序修改，可以将元组看作是只能读取数据不能修改的列表
#
def tuplePython():
    # 创建元组 tuple = () list = []
    tupleTemp1 = ('Google', 'Runoob', 1997, 2000)
    # tupleTemp2 = "a", "b", "c", "d"  # 不需要括号也可
    # 空元组
    # tupleTemp3 = ()
    # 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用：
    tupleTemp4 = 12
    print(type(tupleTemp4))  # int
    tupleTemp5 = (12,)
    print(type(tupleTemp5))  # tuple
    # 访问元组和访问列表类似
    print(tupleTemp1[0])

    # 创建空元组和单元素的元组
    tup1 = [50]
    print(type(tup1))
    tup2 = (49,)
    print(type(tup2))
    # 元组中的元素值是不允许修改的，但是我们可以对元组进行连接组合
    tup3 = tuple(tup1) + tup2
    # 可以删除整个元组,tuple(obj) obj应当为迭代器
    del tup3
    # 元组运算符
    '''
    len(tuple)
    tup1 + tup2
    tuple * 4
    element in tuple
    for temp in tuple
    '''
    # 元组索引和截取
    # 。。。

    # 元组内置的函数
    '''
    len(tuple)
    max(tuple)
    min(tuple)
    tuple(iterable)
    '''
    # 所谓元组的不可变指的是元组所指向的内存中的内容不可变。
    # 不能做一维操作，如果元组中存在列表等，要另行考虑。

    pass


#
# Python Dictionary
# python 字典
# 字典是另一种可变容器模型，且可存储任意类型对象。
# 字典的每个键值(key=>value)对用冒号(:)分割，
# 每个对之间用逗号(,)分割，整个字典包括在花括号({})中
# 可变的数据类型: dict = { }, list = []
# 不可变的数据类型: string = ''或 “”，tuple = （obj1, obj2, ...）或者
# tuple = obj1, obj2 , number = data;存在多种嵌套。
#
def dictPython():
    # 用 \ 来实现多行语句
    """
    total = item_one + \
        item_two + \
        item_three
    :return:
    """
    dictVoid = {}
    listTuple = (1,)
    dictTemp = {listTuple: 'doudou', 2: 'dandan', 3: 'qiqi'}
    # 键必须是唯一的，但值则不必。
    # 值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
    print(dictTemp[(1,)])  # 用元组来作为字典的键，键必须是不可变的
    dictPyTemp = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
    dictTemp.update(dictPyTemp)  # 合并了字典
    print(dictTemp)
    pop_obj1 = dictTemp.pop((1,), None)
    print('pop_obj1: ', pop_obj1)
    print(dictTemp)
    pop_obj2 = dictTemp.popitem()
    print('pop_obj2: ', pop_obj2)
    print(dictTemp)

    print("dict['Name']: ", dictPyTemp['Name'])
    print("dict['Age']: ", dictPyTemp['Age'])
    # 修改字典
    dictPyTemp['Name'] = 'DouDou'
    # 删除字典元素 清空字典 删除字典
    del dictPyTemp['Name']
    dictPyTemp.clear()
    del dictPyTemp
    # 字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行
    # 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
    # 键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
    # dict = {['Name']: 'Runoob', 'Age': 7} 将会报错

    """
    #内置函数
    len(dict)
    str(dict)
    type(variable)
    #内置方法   
    dict.clear()清空字典
    dict.copy()返回一个字典的浅复制
    dict.fromkeys(seq[,value])创建一个新字典，以序列seq中的元素作为字典的键，val为字典所有键对应的初始值
        value为可选参数，其为所有键对应的值，暂未找到可以通过该方法各个单独设置。默认为none
    dict.get(key, default = none)返回指定键的值，如果没有则返回default值
    key in dict
    dict.items()以列表返回可遍历的（键，值）元组数据
    dict.keys()返回一个迭代器，可以使用list()来转换为列表，此处使用键
    dict.setdefault(key, default = none)和get类似，如果该键不存在字典中，将会添加键并将值设为default
    dict.update(dict2)用字典dict2中的键/值对更新到dict中
    dict.values()返回一个迭代器，可以使用list()来转换为列表,此处使用键值
    dict.pop(key[,default])pop方法删除字典给定键key所对应的值，返回的是被删除的值，key值必须给出。否则返回default值
    """
    seqTemp = ('name', 'sex', 'age')
    dictFromSeqTemp = dict.fromkeys(seqTemp)

    pass


#
# Python Dict HomeWork
#
countryCounter = {}  # 局部静态


# 逐个添加
def addOne(countryIn):
    if countryIn in countryCounter:
        countryCounter[countryIn] += 1
    else:
        countryCounter[countryIn] = 1

    pass

# 利用addone批量操作
def countInList(inCountry):
    for tempI in inCountry:
        addOne(tempI)

    pass


#
# Python Set
# 集合是一个无序的不重复元素序列
# 可以用大括号{ obj }或者set()进行创建，但是不能用空大括号创建，因为{}是用来创建一个空字典的。
#
#
def setPython():
    basket = {'apple', 'orange', 'apple', 'pear', 'banana'}
    print(basket)
    dictBasket = {1: 'apple', 2: 'orange', 3: 'pear'}
    dictBasket.setdefault(4, 'banana')
    dictBasketInBasket = {1: 'apple', 2: 'orange', 3: 'pear'}
    dictBasket.setdefault(5, dictBasketInBasket)  # 在字典中添加子字典

    tupleA = ('apple', 'orange', 'apple', 'pear', 'banana')
    setA = set(tupleA)  # set(iterable) iterable:string，list，tuple，dict，file，xrange
    setB = set('asdfghjkl')
    print(setA - setB)
    print(setB | setA)
    print(setA & setB)
    print(setB ^ setA)

    a = {x for x in 'abcdef' if x not in 'abc'}
    print(a)  # set数据的输出顺序问题 hash值 https://www.cnblogs.com/abdm-989/p/11329122.html
    # 在集合中增加元素
    a.add('baidu')
    a.update([1, 2], [2, 3])
    a.update({4, 5})
    print(a)
    # 在集合中移除元素
    a.remove(1)  # a.remove(obj)如果移除对象不存在的话，会发生错误
    a.discard(2)  # 移除对象，如果移除对象不存在的话，不会发生错误
    a.pop()  # 随机删除集合中的一个元素，返回删除的元素。
    # pop方法会对集合进行无序排列，然后将这个无序排列集合的左边第一个元素进行删除。
    # 计数集合元素个数
    # length = len(a)  #计算集合的元素个数
    # 清空集合
    a.clear()
    # 判断元素是否在集合中
    if 4 in a:
        pass
    else:
        print('不在其中')
    # 内置方法完整列表
    """
    set.add()
    set.clear()
    set.copy()
    set.difference()返回一个移除相同元素的新集合
    set.difference_update()直接在原来的集合中移除元素
    set.discard()删除指定元素
    set.intersection()返回交集,一个新的集合
    set.intersection_update()在原始集合上移除不交集的元素
    set.isdisjoint()判断两个集合是否包含相同的元素
    set.issubset()判断指定集合的所有元素是否都包含在指定集合中
    set.issuperset()判断指定集合的所有元素是否都包含在原始的集合中
    set.pop()
    set.remove()
    set.symmetric_difference()返回两个集合不重复的元素集合，一个新集合
    set.symmetric_difference_update()移除与另一集合相同元素。在当前集合中插入另一个集合中的不重复元素。
    set.union()返回两个集合的并集
    set.update()给集合添加元素
    """
    pass


'''
# debug mode
# 调试模块
'''
if __name__ == '__main__':

    setUp = {1, 2, 3, 4, 5, 6, 7}
    setLower = {2, 3}
    print(setUp.issuperset(setLower))
    print(setLower.issubset(setUp))

    setPython()

    country = ['China', 'japan', 'china']
    countInList(country)
    print(len(countryCounter))
    dictPython()

    seq = ('name', 'sex', 'age')
    dictFromSeq = dict.fromkeys(seq, 10)
    getDictItem = dictFromSeq.items()
    getDictList = list(dictFromSeq.keys())
    print('type(getDictItem) ： ', type(getDictItem))  # <class 'dict_item'>
    print(getDictItem)
    print('type(getDictList) ： ', type(getDictList))
    print(getDictList)
    # getItem['name'] = 'doudou' #不可变的类型

    listTest = ['Google', 'Runoob', 1997, 2000]
    tupleTest = (listTest, 'test', 'doudou', 'dandan')
    print(type(tupleTest))
    print(tupleTest[0][1])
    tupleTest[0][1] = 10
    print(tupleTest[0][1])
    for i in range(len(tupleTest[0])):
        tupleTest[0][i] = []
    print("clear")
    # tupleTest[1][0] = 'a' #字符串也是不可变的
    # tupleTest[1] = tupleTest[1] + tupleTest[2]
    # tupleTest[0] = ()#对元组的一维操作是不允许的
    stringTemp = tupleTest[1] + tupleTest[2]

    listTemp = []
    print(type(listTemp))
    tupleTemp = ()
    print(type(tupleTemp))

    list1 = ['Google', 'Runoob', 1997, 2000]
    list1[2] = 'doudou'
    print(list1[2])
    print(list1[0:3])
    tupleTemp = tuple(list1 + listTemp)

    '''
    dict = {'name':'Runoob:', 'url':'www.baidu.com'}
    print(f'what is {dict["name"]} {dict["url"]}')
    para_str1 = '丹丹'
    para_str2 = "萝莉"
    print(f'你在说什么？ {para_str1 + "是大美女"}')
    print('你在说什么？' + para_str1 + "是大美女")

    x  = 1
    print(f'{x+1}')
    print(f'{x+1=}')  # Python 3.8
    '''
    pass
