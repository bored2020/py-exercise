#list 
s = [1,2,3]
t = [4,5,6]
s+t
s*3#将s中的元素按之前的排序重复三次
matrix=[[1,2,3],[4,5,6],[7,8,9]]#嵌套列表
#访问嵌套列表
for i  in matrix:
    for each in i:
        print(each)
for i in matrix:
    for each in i:
            print(each,end=' ')
    print()
matrix[0]
matrix[1][1]#访问第二行第二列


# 创建二维列表
A=[0]*3
A
for i in range(3):
    A[i]=[0]*3
A

#is 运算符
x= "fishc"
y= "fishc"
y is x
#字符串存储相同
a=[1,2,3]
b=[1,2,3]
a is b
#列表存储不同
A[0] is A[1]
#A的第一行和第二行不是同一个对象
B=[[0]*3]*3
B[0] is B[1]
B[1] is B[2]