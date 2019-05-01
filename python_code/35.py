import datetime

def dayofyear():
    year=int(input("请输入年份："))
    month=int(input("请输入月份："))
    day=int(input("请输入天："))
	
    target = datetime.date(year, month, day)
    date = target - datetime.date(target.year-1,12,31)
    print("%s是 %s年的第%s天 "%(target,year,date.days))

if __name__=="__main__":
	print(dayofyear())