"""
    1.if/elif
    2.Loopings(for,while)
    3.break/continue
"""

"""
What is the difference between break and continue?
    
    break exits the loop, while continue skips the current iteration and moves to the next one.

What is meant by control statements and types?
    
    Control statements control the flow of execution, and types include conditional (if), iterative (for, while), and jump (break, continue, return).

What is meant by a for loop?
    
    A for loop iterates over a sequence (list, tuple, string) or range of values.

Can you explain the for loop execution process?
    
    A for loop initializes a variable, checks a condition, executes a block, and updates the variable in each iteration.

Difference between for and while loop?
    
    A for loop runs for a known number of iterations, while a while loop runs until a condition is met.

Is it possible to use break and continue outside of a loop?
    
    No, break and continue are only valid within loops.

Write the syntax of for:
    
    for variable in iterable:

Write the syntax of while:
    
    while condition:

Write the syntax of elif:
    
    elif condition:

Difference between if-else and elif:

    if-else is used for binary conditions, while elif handles multiple conditions.

"""
"""
QUESTIONS(Find the output)
-----------------------
QUESTION 1:
------------
for x in range(1,100):
    if(x==5):
        print(x)

"""
for x in range(1,100):
    if(x==5):
        print(x)            # 5

"""
QUESTION 2:
------------
for x in range(1,100):
    if(x==5):
        break
print(x)

"""
for x in range(1,100):
    if(x==5):
        break
print(x)                  # 5

"""
QUESTION 3:
----------
for x in range(1,100):
    if(x==5):
        continue
print(x)

"""
for x in range(1,100):
    if(x==5):
        continue
print(x)                  # 99

"""
QUESTION 4:
------------
for x in range(1,4):
   for y in range(1,4):
       print(y)
print(x)

"""
for x in range(1,4):
       for y in range(1,4):
        print(y)                # 123123123(top to bottom)
print(x)                        # 3

"""
QUESTION 5:
-----------
for x in range(1,4):
   for y in range(1,x):
       print(y)
"""
for x in range(1,4):
       for y in range(1,x):
        print(y)             # 112 (top to bottom)

"""

QUESTION 6:
-----------
for x in range(1,4):
   for y in range(x+1,4):
       print(y)
"""
for x in range(1,4):
    for y in range(x+1,4):
        print(y)             #  233 (top to bottom)

"""
QUESTION 7:
------------
for x in range(1,100):
    if(x==5):
        print(x)

"""
for x in range(1,100):
    if(x==5):
        print(x)          # 5

"""
QUESTIONS(Programs)
-------------------
QUESTION 1:
-----------
Description: Write Python program to allow the user to input his/her age.     
             Then the program will show if the person is eligible to vote.
             A person who is eligible to vote must be older than or equal 1 to 18 years old.
Example:
--------
Input  = 10
Output = print not eligible.

"""
#user = int(input("Enter Your Age:"))
#if user >= 18:
#    print(f"You are {user} years old so eligble for vote.")
#else:                                                               # Enter Your Age:10
#    print(f"You are {user} years old so not eligble for vote.")     # You are 10 years old so not eligble for vote.

"""
QUESTION 2:
-----------
Description: Write a program to find even or odd number

Example:
---------
Input  = 10
Output = Even

"""
i = 10
if i % 2 == 0:
    print(f"The given number {i} is Even")
else:
    print(f"The given number {i} is Odd")       # The given number 10 is Even

"""
QUESTION 3:
------------
Description: Write a program to print even number from 1 to 100 

Example:
---------
Output = 2,4,....100

"""
for i in range(1,100):
    if i % 2 == 0:
        print(i)        # (2,4,6,...98) (top to bottom)
"""
QUESTION 4:
------------
Description: Find the sum of odd number 1 to 100

Example:
--------
Output = 2500

"""
odd = 0
for i in range(1,101):
    if i % 2 != 0:           
        odd += i
print("Sum of Odd numbers are:",odd) # 2500

"""
QUESTION 5:
-----------
Description: Count of even number 1 to 100

Example:
--------
Output = 50

"""
c = 0
for i in range(1,101):
    if i % 2 == 0:
        c += 1          # here using 1 for count
print("Count of Even numbers are:",c) # 50

"""
QUESTION 6:
-----------
Description: Write a program to find the factorial of a number.

Example:
--------
Input  = 5
Output = 120

"""
user = 5

result = 1

for i in range(1,user+1):
    result *= i
print(f"factorial of {user} is:",result)  # factorial of 5 is: 120

"""
QUESTION 7:
------------
Description: Write a program to print the fibonacci series of a number 1 to 100.

Example:
--------
Output = 0,1,1,2,3,5.....

"""
a = 0
b = 1

while a<=100:
    print(a,end="")   # 01123581321345589
    a, b = b, a+b   
    


