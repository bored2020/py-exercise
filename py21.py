heros = ["钢铁侠", "绿巨人"]
heros.append("黑寡妇")
heros
heros.extend(["eagleeys", "thanos", "thunder"])
heros
s = [1, 2, 3, 4, 5]
#切片方法
s[len(s):] = [6]
s
s[len(s):] = [7, 8, 9]  #等同于s.extend([7,8,9])
s
#insert方法
s = [1, 3, 4, 5]
s.insert(1, 2)  #第一个是位置，第二个是插入的数值
s
s.insert(len(s), 6)  #在末尾插入
s
#删除
heros.remove("thanos")
heros
heros.remove("jinglian")
heros.pop(2)  #删除具体位置的元素
heros
heros.clear()  #全部删除
