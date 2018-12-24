# encoding=utf8

def tips_for_money_exchange():
    print("Dollar exchange rate: 6.9432")
    print("Euro exchange rate: 7.9111")    
    print("Pound exchange rate: 8.9026")
    print("Yen exchange rate: 0.06155")

tips_for_money_exchange()

number = raw_input("please put your number here: \n") 
choose= raw_input("please put your choose here: \n") 

number = int(number)

print("result is:")

if choose == "Dollar exchange rate":
    print(number*6.9432)
elif choose == "Euro exchange rate":
    print(number*7.9111)
elif choose == "Pound exchange rate":
    print(number*8.9026)
elif choose == "Yen exchange rate":
    print(number*0.06155)

# 可以的
# 写的蛮好
# 说一点：
#   函数名字可以自己起啊，不必每次一样的

































