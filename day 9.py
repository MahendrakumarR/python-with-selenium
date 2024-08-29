# set {}
"""
1. What is a Set?

    A set is an unordered collection of unique elements in Python.

2. What is the Difference Between List and Set?

    Lists are ordered and can contain duplicates, while sets are unordered and contain only unique elements.

3. What are the Methods Present in Set?

    Common methods include add(), update(), remove(), discard(), pop(), clear(), union(), intersection(), difference(), and symmetric_difference().

4. What are the Advantages of Set?

    Sets automatically remove duplicates and offer fast membership tests.

5. How to Remove the Values Present in Set?

    Use remove(), discard(), or pop() methods.

6. Is it Possible to Take a Particular Value from a Set?

    No, because sets are unordered, so you can't access elements by index.

7. What is the Method Used for Sorting Values in Set?

    Convert the set to a list and use sorted().

8. What is the Difference Between remove() and discard()?

    remove() raises an error if the element is not found; discard() does not.

9. What is the Purpose of union, intersection, difference, symmetric_difference?

    They are used for combining, finding common elements, finding differences, and finding non-overlapping elements between sets, respectively.

10. Is it Possible to Convert a Set into a Tuple?

    Yes, use tuple().

11. Is Reversing Possible in Set?

    No, because sets are unordered.

"""
"""
QUESTION 1:
------------------
QUESTION 1.1:
--------------------
    Description : Create a new set with values and find the length of it
                
                Input : set = {10,20,30,90,10,10,40,50}

"""
set = {10,20,30,90,10,10,40,50}
s_length = len(set)
print(s_length)                  # 6

"""
QUESTION 1.2:
--------------------
Description : Create a new set with values and find the length of it
              Input : set = {python,selenium,sql,java}

"""
set = {"python","selenium","sql","java"}
s_length = len(set)
print(s_length)                   # 4

"""
QUESTION 1.3:
--------------------
Description : Create a new set with values and find the length of it
              Input : set ={10,20,30,90,10,10,40,50,python,java,22.4,True}

"""
set ={10,20,30,90,10,10,40,50,"python","java",22.4,True}
s_length = len(set)
print(s_length)                    # 10

"""
QUESTION 2:
------------------
QUESTION 2.1:
--------------------
Description : Add a value 100 at the last position of set
              Input:   set ={ 10,20,30,90,10,10,40,50 }

"""
set ={ 10,20,30,90,10,10,40,50 }
set.add(100)
print(set)                         # {50, 20, 90, 100, 40, 10, 30}

"""
QUESTION 2.2:
--------------------
Description : Add a value 'python' at the last position of set
              Input:   set = {10,20,30,90,10,10,40,50}
"""
set = {10,20,30,90,10,10,40,50}
set.add("python")
print(set)                          # {'python', 50, 20, 90, 40, 10, 30}

"""
QUESTION 2.3:
--------------------
Description : Add a values (100,200,300) at the last position of set
              Input:   set = {10,20,30,90,10,10,40,50}

"""

set = {10,20,30,90,10,10,40,50}
set1 = {100,200,300}
set.update(set1)
print(set)                          # {100, 40, 200, 10, 300, 50, 20, 90, 30}

"""
QUESTION 3:
------------------
QUESTION 3.1:
--------------------
Description : Find the maximum value in set
              Input:    set  ={ 10,20,30,90,10,10,40,50,10 }

"""
set  ={ 10,20,30,90,10,10,40,50,10 }
m = max(set)
print(m)                           # 90

"""
QUESTION 3.2:
--------------------
Description :Find the maximum value  in set
              Input:    set = {python,selenium,sql,java}
"""
set = {"python","selenium","sql","java"}
m = max(set)
print(m)                           # sql

"""
QUESTION 3.3:
--------------------
Description :Find the minimum value  in set
              Input:    set = {python,selenium,sql,java}
"""
set= {"python","selenium","sql","java"}
m = min(set)
print(m)                           # java

"""
QUESTION 4:
-----------------
QUESTION 4.1:
--------------------
Description : Update set by following data ('j'+'greens') 
              Input:  set = {105,205,305,405,505,605,705,805}
"""
sett = {105,205,305,405,505,605,705,805}
set1 = {'j'+'greens'}
sett.update(set1)
print(sett)                        # {705, 805, 'jgreens', 105, 205, 305, 405, 505, 605}

