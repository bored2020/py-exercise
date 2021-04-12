i = 0
while i < 10 :
    i += 1
    if i % 2 ==0:
        continue
    print(i)

i = 1
while i < 5 :
    print("循环内，i的值是",i)
    i += 1
else:
    print("循环外，i的值是",i)


i = 1
while i <= 9:
    j =1
    while j <= i:
        print(j,"*",i,"=",i*j,end=" ")
        j += 1
    print()
    i += 1

day = 1
hour = 1
while day <= 7:
    while hour <= 8:
        print("今天我要学习八个小时")
        hour += 1
        if hour > 1:
            break
    day += 1
    