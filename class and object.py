class Person:
    name = "小甲鱼"


p = Person
p.name

# 使用双下划线是私有变量


class Person:
    __name = "小甲鱼"


p = Person()
p.__name


class Person:
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name


p = Person("小甲鱼")

p.__name
p.getName()

# 类的继承


class Parent:
    def hello(self):
        print("正在调用父类的方法...")


class Child(Parent):
    pass


p = Parent()
p.hello()

c = Child()
c.hello()

# bif 函数


class A:
    pass


class B(A):
    pass


issubclass(B, A)

issubclass(B, B)

issubclass(B, object)


class C:
    pass


issubclass(B, C)

hasattr

# 魔法方法


class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getPeri(self):
        return (self.x + self.y) * 2

    def getArea(self):
        return self.x * self.y


rect = Rectangle(3, 4)
rect.getArea()
rect.getPeri()