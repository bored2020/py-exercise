# 序列

[1, 2, 3] + [4, 5, 6]

(1, 2, 3) + (4, 5, 6)

"123" + "456"

s = [1, 2, 3]

id(s)

s *= 2

s

id(s)

#  唯一标志的整数值，在Python中每个对象的唯一特征

t = (1, 2, 3)

id(t)

t *= 2

t
id(t)

# is 和 is not 检测对象id值是否相等

x = "FishC"
y = "FishC"
x is y

# in 和 not in 是包含问题

"鱼" in "鱼C"

"FISH" in "FISHC"

x = "FishC"
y = [1, 2, 3]
del x, y

x
y

x = [1, 2, 3, 4, 5]
del x[1:4]
x

# 切片语法
y = [1, 2, 3, 4, 5]
y[1:4] = []
y
# 将一个空列表赋值给指定的区域
