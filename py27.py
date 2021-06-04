# 元组,元组就是被阉割的列表？

#元组使用圆括号

rhyme = (1, 2, 3, 4, 5, '上山打老虎')
rhyme

rhyme = 1, 2, 3, 4, 5, '上山打老虎'
rhyme

rhyme[0]
rhyme[-1]

#元组内容不可变，无法修改元组内容

rhyme[1] = 10

# 元组支持切片

rhyme[3:]

# 元组 只能查

nums = (1, 3, 4, 5, 6, 1, 5, 3, 5, 6, 7)

nums.count(3)  #数出nums中3的元素有几个

heros = ("蜘蛛侠", "绿巨人", "黑寡妇")
heros.index("黑寡妇")  #获得黑寡妇的下标符

#元组可以使用+ *
s = (1, 2, 3)
t = (4, 5, 6)
s + t
s * 3

# 元组可以嵌套,可以使用循环来对元组中的元素进行操作。

w = s, t
w

for each in s:
    print(each)

for i in w:
    for each in i:
        print(each)

# 元组可以使用列表推导式

s = (1, 2, 3, 4, 5)
[each * 2 for each in s]

# 但是将方括号改为圆括号就不行了

(each * 2 for each in s)

# 圆括号的必要性
# 最好一直加上圆括号

# 生成只有一个元素的元组

x = (520)
x
type(x)

# 必须这么写
x = (520, )
type(x)

# 打包操作
t = (123, "fishc", 3.14)
t

# 解包操作
x, y, z = t
x
y
z

# 解包操作
# 左边的元素数量必须和右边的元素数量一样

a, b, c, d, e = "FishC"
a
b
c

# pytho底层功能实现是通过打包解包

x, y = 10, 20
x

_ = (10, 20)
x, y = _
x
y