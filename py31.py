"    左侧不要留白".lstrip()

"右侧不要留白     ".rstrip()

"   两边都不要留白    ".strip()

# chars参数，

"www.lovefishc.com".lstrip("www.")

# 去除传入的chars参数

"www.lovefishc.com".strip("wcom.")

# 按照单个字符为单位进行去除



# 去掉指定的字符串

"www.ilovefishc.com".removeprefix("www.")
"

# 拆分和拼接

"www.ilovefishc.com".partition(".")
# 从左到右找到参数分割的

"ilvoefishc.com/python".rpartition("/")

# 从右向左找分隔符

#split 
"苟日新，日日新，又日新".split()
"苟日新，日日新，又日新".split(",")
"苟日新，日日新，又日新".rsplit(",")
"苟日新，日日新，又日新".split("，",maxsplit=1 )

#使用换行符分割

"苟日新\n日日新\n又日新".split('\n')

"苟日新\r日日新\r 又日新".splitlines()


"苟日新\r日日新\r 又日新".splitlines(True)


# 
".".join(["www","ilovefishc","com"])

"."


year = 2010
"成立于{}年".format(year)

# 输出花括号

"{},{},{}".format(1,"{}",2)