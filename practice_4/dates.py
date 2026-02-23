#1
import datetime
today = datetime.date.today()
five_days_ago = datetime.date.fromordinal(today.toordinal() - 5)
print(today)
print(five_days_ago)
#2
today = datetime.date.today()
yesterday = datetime.date.fromordinal(today.toordinal() - 1)
tomorrow = datetime.date.fromordinal(today.toordinal() + 1)
print(today)
print(yesterday)
print(tomorrow)
#3
import datetime
x = datetime.datetime.now()
print(x.strftime("%x %X"))
#4
d1 = datetime.date.fromisoformat(input())
d2 = datetime.date.fromisoformat(input())
days = abs(d2.toordinal()- d1.toordinal())
seconds = days*24*60*60
print(seconds)
