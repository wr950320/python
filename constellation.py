#encoding=utf8

# 写个程序，用户输入自己的生日，
# 然后告诉她，星座是什么，有什么性格。
# 比如：
# 请输入年：
# 请输入月：
# 请输入日：
# 您的生日是...
# 您的星座是...
# 您的性格可能是...

# 星座和月份和天有关系
# 先判断月份1-12
# 再根据不同月份判断不同的天的范围，确定星座

# 白羊座(3.21-4.20)
# 金牛座(4.21-5.20)
# 双子座(5.21-6.21)
# 巨蟹座(6.22-7.22)
# 狮子座(7.23-8.22)
# 处女座(8.23-9.22)
# 天秤座(9.23-10.22)
# 天蝎座(10.23-11.21)
# 射手座(11.22-12.21)
# 摩羯座(12.22-1.19)
# 水瓶座(1.20-2.18)
# 双鱼座(2.19-3.20)

month=raw_input("Please put your month here \n: ")
day=raw_input(" Please put your day here\n: ")

# ****************************
# 同类型的才能比较大小或是否相等
# ****************************

# month不需要转换了，因为你后面是和字符串类型比较的
# month = int(month)

# 但day还是需要转换的，因为后面是和整数比较的

day=int(day)
print("constellation and character is:")

if month == "1":
    if day < 20:
        print("your constellation is:mojie")
        print("your character is:wisdom")

elif month == "2":
    if day < 19:
        print("your constellation is:shuiping")
        print("your character is:attractive")
    else:
        print("your constellation is: shuangyu")
        print("your character is: emotional")
    
elif month == "3":
    if day < 21:
        print("your constellation is: shuangyu")
        print("your character is: emotional")
    else:
        print("your constellation is:baiyang")
        print("your character is: enthusiastic")

elif month == "4":
    if day < 21:
        print("your constellation is:baiyang")
        print("your character is: enthusiastic")
    else:
        print("your constellation is:jinniu")
        print("your character is: sensual")


elif month == "5":
    if day < 21:
        print("your constellation is:jinniu")
        print("your character is: sensual")
    else:
        print("your constellation is:shuangzi")
        print("your character is: intellectual")


elif month == "6":
    if day < 22:
        print("your constellation is: shuangzi")
        print("your character is:intellectual")
    else:
        print("your constellation is:juxie")
        print("your character is: complicated")

elif month == "7":
    if day < 23:
        print("your constellation is: juxie")
        print("your character is: complicated")
    else:
        print("your constellation is:shizi")
        print("your character is: warm")

elif month == "8":
    if day < 23:
        print("your constellation is: shizi")
        print("your character is: warm")
    else:
        print("your constellation is:chunv")
        print("your character is: introvert")


elif month == "9":
    if day < 23:
        print("your constellation is: chunv")
        print("your character is: introvert")
    else:
        print("your constellation is:tianping")
        print("your character is: kind")

elif month == "10":
    if day < 23:
        print("your constellation is: tianping")
        print("your character is: kind")
    else:
        print("your constellation is:tianxie")
        print("your character is: mysterious")

elif month == "11":
    if day < 22:
        print("your constellation is: tianxie")
        print("your character is: mysterious")
    else:
        print("your constellation is:sheshou")
        print("your character is: optimistic")


elif month == "12":
    if day < 22:
        print("your constellation is: sheshou")
        print("your character is: optimistic")
    else:
        print("your constellation is:mojie")
        print("your character is: wisdom")











# 基础还没掌握好

















