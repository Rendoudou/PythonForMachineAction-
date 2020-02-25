# !/user/bin/python
# -*- coding:utf-8 -*-


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.special import gamma
from scipy.special import factorial


#
# Debug
#
if __name__ == "__main__":
    
    x = np.arange(0.05, 10, 0.015)
    y =  gamma(x)
    plt.plot(x, y, linewidth = 2, color = '#007500', label = 'gamma(x)')

    plt.grid()
    plt.show()

    pass