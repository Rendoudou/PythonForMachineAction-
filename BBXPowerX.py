# !/user/bin/python
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np


#
# x < 0  -x ** -x
# x > 0  x ** x
# 
def xPowerX(inX):
    print(inX > 0) #bool 数组

    y = np.ones_like(inX)
    for i in range(len(inX)):
        if inX[i] > 0:
            y[i] = np.power(inX[i], inX[i])
        if inX[i] < 0:
            y[i] = np.power(-inX[i], -inX[i])
        pass
    return y


#
# debug
#
if __name__ == "__main__":

    x = np.linspace(0.0001, 1.3, 101)
    y = xPowerX(x)

    plt.plot(x, y, 'g-', label='x^x', linewidth=2)
    plt.grid(True)
    plt.legend(loc='upper left')
    plt.show()

    pass
