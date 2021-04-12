for each in "FISHC":
    print(each)
# TODO: write code...
while i < len(fishc):
    print("fishc"[i])
    i += 1

sum = 0
for i in range(10000001):
    sum += i
print(sum)

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "=", x, "*", n // x)
            break
    else:
        print(n, "是一个素数")
