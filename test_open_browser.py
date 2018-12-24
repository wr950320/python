# encoding=utf8

# 写个小程序示例一下上次学的一些概念
# 这个程序的功能就是：
# 根据用户输入的值，来选择打开不同的网站


# 这一句是导入一个别人写好的函数直接来使用
# 导入open函数，它的参数就是网址，功能是调用本地的浏览器打开一个网站
from webbrowser import open

# 打印3个选项给用户选择输入
# 定义个函数，里面打印3句话
def print_3_sentence():
	print("A: www.baidu.com")
	print("B: www.jd.com")	
	print("C: www.taobao.com")
	print("") #打印个空行

print_3_sentence()

# choice是个变量，接受用户输入的值
choice = raw_input("please choose from A/B/C: \n")

# 把上次学的条件语句也加进来
# 选择不同的字母，打开不同的网站
if choice == "A":
	open("www.baidu.com")
elif choice == "B":
	open("www.jd.com")
elif choice == "C":
	open("www.taobao.com")
else:
	# 不是A/B/C时默认打开谷歌
	open("www.google.com")

# 本实例里面用到了上次学的 
#     变量+函数+条件语句
# 也对应了程序的本质：
#     输入 => 处理 => 输出 模型

# 好好体会下吧
# 自己改一改，双击该文件运行，输入，查看打开的网站，
# 

# byebye

# 导入open函数，它的参数就是网址，功能是调用本地的浏览器打开一个网站
from webbrowser import open

def print_3_sentent():
	print("1:m.v.qq.com")
	print("2:m.iqiyi.com")
	print("3:m.tv.sohu.com")

print_3_sentent()

choice = raw_input("please choose from 1/2/3: \n")

if choice == "1":
    open("m.v.qq.com")
elif choice == "2":
	open("m.iqiyi.com")
elif choice == "3":
	open("m.tv.sohu.com")
else:
	open("youku.com")


# 这个会了吗？嗯











