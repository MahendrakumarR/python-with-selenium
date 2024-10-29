
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

print("print the Current Date and time :",c)