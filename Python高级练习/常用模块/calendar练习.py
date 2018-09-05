import calendar

#输出日历
#l每行间隔字符数
#w每个日期间隔字符数
#c每个月间隔字符数
#m一行显几个月
a = calendar.calendar(2018,l=1,w=1,c=1)
print(a)

#isleap,判断闰年
bol = calendar.isleap(2018)
print(bol)

#leapdays,两个年份之间闰年个数
num = calendar.leapdays(2000,2018)
print(num)

#manth,月份日历
print(calendar.month(2018,9))

#monthrange,获取某个月第一天是周几,有几天,0代表周一
print(calendar.monthrange(2018,9))

#monthcalendar,返回一个月的矩阵列表list
for i in calendar.monthcalendar(2018,9):
    print()
    for j in i:
        print(str(j).rjust(3," "),end=" ")

#prcal 直接打印日历不需要print
#输出日历
#l每行间隔字符数
#w每个日期间隔字符数
#c每个月间隔字符数
#m一行显几个月
calendar.prcal(2018,m=2)

#prmonth 打印月份不需要print
calendar.prmonth(2018,9)

#weekday获取某天是星期几
print(calendar.weekday(2018,9,10))

