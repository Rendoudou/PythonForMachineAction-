'''
# file name: kNN.py
# description: kNN算法python 实现样例
# establish date: 2020 01 01
# author: doudou
'''

from numpy import *
import matplotlib
import matplotlib.pyplot as plt
import operator


'''
# kNN算法python 设立数据集
# 2020 01 01
# version 01
# func createDataSet()
# para void
# out void
'''
def createDataSet():
    dataSet = array([[1.0, 1.1], [1.0, 1.0], [0.0, 0.0], [0.0, 0.1]])
    lables = ['A', 'A', 'B', 'B']

    return dataSet,lables


'''
# kNN算法python k近邻算法
# use for 依据样本与输入向量的欧氏距离评判输入向量标签
# 2020 01 04
# version 01
# func classifyDir(inX, dataSet, lables, k)
# para 
    @ inX     用于分类的输入向量
    @ dataSet 预先设置的数据集合
    @ lables  对应数据集合标签向量
    @ k       要求匹配的样本数目
# out 
    @ sortedClassCount[0][0] 数据处理后得出的标签
'''
def classifyDir(inX, dataSet, lables, k):
    dataSize = dataSet.shape[0]                     #dataSize 与 dataSet.shape[0]代表行数
    diffMat = tile(inX, (dataSize, 1)) - dataSet    #tile 函数重复inX的各个维度，重复行后与各个样本乡间得到距离差数据（二维）
    sqDiffMat = diffMat ** 2                        #平方距离，每一个维度平方
    sqDistances = sqDiffMat.sum(axis = 1)           #平方和
    distances = sqDistances ** 0.5                  #开根号，实际距离
    sortedDistance = distances.argsort()            #实际距离排序,返回的是索引值，从小到大排序后的数组的索引值
    classCount = { }                                #空字典
    for i in range(k):
        nowMinestDistance = sortedDistance[i]
        voteIlabel = lables[nowMinestDistance]                        #提取最接近索引值对应的标签，先是提取最小值的索引值，
                                                                      #再通过索引值找到最小值对应的标签，之后提取次小值的标签
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1    #返回指定键（key）的值并加一，如果不存在则返回默认值（0），原始数值会出现两个B，结果必然为B
    sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)    #字典以列表的形式返回（list）
    '''
    sorted(iterable, key=None, reverse=False)
    @para
        iterable -- 可迭代对象。
        key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
        reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。
    '''
    return sortedClassCount[0][0]


'''
# kNN算法python 文本操作
# use for 将文本数据转化为可操作数据格式
# 2020 01 16
# version 01
# func fileMatrix(filename)
# para 
    @ filename 文件名
# out 
    @ returnMat 返回处理后的数据集
    @ classLabelVector 返回处理后的标签数据集
'''
def file2Matrix(fileName):
    fileOpen = open(fileName)                       #输入参数文件名打开文件
    arrayOfLines = fileOpen.readlines()             #返回一行行的列表
    numberOfLines = len(arrayOfLines)               #得到列表的行数
    returnMat = zeros((numberOfLines, 3))           #创建空的表格 行数*3
    classLabelVector = []                           #空字典
    index = 0
    for line in arrayOfLines:
        line = line.strip()                             #返回移除字符串头尾指定的字符生成的新字符串。
        listFromLine = line.split('\t')                 #依照空格分割字符串
        returnMat[index, : ] = listFromLine[0 : 3]
        classLabelVector.append(int(listFromLine[-1]))  #取列表的最后一个格子,利用append方法在列表后面加入新的对象，类似队列在最后加上对象，显示转换为int整型
        index = index + 1
    return returnMat, classLabelVector


