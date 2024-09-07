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

"""
QUESTION 2:
-----------
Description:Find the index position

   String_1: Greens Technology
   Find the index of e

   String_2: Automation testing tool
   Find the index of testing

   String_3: Selenium automation using Python
   Find the index of automation and using
   
   String_4: Programming languages are c,c++,Java and Python
   Find the index of c
   Find the index of Java
   Find the index of Ruby
   Find the index of q and t

"""
String_1 = "Greens Technology"
v = String_1.find('e')
print(v)                            # 2

String_2 = "Automation testing tool"
v1 = String_2.find('testing')
print(v1)                           # 11

String_3 = "Selenium automation using Python"
v2 = String_3.find('automation')
v3 = String_3.find('using')
print(v2,v3)                        # 9 20

String_4 = "Programming languages are c,c++,Java and Python "
v4 = String_4.find('c')             # 26
v5 = String_4.find('Java')          # 32
v6 = String_4.find('Ruby')          # -1
v7 = String_4.find('q')             # -1
v8 = String_4.find('t')             # 43
print(v4, v5, v6, v7, v8)           # 26 32 -1 -1 43 

"""
QUESTION 3:
-----------
Description:Using find method perform the below operations

   String_1: "Selenium automation using Python"
   Find the occurence of automation and using

"""

String_5 = "Selenium automation using Python"
v9 = String_5.find('automation')
v10 = String_5.find('using')
print(f"The word 'automation' occurece at : {v9}" )   # The word 'automation' occurece at : 9
print(f"The word 'using' occurece at : {v10}" )       # The word 'using' occurece at : 20
 
"""
QUESTION 4:
----------
Description:Given String is "Welcome to Python class" and find the substring
   
   Input = "Welcome to Python class"

   Outputs:
   --------
   e
   elco
   to
   Python
   to Python class

And also try with negative scenarios

"""
input_str = "Welcome to Python class"

output_1 = input_str[1]
output_2 = input_str[1:5]
output_3 = input_str[8:10]
output_4 = input_str[11:17]
output_5 = input_str[8:]

print(output_1)             # e
print(output_2)             # elco
print(output_3)             # to
print(output_4)             # python
print(output_5)             # to python class
