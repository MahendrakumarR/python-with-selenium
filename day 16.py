
# Date Format

"""
Under which module are Date functions available?

    Date functions are available in the datetime module.

Is datetime a class?

    Yes, datetime is a class within the datetime module.

What is the default date format?

    The default date format is YYYY-MM-DD.

What are methods available in the datetime class?

    Methods include now(), today(), strptime(), strftime(), fromtimestamp(), and more.

What is the purpose of the now() method?

    now() returns the current local date and time.

What is the purpose of the strftime() method?

    strftime() formats dates according to a specified format string.

What is the difference between %Y and %y?

    %Y gives the full year (e.g., 2023), while %y gives the last two digits of the year (e.g., 23).

What is the difference between %B and %b?

    %B provides the full month name (e.g., "October"), whereas %b gives the abbreviated month name (e.g., "Oct").

Is it possible to pass a date as a constructor?

    Yes, you can pass a date to the datetime class constructor.

How many parameters are needed for the datetime() class?

    datetime() requires 3 main parameters: year, month, and day.

What is the type of datetime.now() and datetime(2020,3,12)?

    Both are of type datetime.datetime.

"""
"""
QUESTION 1:
------------
Description : print the Current Date and time 

"""
print("============= print the Current Date and time =============")

from datetime import datetime

c = datetime.now()

print("print the Current Date and time :",c)  # print the Current Date and time : 2024-11-02 05:48:08.060458

"""
QUESTION 2:
------------
Description : print the Current Date and time and Below format
              
              Print Year in format -->2020
              Print Year in format -->20

"""
print("============= print the Current Date and time and Below format =============")

from datetime import datetime

c1 = datetime.now()

print("print the Year in full format :",c1.strftime("%Y"))  # print the Year in full format : 2024
print("print the Year in short format :",c1.strftime("%y")) # print the Year in short format : 24

"""
QUESTION 3:
------------
Description : print the Current Date and time and Below format
              
              Print month in format -->June
              Print month in format -->Jun

"""
print("============= print the Current Date and time and Below format =============")

c2 = datetime.now()

print("Month in full format :",c2.strftime("%B"))   # Month in full format : November
print("Month in short format :",c2.strftime("%b"))  # Month in short format : Nov

"""
QUESTION 4:
------------
Description : print the Current Date and time and Below format
              
              Print day in format --> Wednesday
              Print day in format --> Wed

"""

print("============= print the Current Date and time and Below format =============")

c3 = datetime.now()

print("Week in full format :",c3.strftime("%A"))       # Week in full format : Saturday
print("Week in short format :",c3.strftime("%a"))      # Week in short format : Sat

"""
QUESTION 5:
------------
Description : print the Current Date and time in the format Year-month-day

"""
print("============= print the Current Date and time in the format Year-month-day =============")

c4 = datetime.now()

print("Full format of date time year :",c4.strftime("%Y-%m-%d")) # Full format of date time year : 2024-11-02

"""
QUESTION 6:
------------
Description : print the Current Date and pass argument in constructor
               Example :  datetime.datetime(2020,6,12)

"""
print("============= print the Current Date and pass argument in constructor =============")

c5 =datetime(2020,6,12)

print("Pass arguments :",c5)  # Pass arguments : 2020-06-12 00:00:00

"""
QUESTION 7:
------------
Description : print the Current Date and pass argument in constructor
               Example :  datetime.datetime(2020,"June",12)

"""
print("============= print the Current Date and pass argument in constructor =============")

year = 2020
month_name = "June"
day = 12

specific_date = datetime.strptime(f"{year} {month_name} {day}", "%Y %B %d")

print("Specific date:", specific_date.strftime("%Y-%B-%d"))      # Specific date: 2020-June-12
 


# ------------------------------ End -----------------------------------------