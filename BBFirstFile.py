# !/user/bin/python
# -*- coding:utf-8 -*-

# numpy的底层是用C语言写的，为了提高速度
import numpy as np
import matplotlib.pyplot as plt
import math
import time


#
# Test
#
def draw():

    start = time.time()
    #start = time.clock()
    u = 0
    sigma = 1
    x = np.linspace(u - 3 * sigma, u + 3 * sigma, 51)
    y = np.exp((-(x - u) ** 2)/(2 * sigma ** 2)) / (math.sqrt(2 * math.pi) * sigma)

    plt.figure(1) # 创建画布
    plt.plot(x, y, 'r-', x, y, 'go', linewidth=2, markersize=8)
    plt.grid(True)
    plt.show()

    timePass = time.time() - start
    print(timePass)

    pass

#
# 堆叠 stack and axis
#
def arrayStack():
    pass


#
# array get
#
def getUniqueArray():
    # 暴力去重
    arrayBasic = np.array(((1, 2), (3, 4), (5, 6), (1, 3), (3, 4), (7, 6)))
    print("去重前")
    print(arrayBasic)

    # 方案一
    arrayToComplex = arrayBasic[:, 0] + arrayBasic[:, 1] * 1j
    np.unique(arrayToComplex)
    indexUnique = np.unique(arrayToComplex, return_index=True)[1]
    print("去重后")
    print(arrayBasic[indexUnique])

    # 暴力去重
    # 集合的元素不重复
    arrayList = list(set((tuple(t) for t in arrayBasic)))
    arrayToUnique = np.array(arrayList)
    print("去重后 \n", arrayToUnique)

    pass


#
# array reshape add. 列数组加行数组
#
def columnAddLine():
    out = np.arange(0, 60, 10).reshape(-1, 1) + np.arange(0, 6, 1)
    print(out)

    pass


#
# buildArray
# 测试学习
#
def buildArray():
    np.set_printoptions(linewidth=100)

    # # range 生成数组
    # print(range(0, 10, 2))
    # # print(range(0, 10, 0.5))
    #
    # # np.arange()
    # print(np.arange(0, 10, 0.5))
    #
    # print(np.linspace.__annotations__)
    #
    # print(np.linspace(0, 10, 10, endpoint=False))
    #
    # print(np.logspace(1, 2, 10, endpoint=False))
    #
    # strTemp = 'abcd'
    #
    # # def logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None,
    # #              axis=0):
    #
    # arrayTemp4 = np.logspace(0, 9, 10, base=3)
    # i = range(0, 10, 2)
    # arrayOut1 = arrayTemp4[i]
    # # 使用整数序列作为索引时，
    # print(arrayOut1)
    # print(arrayTemp4)
    #
    # arrayOut1[0] = 10086
    #
    # print()
    # print(arrayOut1)
    # print(arrayTemp4)

    arrayTemp5 = np.random.rand(10)
    print(arrayTemp5)
    print(arrayTemp5 > 0.6)
    arrayTemp6 = arrayTemp5[arrayTemp5 > 0.6]

    print(arrayTemp6)
    arrayTemp5[arrayTemp5 > 0.6] = 0.6
    print(arrayTemp5)

    pass


#
# debug
#
if __name__ == "__main__":
    # buildArray()

    draw()

    getUniqueArray()

    array = np.arange(0, 60, 10).reshape((-1, 1)) + np.arange(6)
    print(array)
    array.shape = 3, 12
    print(array)

    arrayTemp1 = np.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]], dtype=float)
    arrayTemp2 = np.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]], dtype=complex)

    arrayTemp3 = arrayTemp1.astype(np.int)
    # arrayTemp4 = arrayTemp1.dtype = np.int 出错

    print(arrayTemp1)
    print(arrayTemp2)
    print(arrayTemp3)

    np.set_printoptions(linewidth=80)

    array2 = np.arange(0, 60, 10).reshape((-1, 1))
    array2 = array2 + np.arange(6)

    print(array2)

    pass
