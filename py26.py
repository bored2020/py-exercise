#列表推导式
words = ["great","fishc","brilliant","excellent","fantiacs"]
fwords = [w for w in words if w[0] == "f"]#筛选出f开头的单词
fwords
even = [i for i in range(10) if i % 2 == 0]#能够被2整除的数
even
#顺序是先执行for语句再运行后面的表达式
even = [i + 1 for i in range(10) if i % 2 ==0]
even
#列表推导式嵌套
matrix = [[1,2,3],[4,5,6],[7,8,9]]
flatten = [col for row in matrix for col in row]
flatten#将矩阵拆开
#将flatten写成循环的形式
flatten = []
for row in matrix:
    for col in row:
        flatten.append(col)
#外层循环放在外面，内层循环放在里面
flatten
[x + y for x in "fishc" for y in "FISHC"]
#PYTHON中临时变量记为下划线
_ = []
for x in "fishc":
    for y in "FISHC":
        _.append(x + y)
_      
