def solve(n):
    a,b = 0 ,1
    for i in range(n):
        a,b = b ,a+b
    return a


solve(5)

solve(10)