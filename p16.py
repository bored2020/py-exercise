age = 16
if age < 18:
    print("低于18岁禁止访问")
else:
    print("欢迎")
age = 16
print("低于18岁禁止访问") if age < 18 else print("欢迎")
a = 3
b = 5
if a < b:
    small = a
else:
    small = b
small

a = 3
b = 5
small = a if a < b else b
small

score = 66
level = ('D' if 0 <= score < 60 else
         'C' if 60 <= score < 80 else 'B' if 80 <= score < 90 else
         'A' if 90 <= score < 100 else 'S' if score == 100 else "请输入0~100的分值")
print(level)

age = 18
isMale = True
if age < 18:
    print("未满18岁，禁止访问")
else:
    if isMale:
        print("任君选购")
    else:
        print("本店向男性开放")