'''
# kNN算法python
# use for 将数据作图
# 2020 01 22
# version 01
# func dataMatPlot(dataMat)
# para 
    @ dataMat 合适的数据格式，file2Matrix返回的数据矩阵
    @ dataLabel 合适的数据格式，file2Matrix返回的数据标签
# out void
'''
def dataMatPlot(dataMat, dataLabel):
    plt.figure(figsize = (6, 6), dpi = 80)
    fig = plt.figure(1) #第一个画板 返回的是figure对象，可以用add_subplot添加图片
    '''
    scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None,
           verts=None, edgecolors=None, hold=None, data=None, **kwargs)
    https://blog.csdn.net/qiu931110/article/details/68130199 参考
    ax.scatter(dataMat[:, 1], dataMat[:, 2])
    '''

    ax1 = fig.add_subplot(221)
    ax1.set_title('plot one')
    ax1.set_xlabel('玩视频游戏所消耗的时间的百分比')
    ax1.set_ylabel('每周所消费的冰激凌公升数')
    ax1.scatter(dataMat[ : , 1], dataMat[ : ,2]) #参数分别是第二列和第三列

    ax2 = fig.add_subplot(222)
    ax2.set_title('plot two')
    ax2.set_xlabel('玩视频游戏所消耗的时间的百分比')
    ax2.set_ylabel('每周所消费的冰激凌公升数')
    ax2.scatter(x = dataMat[:, 1], y = dataMat[:, 2], s = 15.0*array(dataLabel),
               c = 15.0*array(dataLabel)) #设置每个点的大小，和每个点的颜色，根据标签设置

    ax3 = fig.add_subplot(223)
    ax3.set_title('plot three')
    ax3.set_xlabel('每年获取的飞行常客里程数')
    ax3.set_ylabel('玩视频游戏所消耗的时间的百分比')
    ax3.scatter(x=dataMat[:, 0], y=dataMat[:, 1], s=15.0 * array(dataLabel),
               c=15.0 * array(dataLabel))  # 设置每个点的大小，和每个点的颜色，根据标签设置
    plt.show()
    '''
    plt.figure(figsize = (6, 6), dpi = 80)
    plt.figure(1) #第一个画板 返回的是figure对象，可以用add_subplot添加图片

    ax1 = plt.subplot(221)
    ax1.scatter(dataMat[ : , 1], dataMat[ : ,2]) #参数分别是第二列和第三列

    ax2 = plt.subplot(222)
    ax2.scatter(x = dataMat[:, 1], y = dataMat[:, 2], s = 15.0*array(dataLabel),
               c = 15.0*array(dataLabel)) #设置每个点的大小，和每个点的颜色，根据标签设置
    ax3 = plt.subplot(223)
    ax3.scatter(x=dataMat[:, 0], y=dataMat[:, 1], s=15.0 * array(dataLabel),
               c=15.0 * array(dataLabel))  # 设置每个点的大小，和每个点的颜色，根据标签设置
    plt.show()
    '''
    return


'''
# kNN算法python
# use for 归一化数值
# 2020 02 11
# version 01
# func autoNorm(dataSet)
# para 
    @ dataSet 输入数据集
# out
    @ normDataSet 归一化后的数据集
'''
def autoNorm(dataSet):
    minValue = dataSet.min(0)
    maxValue = dataSet.max(0)
    ranges = maxValue - minValue
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape(0)

    return normDataSet

'''
# kNN算法python k近邻算法
# 2020 01 05
# version 01
# debug
#   __name__ 是每一个py文件的一个内置变量，用来指代当前运行的模块名称，会改变
#   __main__ 始终指当前执行模块的名称
#   只有当文件自身运行到此处时才符合__name__ == '__main__'，所以只有debug时能运行此处代码
#   https://blog.csdn.net/heqiang525/article/details/89879056
'''
if __name__ == '__main__':

    dataSet,lables = createDataSet()
    inx = [0.0, 0.0]
    test = classifyDir(inx, dataSet, lables, 2)
    #print(test)
    dataMat,dataLabel = file2Matrix("datingTestSet2.txt")
    dataMatPlot(dataMat,dataLabel)











