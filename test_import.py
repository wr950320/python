# encoding=utf8

# 上次那个 import 的意思就是：导入别人写好的python库，
# 所谓 ‘库’的意思，就是说：
# 你在开发的时候，并不是所有的功能都要你自己去写的，那会累死的...
# 所以，基本上你能想到的所有的功能，都会有对应的库已经写好了,
# 然后我们只需要导入某个库，然后就可以直接使用它里面的函数了

#   一个python文件其实就可以作为一个库了
#     单个文件作为库就很简单了，就一个python文件而已

# 举个例子：我们写个库试试
# XX库是个python文件，里面放有一个变量XX1和函数XX2

# 从库里面导入变量和函数来使用的写法就是  import

# 简单一点，之导入库的名字，然后，里面的东西直接使用.来引用
# 就写个import，然后使用.来导入里面的东西


import wo_de_ku     #导入XX库，XX库就是那个XX.py文件的意思，那个文件作为一个库
print(wo_de_ku.XX1) #用.来使用XX库中的XX1


# 
# 上面的例子和下面的例子的 本质是一样的,都是 import 的用法
# 

# 上次使用了 webbrowser库里面的open函数，记得不
# import webbrowser   # 导入webbrowser库
# webbrowser.open("www.baidu.com")  #使用.来使用它里面的open函数
# open函数的功能就是调用浏览器打开一个网址啊



# 库也叫模块，就是别人写好的代码，然后你可以导入到你的代码里来用的意思。
# 基本上各种功能都是写好了后，以库/模块的形式提供给别人使用的.
# 比如上面的webbrowser就是一个别人写好的库，专门用来调用本地浏览器的.

# 理解下啊

# 再举个例子，
# 导入使用一个专门做桌面程序的库/模块/包
# 这个库的名字叫wx

import wx  #导入wx库

# 调用wx库里面的各种函数，变量来实现桌面程序的功能
app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "hi, it's a window...")

path_text = wx.TextCtrl(frame,pos = (50,5),size = (100,50))
open_button = wx.Button(frame,label = "点我试试",pos = (80,60),size = (50,20))

def openfile(event):     
    your_input = path_text.GetValue()
    wx.MessageBox(your_input, "你好，美女")

open_button.Bind(wx.EVT_BUTTON, openfile)

frame.Show(True)
app.MainLoop()

# 好玩不。。。反正就是各种库的使用，非常方便。。
# 要什么功能，有什么功能，随意调用。
#牛逼


# ******************************************************
# 上网查询各种库的使用文档，示例，照着写，就这么简单。。。
# 这个能力很重要
# ******************************************************


# ok啦
# 以上示例就是使用了wx库/模块来写了个小桌面程序了。
# 其实我们的代码做的事情没什么，就是各种调用它的=东西而已。。。

# 写代码就是这样，不停的使用各种库/模块来实现自己的程序。


# byebye


# 昨天这个import懂了吗
# 嗯
















