# encoding=utf8

# 函数的定义：
# 格式：  def就是用来定义一个函数的 (def其实是英文里的definition的缩写，就是定义的意思)

# 定义函数
def my_first_function(x, y, z):
	print("hi, this is my first function, it receives 3 arguments")
	print("the arguments is", x, y, z)
	print("byebye...")

# xz，就自己定义好了一个叫做my_first_function的函数了，
# 然后，就可以用 函数名(参数)  的方式调用它了

# 调用函数
my_first_function(1, 2, 3)
my_first_function("how", "are", "you")

# 哎，window上面的中文总是会出现乱码问题。。。


# 再举个例子
# 之前有学过print函数
# 现在，我们可以基于print函数定义一个自己的my_print函数，
# 里面的功能就是在每个原来的print的后面加一句话
def my_print(x):
	x = x + " -> this is from my_print"
	print(x)

my_print("test my_print")	

# 工作的时候，其实就是在定义各种函数，然后在调用各种函数



