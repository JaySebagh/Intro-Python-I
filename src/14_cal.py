"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

month = input("Month: ")
year = input("Year: ")

currY = datetime.now().year
currM = datetime.now().month

def cal():
  if len(month) == 0 and len(year) == 0:
    print(calendar.month(currY, currM))
  elif len(month) > 0 and len(year) == 0:
    m = int(month)
    print(calendar.month(currY, m))
  elif len(month) > 0 and len(year) > 0:
    m = int(month)
    y = int(year)
    print(calendar.month(y, m))
  elif len(month) == 0 and len(year) > 0:
    print("Error: Month Required")
cal()

# def cal():
#   if month == "" and year == "":
#     print(calendar.month(currY, currM))
#   try:
#     int(month) and len(year) > 0
#   except:
#     print("Error: Expected Month")
#   else:
#     m = int(month)
#     print(calendar.month(currY, m))
    
# cal()