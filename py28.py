# 字符串

# 判断一个整数是否为回文数字

x = "12321"
# 字符串说到底是序列
"是回文数" if x == x[::-1] else "不是回文数"
x = "i love Fishc"
x.capitalize()
x.casefold()
x.title()
x.swapcase()
x.upper()
x.lower()

x = "有内鬼，终止交易"
x.center(5)
x.center(15)
x.ljust(15)
x.rjust(15)
x.zfill(15)

"520".zfill(5)

x.center(15, "干")
