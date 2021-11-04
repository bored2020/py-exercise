from _typeshed import Self


class Solution:
    def minaraay(self,numbers: [int])-> int :
        i, j  = 0 ,len(numbers) - 1
        while i < j :
            m = (i + j ) // 2
            if numbers[m] > numbers[j] : i = m + 1
            elif numbers[m] < numbers[j] : j = m 
            else: j -= 1
        return numbers[i]


s = Solution()

s.minaraay([3,4,5,1,2,3])
 

data = [1,2,3,4,5,9,8]

data.append(10)

data


data.pop()

data


data2  = list([1,2,3,4,5])

data2

data2.insert(1,1)
data2

data2[-1]