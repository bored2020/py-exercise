x = "上海自来水来自海上"

x.count("海")

x.count("海", 0, 5)
# 指定起始位置和终止位置进行查找出现的次数

# 查找具体字的下标

x.find("海")
#从左向右查找，返回第一个出现的下标

x.rfind("海")

# 从右往左查找

x.find("鱼")

x.rfind("鱼")

x.index("鱼")

# 字符串替换的方法
code = """
        print("i lvoe fishc")
    print("i love my wife)"""
code
newcode = code.expandtabs(4)
newcode

# 替换字符串  replace

"在吗，我在你家楼下，快点下来！！".replace("在吗", "想你")

# 使用替换


# 使用转换表格,相当于是制造了一个字典


table = str.maketrans("ABCDEFG","1234567")
"i love FishC".translate(table)

"i love FishC".translate(str.maketrans("ABCDEFG","1234567"))


"i love FishC".translate(str.maketrans("ABCDEFG","1234567","love"))
