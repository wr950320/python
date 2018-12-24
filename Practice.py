# encoding=utf8

# import这一句只需要在开头写一次就行了，就导入进来了，后面直接使用就行
import webbrowser 


# 在python中，以4个空格表示一个层级的缩进


def print_4_sentence():
    print("1: watch the news ")
    print("2: listen to music")    
    print("3: shopping")
    print("4: Watch videos")

print_4_sentence()

choice = raw_input("please choose from 1/2/3/4: \n")

if choice == "1":
    def print__3__sentence():
        print("1.1m.baidu.com")
        print("1.2m.sohu.com")
        print("1.3news.qq.com")

    choice = raw_input("please choose from 1.1/1.2/1.3: \n")

    if choice == "1.1":
        webbrowser.open("m.baidu.com")
    elif choice == "1.2":
        webbrowser.open("m.sohu.com")
    elif choice == "1.3":
        webbrowser.open("news.qq.com")


if choice == "2":   
    def print__3__sentence():
        print("2.1h.xiami.com")
        print("2.2music.baidu.com")
        print("2.3mucic.163.com")

    choice = raw_input("please choose from 2.1/2.2/2.3: \n")

    if choice == "2.1":
        webbrowser. open("h.xiami.com")
    elif choice == "2.2":
        webbrowser.open("music.baidu.com")
    elif choice == "2.3":
        webbrowser.open("mucic.163.com")


if choice == "3":
    def print__3__sentence():
        print("3.1m.taobao.com")
        print("3.2m.jd.com")
        print("3.3m.vip.com")

    choice = raw_input("please choose from 3.1/3.2/3.3: \n")

    if choice == "3.1":
        webbrowser. open("m.taobao.com")
    elif choice == "3.2":
        webbrowser.open("m.jd.com")
    elif choice == "3.3":
        webbrowser.open("m.vip.com")


if choice == "4":
    def print__3__sentence():
        print("4.1m.v.qq.com")
        print("4.2m.video.baidu.com")
        print("4.3youku.com")

    choice = raw_input("please choose from 4.1/4.2/4.3: \n")

    if choice == "4.1":
        webbrowser. open("m.v.qq.com")
    elif choice == "4.2":
        webbrowser.open("video.baidu.com")
    elif choice == "4.3":
        webbrowser.open("youku.com")




# ok了
# 写的很ok
# 可以的


# 关于这个4个空格的意思，再举个例子：
def test_space():
    a = 0
    if a > 0:
        print("a > 0")
        if 0 < a < 10:
            print("0 < a < 10")
                if 10 < a < 20:
                    print("10 < a < 20")
# 可以选中这一段就可以看到里面的空格数了
# 在python中，以4个空格表示一个层级的缩进
# 懂吧 嗯 ok



































