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

"""
QUESTION 5:
-----------
Description:Find whether the string python is present or not using 'if'

Input = Programming languages are c,c++,Java and Python 
   
   if (s.find('Python') != -1):
  
     print("Contains substring 'Python'")
   
else:
  
     print("Doesn't contain substring")
"""
s = "Programming languages are c,c++,Java and Python"
if (s.find('Python') != -1): 
    print("Contains substring 'Python'")                # Contains substring 'Python'
else:
    print("Doesn't contain substring")

"""
QUESTION 6:
-----------

QUESTION 6.1:
-------------
Description: Given String as "Welcome to Python class" and split it by space.

Example:
--------
Input = "Welcome to Python class"

Output:
-------
Welcome
to
Python
class

"""
splite_ = "Welcome to Python class"
sp_v = splite_.split()
for i in sp_v:
    print(i)                        # Welcome | to | python | class (top to bottom)

"""
QUESTION 6.2:
-------------
Description: Given String as "Welcome to python class" and split it by l 

Example:
--------
Input = "Welcome to python class"
Output:
-------
Welcome 
to python class

"""
splite_1 = "Welcome to Python class"
sp_v2 = splite_1.split(" ",1)           # first space after all print
for i in sp_v2:
    print(i)                            # Wlecome | to python class
                                        
"""
QUESTION 7:
-----------
Description:Find the count of word "is"

Input: "Python is awesome and it is dynamic language"

output:
------
2   

"""
cou = "Python is awesome and it is dynamic language"
print(cou.count('is'))                                # 2

"""
QUESTION 8:
-------------
Description:Get the input from the user and find the count of character 'o'

"""
# user = input("Enter the String:")         # hello everyone
# print(user.count('o'))                    # 2

"""
QUESTION 9:
----------

Description: Given String as "Welcome" and count the number of consonants and vowels

Example:
---------
Input  = Welcome

output:
-------
vowels    = 3
consonants = 4

"""
str_ = "Welcome"

vowels = 0
consonants = 0

vowels_ = "aeiouAEIOU"

for char in str_:
    if char.isalpha():
        if char in vowels_:
            vowels += 1    
        else:
            consonants += 1
            
print(f"Vowels : {vowels}")          # Vowels : 3
print(f"Consonants : {consonants}")  # Consonants : 4

"""
QUESTION 10:
------------
Description : Get two input strings from user and Compare 

"""
#str_1 = input("Enter First String:")        # python
#str_2 = input("Enter second String:")       # Python
#print(str_1 == str_2)                       # False

"""
QUESTION 11:
------------
QUESTION 11.1
-------------
Description: Given String as "Welcome to Python class" and verify whether the given string startsWith, endsWith

"""
given_str = "Welcome to Python class"
print(given_str.startswith("Welcome"))      # True
print(given_str.startswith("hi"))           # False
print(given_str.endswith("class"))          # True
print(given_str.endswith("python"))         # False

"""
QUESTION 12:
------------

QUESTION 12.1
-------------
Description:Get the input from the user and print that word in lowercase, uppercase, capital

"""
#user_1 = input("Enter the String in Uppercase:")     # HELLO
#user_2 = input("Enter the String in Lowercase:")     # welcome
#user_3 = input("Enter the String in smallletters:")  # mahendran
#print(user_1.lower())                                # hello
#print(user_2.upper())                                # WELCOME
#print(user_3.capitalize())                           # Mahendran

"""
QUESTION 13:
------------
QUESTION 13.1:
--------------
Description:Remove the unwanted spaces from the given string

Example:
--------
Input  = "      Incredible India        "
Output = Incredible India

"""
input = "   Incredible India   "
val = input.strip()                  # both left and right side space remove
val_r = input.rstrip()               # right side space only remove
val_l = input.lstrip()               # left side space only remove
print(val)                           # Incredible India
print(val_r)                         #    Incredible India
print(val_l)                         # Incredible India

"""
Question 14:
------------
Description:Check whether the given inputs are isnumeric,isdigit and isdecimal

Inputs:
-------
s1 = "45"
s2 = "Â¾"
s3 = "4Â¾"
s4 = "Â²"
s5 = "1/4"

"""
s1 = "45"
s2 = "Â¾"
s3 = "4Â¾"
s4 = "Â²"
s5 = "1/4"
print(s1.isalpha())             # False
print(s2.isnumeric())           # False
print(s3.isalnum())             # True
print(s4.isdecimal())           # False
print(s5.isdigit())             # False
