# string

"""
What is string in Python?

    A string in Python is a sequence of characters enclosed in quotes.

What are the ways we can have to declare the string in Python?
    
    Strings can be declared using single quotes ('), double quotes ("), or triple quotes (''' or triple dounble quotes)

What is the function to identify memory location?
T
    he id() function.

How to find the length of the string?

    Use the len() function.

How to assign multiline String?

    Use triple quotes (''' or triple dounble quotes ).

How to join two strings and how many ways?

    Use the + operator or join() method.

What is meant by slicing operator and purpose?

    The slicing operator ([:]) extracts a portion of a string.

How to compare two strings?

    Use comparison operators (==, !=, <, >, etc.).

Difference between "==" and "is"?

    == compares values, while is checks for object identity.

What is the purpose of format() method?

    The format() method formats and inserts values into a string.

What is meant by escape character?

    An escape character (e.g., \n, \t) is used to insert special characters.

What is the purpose of strip() method?

    The strip() method removes leading and trailing whitespace from a string.

"""

"""
QUESTION 1:
-----------
Description: Find the length of the below string

              String_1: "GreensTechnology"
              String_2: "Python Programming"
              String_3: "s e l e n i u m"
              String_4: "9876543210"
              String_5: "Hi welcome to the world of programs"
"""
String_1 = "GreensTechnology"
print(len(String_1))                                            # 16

String_2 = "Python Programming"
print(len(String_2))                                            # 18

String_3 = " s e l e n i u m "
print(len(String_3))                                            # 17

String_4 = "9876543210"
print(len(String_4))                                            # 10 

String_5 = "Hi welcome to the world of programs"
print(len(String_5))                                            # 35