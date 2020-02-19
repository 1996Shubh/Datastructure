""" A program Calendar that takes the month and year as command-line arguments and prints the Calendar of the month.
Store the Calendar in an 2D Array,
the first dimension the week of the month and the second dimension stores the day of the week"""

from calander import Calender

"""Creating object for Calender class"""
obj = Calender()
"""Taking input from user"""
while True:
    try:
        year = int(input("Enter the year  :"))
        month = int(input("Enter the month :"))
        if month<=12 and month>=0 and len(str(year))==4:
            break
        else:
            print("Invalid input !!")
    except ValueError:
        print("Invalid input!!")
"""Month dictnoary"""
month_name = {1:"January",2:"February",3:"March",4:"Aprial",5:"May",6:"June",7:"July",8:"Auguest",9:"September",10:"Octomber",11:"November",12:"December"}

cal = obj.month(year,month)
print(f"\n \n Year:{year} Month:{month_name[month]}\n")

"""Printing calender"""
for nums in cal:
    print(nums)