"""
QUESTION 5:
--------------------
QUESTION 5.1:
--------------------
Description :Convert string into set, Convert float into set, Convert integer into set
            Input:python, 3.5, 4
"""
# st, f, i = 'python', 3.5, 4                # here 'st', 'f', 'i' - are varibles
# s1, i1, f1 = set(st), set(f), set(i)       # here also s1, i1, f1 - are varibles convert into set 
# print(s1,i1, f1)                           # TypeError: 'set' object is not callable

"""
QUESTION 6:
--------------------
QUESTION 6.1:
--------------------
Description : To check weather value 200 is present or not in set
              Input:  set ={ 105,205,305,405,505,605,705,805}
"""
set = { 105,205,305,405,505,605,705,805}
print(200 in set)                         # False

"""
QUESTION 6.2:
--------------------
Description : Create a set with values and compare the another set
              Input:   set= {10,20,30,40,50,60}
              Input:   set1 = {10,20,30,40,50,60}
"""
set_= {10,20,30,40,50,60}
set_1 = {10,20,30,40,50,60}
print(set_ == set_1)                       # True

"""
QUESTION 7:
--------------------
QUESTION 7.1:
--------------------
Description : Get the each value of set by using  for loop
              Input:   set={ 105,205,305,405,505,605,705,805}
"""
set = { 105,205,305,405,505,605,705,805}
for i in set:
    print(i)                            # 105,205,305,405,505,605,705,805  (top - bottom)

"""
QUESTION 7.2:
--------------------
Description : Get the each value of set by using  Enumarate for loop
              Input:   set={ 105,205,305,405,505,605,705,805}
"""

set = { 105,205,305,405,505,605,705,805}
for index,value in enumerate(set):
    print(f"Index: {index} Value: {value}")        # Index: 0 Value: 705  to Index: 7 Value: 605 (top-bottom)

"""
QUESTION 7.3:
---------------------
Description : Get the each value of setby using  Enumarate for loop and print only odd index value
              Input:   set={ 105,205,305,405,505,605,705,805}
"""

set = { 105,205,305,405,505,605,705,805}
for index,value in enumerate(set):
    if index % 2 != 0 :
        print(f"Index:{index} Value:{value}")           
# Output                                           
"""
Index:1 Value:805
Index:3 Value:205
Index:5 Value:405
Index:7 Value:605

"""
"""
QUESTION 8:
------------------------
QUESTION 8.1:
--------------------
Description :Create a set with values and perform union between two set
              Input:   set= {10,20,30,40,50,60}
              Input:   set1 ={ 60,80,90,40,50,10}
"""
set = {10,20,30,40,50,60}
set1 = { 60,80,90,40,50,10}
s = set.union(set1)
print(s)                       # {40, 10, 80, 50, 20, 90, 60, 30}

"""
QUESTION 8.2:
--------------------
Description :Create a set with values and perform intersection between two Set
              Input:   set = {10,20,30,40,50,60}
              Input:   set1 = { 60,80,90,40,50,10}
"""
set = {10,20,30,40,50,60}
set1 = { 60,80,90,40,50,10}
i = set.intersection(set1)
print(i)                       # {40, 50, 10, 60}

"""
QUESTION 8.3:
--------------------
Description :Create a set with values and perform difference between two list
              Input:   set = {10,20,30,40,50,60}
              Input:   set1 = { 60,80,90,40,50,10}
"""
set = {10,20,30,40,50,60}
set1 = { 60,80,90,40,50,10}
d = set.difference(set1)
print(d)                       # {20, 30}

"""
QUESTION 8.4:
--------------------
Description :Create a set with values and perform symmetric_difference between two Set
              Input:   set= {10,20,30,40,50,60}
              Input:   set1 ={ 60,80,90,40,50,10}
"""
set = {10,20,30,40,50,60}
set1 = { 60,80,90,40,50,10}
s_d = set.symmetric_difference(set1)
print(s_d)                              # {80, 20, 90, 30}