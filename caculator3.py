# encoding=utf8
#写一个人生计算器，输入出生年月日，算出你活了多久，还能活多久（人的寿命是80年）
#人生剩下百分之多少（一年365天，一月30天）



    
year=raw_input("year: ")
month=raw_input("month: ")
day=raw_input("day: ")
operator = raw_input("operator: ")

year=int(year)
month=int(month)
day=int(day)

print("result is:")

def my_first_value(a=2018-year):
if operator == "-":
     print(2018 - year)
        elif operator == "*":
            print(a * 365)
       
def my_second_value(b=11-month):
if operator == "-":
    print(11 - month)       
        elif operator == "*":
            print(b * 30)
       
def my_third_value(c=10-day):
if operator == "-":
    print(10 - day)

    


    
     
     
     









































