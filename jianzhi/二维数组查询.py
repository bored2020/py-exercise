# 二维数组中的查找，在一个二维数组中，每一行按从左到右的升序排序，每一列按从上到下的升序排序，完成一个函数，输入一个整数，判断二维数组中是否含有这个函数。



from typing import List


class Solution:
    def findnumber(self,matrix:List[List[int]],target:int)-> bool :
        i , j =len(matrix) - 1 ,0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] > target : i-= 1
            elif matrix[i][j] < target : j += 1
            else:return True
        return False



data =  [[1,2,3,4],[5,6,10,11],[13,14,15,16]]

data

s = Solution()

s.findnumber(matrix= data,target=4)

