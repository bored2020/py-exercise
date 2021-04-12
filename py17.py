love = "yes"
while love == "yes":
    love = input("今天你还爱我吗")
i = 1
sum = 0
while i <= 10000:
    sum = sum + i
    i += 1

print(sum)

# break语句
while True:
    answer = input("主人，我可以推出循环了吗")
    if answer == "可以":
        break
    print("哎，好累····") 