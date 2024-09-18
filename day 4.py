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
QUESTION 11:
------------
for x in range(1,100):
    if(x==5):
        print(x)

"""
for x in range(1,100):
    if(x==5):
        print(x)          # 5

