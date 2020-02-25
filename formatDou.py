"""
# 输出用格式函数
# 测试
"""


#
# 分割线
#
def ALineToDepartData(size : int, strIn : str):

    sizeTemp = int(size)
    strTemp = ""

    for i in range(sizeTemp):
        strTemp += strIn
    print("\n")
    print(strTemp)
    print("\n")

    pass

#
# debug
#
if __name__ == "__main__":

    ALineToDepartData(50,"=")

    pass