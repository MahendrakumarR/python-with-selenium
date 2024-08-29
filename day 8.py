# tuple()

"""

1.What is a tuple?

    A tuple is an ordered, immutable collection of elements in Python.

2.What is the difference between list and tuple?

    Lists are mutable (can be changed), while tuples are immutable (cannot be changed).

3.What are the methods present in tuple?

    Common tuple methods are count() and index().

4.Advantages of Tuple over List?

    Tuples are faster, use less memory, and are suitable for fixed data.

5.How to remove the values present in tuple?

    Tuples are immutable, so values cannot be removed directly; you can convert the tuple to a list, remove the values, and convert it back to a tuple.

"""
"""
QUESTION 1:
------------------
QUESTION 1.1:
--------------------
Description : Create a new tuple with values and find the length of it
              Input : tuple = 10,20,30,90,10,10,40,50

"""
tuple = 10,20,30,90,10,10,40,50
print(len(tuple))                              # 8

"""
QUESTION 1.2:
--------------------
Description : Create a new tuple with values and find the length of it
              Input : tuple = ("python","selenium","sql","java")
"""
tuple = ("python","selenium","sql","java")
print(len(tuple))                              # 4

"""
QUESTION 2:
------------------
QUESTION 2.1:
-------------------
Description : Get the first index value of 10 
              Input:  tuple = (10,20,30,90,10,10,40,50)
"""
tuple = (10,20,30,90,10,10,40,50)
print(tuple.index(10))                          # 0