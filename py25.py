oho = [1,2,3,4,5]
oho = [i * 2 for i in oho]
oho
x = [i for i in range(10)]
x
x = [i+1 for i in range(10)]
x
y = [c*2 for c in "fishc"]
y
#ord是将字符串转化为编码的内置函数
code = [ord(c) for c in "fishc"]
code
#提取出第二列
matrix = [[1,2,3],
         [4,5,6],
         [7,8,9]]
col2 = [row[1] for row in matrix]
col2
#获取对角线元素
diag = [matrix[i][i] for i in range(len(matrix))]
diag