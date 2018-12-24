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

number1 = raw_input("please put your first number here:  ")
number2 = raw_input("please put your second number here:  ")
operator = raw_input("please put your operator(+-*/) here:  ")

# 用户输入进来的默认是 字符串类型，需要转换成 数字类型,
# 因为数字类型 才能做加减乘除 操作
number1 = int(number1)
number2 = int(number2)

print("result is:")

if operator == "+":
	print(number1 + number2)

elif operator == "-":
	print(number1 - number2)

elif operator == "*":
	print(number1 * number2)

elif operator == "/":
	print(number1 / number2)			

else:
	print("please choose from +-*/ !")


# 明白不
#嗯
# 好，自己写一遍，





































