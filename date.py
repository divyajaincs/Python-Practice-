import time;
import calendar;
ticks=time.time()
print("no of ticks",ticks)
print(time.localtime())
localtime=time.localtime(time.time())
print("Local time:",localtime)
localtime1=time.asctime(time.localtime(time.time()))
print("current time:",localtime1)
cal=calendar.firstweekday()
print("Calender is here:\n",cal)
