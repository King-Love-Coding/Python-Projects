# Program to display calendar of the given month and year
import calendar
# yy = 2014
# mm = 11
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))
print(calendar.month(yy, mm))
