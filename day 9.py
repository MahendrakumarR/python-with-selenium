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
print(set)                         # {100, 40, 200, 10, 300, 50, 20, 90, 30}

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