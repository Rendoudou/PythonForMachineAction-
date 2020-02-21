"""
# Python学习 类
# editor doudou
# data 21 02 2020
# ver 01 初次学习，抄录编辑。0221
"""


#
# 把一个类作为一个迭代器
# 类 class: templated
#
class MyNumbers:
    # 共有属性
    record = 0
    # 私有属性
    __height = 0
    __width = 0

    # def __init__(self, *args):
    #    pass

    def __init__(self, heightIn, widthIn, recordIn):  # 构造方法,self代表类的实例而非类

        print("创建中...")
        self.__height = heightIn
        self.__width = widthIn
        self.record = recordIn
        print("创建完毕...")
        pass

    # 类方法
    @classmethod
    def constructClass(cls):
        print("创建中...")
        return cls(0, 0, 0)  # 调用主构造函数

    # 类的方法与普通的函数只有一个特别的区别——它们
    # 必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。

    def __iter__(self):
        self.record = 1
        return self

    def __next__(self):
        x = self.record
        self.record = self.record + 1
        return x

    def prtSelf(self):
        print("self: ", self)  # self 代表的是类的实例，代表当前对象的地址
        print("class: ", self.__class__)  # self.class 则指向类
        pass

    pass


#
# 类的继承 父类
#
class LiveAnimal:
    # __magicVolume = 0  # 蓝量
    __bloodVolume = 0  # 血量
    __specieName = " "  # 种族名
    __basicHeight = 0  # 基本（正常）高度
    __basicWidth = 0  # 基本（正常）宽度
    __basicLifeSpan = 0  # 基本寿命
    __basicAttack = 0  # 基础攻击力
    __basicDefensivePower = 0  # 基本防御力
    __destroyAble = True  # 可以破坏

    # 构造函数
    def __init__(self, *args):

        if (type(args) == list) & (len(args) >= 7):
            self.__bloodVolume = int(args[0])
            self.__specieName = str(args[1])
            self.__basicHeight = int(args[2])
            self.__basicWidth = int(args[3])
            self.__basicLifeSpan = int(args[4])
            self.__basicAttack = int(args[5])
            self.__basicDefensivePower = int(args[6])
        else:
            print("init error...")
        pass

    # 析构函数
    def __del__(self):
        print(f'{self.__specieName} die...')
        pass

    # 类方法
    @classmethod
    def constructClass(cls):
        return cls([0, "unknown", 0, 0, 0, 0, 0])
        pass

    def getSpecieName(self):
        return self.__specieName

    pass


#
# 类继承 子类
#
class PeopleNpc(LiveAnimal):
    # 私有变量
    __destroyAble = False

    # 构造函数
    def __init__(self, *args):

        if (type(*args) == list) & (len(*args) == 7):
            super().__init__(*args)
        else:
            print("init error")
        pass

    pass

