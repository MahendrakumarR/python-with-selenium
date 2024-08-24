"""
QUESTION 1:
-----------
Description: Find the length of the below string

              String_1: GreensTechnology
              String_2: Python Programming
              String_3: s e l e n i u m
              String_4: 9876543210
              String_5: Hi welcome to the world of programs

# Strings provided in the question
String_1 = "GreensTechnology"
String_2 = "Python Programming"
String_3 = "s e l e n i u m"
String_4 = "9876543210"
String_5 = "Hi welcome to the world of programs"

# Finding the length of each string using len() function
length_String_1 = len(String_1)
length_String_2 = len(String_2)
length_String_3 = len(String_3)
length_String_4 = len(String_4)
length_String_5 = len(String_5)

# Displaying the lengths of the strings
print(f"Length of String_1 '{String_1}' is: {length_String_1}")
print(f"Length of String_2 '{String_2}' is: {length_String_2}")
print(f"Length of String_3 '{String_3}' is: {length_String_3}")
print(f"Length of String_4 '{String_4}' is: {length_String_4}")
print(f"Length of String_5 '{String_5}' is: {length_String_5}")

"""
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
"""
# String 1
string_1 = "Greens Technology"
index_e = string_1.find('e')
print(f"Index of 'e' in '{string_1}': {index_e}")

# String 2
string_2 = "Automation testing tool"
index_testing = string_2.find('testing')
print(f"Index of 'testing' in '{string_2}': {index_testing}")

# String 3
string_3 = "Selenium automation using Python"
index_automation = string_3.find('automation')
index_using = string_3.find('using')
print(f"Index of 'automation' in '{string_3}': {index_automation}")
print(f"Index of 'using' in '{string_3}': {index_using}")

# String 4
string_4 = "Programming languages are c,c++,Java and Python"
index_c = string_4.find('c')
index_java = string_4.find('Java')
index_ruby = string_4.find('Ruby')
index_q = string_4.find('q')
index_t = string_4.find('t')

print(f"Index of 'c' in '{string_4}': {index_c}")
print(f"Index of 'Java' in '{string_4}': {index_java}")
print(f"Index of 'Ruby' in '{string_4}': {index_ruby}")
print(f"Index of 'q' in '{string_4}': {index_q}")
print(f"Index of 't' in '{string_4}': {index_t}")

"""
"""

QUESTION 3:
-----------
Description:Using find method perform the below operations

   String_1: Selenium automation using Python
   Find the occurence of automation and using

"""
"""
# String 1
string_1 = "Selenium automation using Python"

# Find the first occurrence of "automation"
index_automation = string_1.find('automation')
print(f"Index of 'automation' in '{string_1}': {index_automation}")

# Find the first occurrence of "using"
index_using = string_1.find('using')
print(f"Index of 'using' in '{string_1}': {index_using}")

"""
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