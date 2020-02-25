# !/user/bin/python
# -*- coding:utf-8 -*-

import math
import matplotlib.pyplot  as plt
import numpy


#
# Debug
#
if __name__ == "__main__":
    
    # 曲线1
    x = numpy.arange(0.05, 3, 0.05)
    y1 = [math.log(a, 1.5) for a in x]
    plt.plot(x, y1, linewidth = 2, color = '#007500', label = 'log1.5(x)')
    plt.plot([1,1], [y1[0], y1[-1]], "r--", linewidth = 2)  # 画竖线
    
    # 曲线2
    y2 = [math.log(a, 2) for a in x]
    plt.plot(x, y2, linewidth = 2, color = '#9f35ff', label = 'log2(x)')

    # 曲线3
    y3 = [math.log(a, 3) for a in x]
    plt.plot(x, y3, linewidth = 2, color = '#f75000', label = 'log3(x)')

    plt.grid(True)
    plt.show()
    
    pass