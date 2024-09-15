"""
QUESTION 1:
-----------
Description: Find the length of the below string

              String_1: GreensTechnology
              String_2: Python Programming
              String_3: s e l e n i u m
              String_4: 9876543210
              String_5: Hi welcome to the world of programs
"""

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

QUESTION 3:
-----------
Description:Using find method perform the below operations

   String_1: Selenium automation using Python
   Find the occurence of automation and using

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

# Given string
input_string = "Welcome Java then Ruby to Python class"

# Positive scenarios
# Extracting each specified substring
substring_1 = input_string[1]         # 'e'
substring_2 = input_string[1:5]       # 'elco'
substring_3 = input_string[23:25]     # 'to'
substring_4 = input_string[26:32]     # 'Python'
substring_5 = input_string[23:]       # 'to Python class'

# Printing the positive scenario outputs
print("Positive Scenarios:")
print(substring_1)
print(substring_2)
print(substring_3)
print(substring_4)
print(substring_5)

# Negative scenarios

substring_6 = input_string.find('Java')     # Should return -1
substring_7 = input_string.find('Ruby')     # Should return -1
substring_8 = input_string.find('Pythonic') # Should return -1

# Printing the negative scenario outputs
print("\nNegative Scenarios:")
print(f"Index of 'Java': {substring_6}")
print(f"Index of 'Ruby': {substring_7}")
print(f"Index of 'Pythonic': {substring_8}")


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

# Given string
input_string = "Programming languages are c,c++,Java and Python"

# Check if 'Python' is present in the string
if input_string.find('Python') != -1:
    print("Contains substring 'Python'")
else:
    print("Doesn't contain substring 'Python'")


"""
QUESTION 6:
-----------

QUESTION 6.1:
-------------
Description: Given String as "Welcome to Python class" and split it by space.

Example:
--------
Input = Welcome to Python class 

Output:
-------
Welcome
to
Python
class

"""

# Given string
input_string = "Welcome to Python class"

# Split the string by spaces
split_words = input_string.split(' ')

# Print each word on a new line
for word in split_words:
    print(word)


"""
QUESTION 6.2:
-------------
Description: Given String as "Welcome to python class" and split it by l 

Example:
--------
Input = Welcome to python class 
Output:
-------
We
come to python c
ass

"""

# Given string
input_string = "Welcome to python class"

# Split the string by the letter 'l'
split_by_l = input_string.split('l')

# Print each part on a new line
for part in split_by_l:
    print(part)


"""
QUESTION 7:
-----------
Description:Find the count of word "is"

Input: "Python is awesome and it is dynamic language"

output:
------
2

"""

# Given string
input_string = "Python is awesome and it is dynamic language"

# Count the occurrences of the word "is"
count_is = input_string.count('is')

# Print the count
print(count_is)


"""
QUESTION 8:
-------------
Description:Get the input from the user and find the count of character 'o'

Input:"Hi welcome to the world of programs"

Output:
-------
5

"""

# Get input from the user
user_input = input("Enter a string: ")

# Count the occurrences of the character 'o'
count_o = user_input.count('o')

# Print the count
print(f"The count of character 'o': {count_o}")


# ------------------------------ End -----------------------------------------