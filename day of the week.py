#This program tells you what day of the week any day you enter was on
# 0 = monday 1= tuesday 2= wednesday 3= thursday 4= friday 5= saturday 6= sunday
import datetime
import calendar


def findDay(date):
    return (calendar.day_name[day])

month = int(input('Enter month:'))
day = int(input('Enter day:'))
year = int(input('Enter year:'))

datestr = datetime.datetime(year,month,day)

day = datestr.weekday()

print(day)
