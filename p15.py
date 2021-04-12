# 分支和循环
if 3 >= 5:
    print("我在里面")
    print("我也在里面")
print("我在外面")

if "小甲鱼" == "小姐姐":
    print("小甲鱼是小姐姐")
else:
    print("小甲鱼不是小姐姐")

# 根据用户输入的分数输出等级
score = input("你的分数")
score = int(score)

if 0 <= score < 60:
    print("D")
elif 60 <= score < 80:  # 这里使用elif来表示 else if
    print("C")
elif 80 <= score < 90:
    print("B")
elif 90 <= score < 100:
    print("A")
elif score == 100:
    print("S")

# 第四种情况实在第三种的情况下添加一个else，表示上面所有的条件
# 均不成立的情况下，执行某条语句或某个代码块
score = input("你的分数")
score = int(score)

if 0 <= score < 60:
    print("D")
elif 60 <= score < 80:  # 这里使用elif来表示 else if
    print("C")
elif 80 <= score < 90:
    print("B")
elif 90 <= score < 100:
    print("A")
elif score == 100:
    print("S")
else:
    print("请输入 0~100的分值")