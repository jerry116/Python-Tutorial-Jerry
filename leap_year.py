#coding=utf-8
def is_leap_year(i):
    if i == 0:
        print "年不能是0"
    elif i%400 == 0:
        print i,"是闰年"
    elif (i%4 == 0) and (i%100 != 0):
        print i,"是平年"
    else:
        print i, "是平年"

str1 = input("请输入您要检测的年份：")
str = str(str1)
while str.isdigit() == 0:
    str = input("您输入的非纯数字，请重新输入：")
yea = int(str)

is_leap_year(yea)