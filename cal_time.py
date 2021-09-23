"""
Calendar Module
The calendar module allows you to output calendars and provides additional useful functions for them.

class calendar.TextCalendar([firstweekday])

This class can be used to generate plain text calendars.
"""
import calendar
"""
print(calendar.TextCalendar(firstweekday=6).formatyear(2021))
"""
n1,n2,n3 = map(int,input().split())
print(list(calendar.day_name)[calendar.weekday(n3, n1, n2)].upper())