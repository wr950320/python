# encoding=utf8

# 循环语句
# 上次讲 数据类型的时候， 最后讲了2个复合类型的，也就是里面有多个值的，
# list 和 dict， 记得吧

l1 = [1, 2, 3, 4, 5]
m1 = {"name": "xxx", "age": 24, "salary": 10000}

# 所谓的 循环， 就是循环这2样东西，把里面的值一项一项的读取一次，直到最后一个
# 循环的写法就是:
# for i in xxx:
# 	print(i)

# 例子1： 循环打印l1里面的每一项
for i in l1:
	print(i)
# 例子2： 循环打印m1里面的每一项（Key:Value）

# 只打印key
for j in m1:
	print(j)

# 打印key:value
for k, v in m1.items():  #这个.的写法你暂时还不知道，后面再说
	print(k, v)


# 现在，上面的代码会 循环打印 l1, m1里面的每一项了


