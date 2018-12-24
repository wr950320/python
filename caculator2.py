# encoding=utf8


#*******************************************************************
#写个计算机程序：先让用户输入3项：值1，值2，计算操作(+-*/)
# 先说个东西：
# 之前有学过基本数据类型，其中包括 字符串/数字 这2个
# 而 字符串和数字是可以转换的，
# 比如 字符串"12" 可以转换成 数字12，或者 数字12 可以转换成 字符串"12"
# 转换的方法就是 使用2个函数,
# 数字转成字符串用 str()， 字符串转成数字用 int()
# 比如：
print str(12) == "12"
print int("12") == 12
# 明白不？
#嗯
# 
# 基于这个就可以写计算器了

#写个计算机程序：先让用户输入3项：值1，值2，计算操作(+-*/)

# 写吧
number1 = raw_input("number 1:  ")
number2 = raw_input("number 2:  ")
operator = raw_input("operator:  ")

number1 = int(number1)
number2 = int(number2)
print ("result:")

if operator == "+":
    print(number1 + number2)  #这里不能加 ""在外面，这样的话就是打印个字符串出来了，而不是计算值了
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    print(number1 / number2)
else:
	print("must choose from： +-*/ !")


# 你的错误是：
print(1+2)  #打印  3
# 和
print("1+2") #打印  1+2
# 是不一样的



#尽量写英文。。。





























