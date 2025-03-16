'''
Write a program that outputs whether or not today is a weekday. (The program should be called weekday.py)
You will need to search the web to find how you work out what day it is.
'''
# For this exercise I combined the methods listed out here: 
#https://pynative.com/python-get-the-day-of-week/#:~:text=Get%20the%20Weekday%20Name%20of%20a%20Date%20using%20strftime()%20method,-In%20the%20above&text=For%20example%2C%20datetime(2022%2C,datetime%20in%20a%20string%20format.

import calendar
from datetime import date
import datetime


# get today's date
d = date.today()

# The weekday() method returns the day of the week as an integer, where Monday is 0 and Sunday is 6. 
no = d.weekday()

# if statement where if the result is 0-4 its a weekday as per weekday() and 5-6 is weekend.
if no < 5:
    print("Yes, unfortunately today is a weekday.")
else:  # 5 Sat, 6 Sun
    print("It is the weekend, yay!")

