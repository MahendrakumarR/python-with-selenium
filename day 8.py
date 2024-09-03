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
tuple_n = 10,20,30,90,10,10,40,50
print(len(tuple_n))                              # 8

"""
QUESTION 1.2:
--------------------
Description : Create a new tuple with values and find the length of it
              Input : tuple = ("python","selenium","sql","java")
"""
tuple_le = ("python","selenium","sql","java")
print(len(tuple_le))                              # 4

"""
QUESTION 2:
------------------
QUESTION 2.1:
-------------------
Description : Get the first index value of 10 
              Input:  tuple = (10,20,30,90,10,10,40,50)
"""
tuple_f = (10,20,30,90,10,10,40,50)
print(tuple_f.index(10))                          # 0

"""
QUESTION 2.2:
--------------------
Description : Get the last index value of 10 
              Input:   tuple = (10,20,30,90,10,10,40,50)
"""
tuple_in = (10,20,30,90,10,10,40,50)
print(tuple_in.index(10,5))                      # 5

"""
QUESTION 2.3:
--------------------
Description : Get the each index value of 10 present in below tuple
              Input:    tuple = (10,20,30,90,10,10,40,50,10)
"""
tuple_w = (10,20,30,90,10,10,40,50,10)
for index,value in enumerate(tuple_w):
    if value == 10:
        print(index)                           # 0 4 5 8  (top to bottom)

"""
QUESTION 3:
------------------
QUESTION 3.1:
--------------------
Description : Get the value present at 2nd index
              Input:   tuple = (10,20,30,40,50,60)
"""
tuple_1 = (10,20,30,40,50,60)
value = tuple_1[2]
print(value)                                   # 30

"""
QUESTION 3.2:
--------------------
Description : Get the value present at -3rd index
              Input:  tuple = (105,205,305,405,505,605,705,805)
"""
tuple_i = (105,205,305,405,505,605,705,805)
value = tuple_i[-3]
print(value)                                   # 605

"""
QUESTION 4:
------------------
QUESTION 4.1:
--------------------
Description : Add a value 100 at the last position of tuple
              Input:   tuple = (10,20,30,90,10,10,40,50)
"""
tuple_q = (10,20,30,90,10,10,40,50)
new = tuple_q + (100,)
print(new)                                    # (10, 20, 30, 90, 10, 10, 40, 50, 100)

        # or

tuple_value = (10,20,30,90,10,10,40,50)
conrt_list = list(tuple_value)                # tuple convert into list
conrt_list.append(1011)                       # add new value into list
conrt_tuple = tuple(conrt_list)               # then convert list into tuple
print(conrt_tuple)                            # (10, 20, 30, 90, 10, 10, 40, 50, 1011)

"""
QUESTION 4.2:
--------------------
Description : Add a values ('java','python') at the last position of tuple
              Input:   tuple = (10,20,30,90,10,10,40,50)
"""
tuple_e = (10,20,30,90,10,10,40,50)
l_e = list(tuple_e)
l_e.extend(['java','python'])                  # (10, 20, 30, 90, 10, 10, 40, 50, 'java', 'python')
t_e = tuple(l_e)
print(t_e)

        # or

tuple_ll = (10,20,30,90,10,10,40,50)
new = tuple_ll + ('java','python')
print(new)                                   # (10, 20, 30, 90, 10, 10, 40, 50, 'java', 'python')

"""
QUESTION 5:
------------------
QUESTION 5.1:
--------------------
Description : Count the 10 value present in tuple
              Input:    tuple  = (10,20,30,90,10,10,40,50,10)
"""
tuple_count  = (10,20,30,90,10,10,40,50,10)
v = tuple_count.count(10)
print(v)                                    # 4

"""
QUESTION 5.2:
--------------------
Description :Find the maximum value  in tuple
              Input: tuple  = (10,20,30,90,10,10,40,50,10)
              Input: tuple = ("A", "a")
"""
tuple_max_min_alpha  = ("A", "a")
tuple_max_min_num  = (10,20,30,90,10,10,40,50,10)
print(max(tuple_max_min_alpha))                       # a   Maximum Value
print(min(tuple_max_min_alpha))                       # A   Minimum Value
print(max(tuple_max_min_num))                         # 90   Maximum Value
print(min(tuple_max_min_num))                         # 10   Minimum Value

"""
QUESTION 6:
--------------------
QUESTION 6.1:
--------------------
Description :Convert string into tuple
              Input:python
"""
a = "python"
tuple_str = tuple(a)
print(tuple_str)                 # ('p', 'y', 't', 'h', 'o', 'n')

"""
QUESTION 6.2:
--------------------
Description :Convert list into tuple
              Input: List = ['java','python',20,10,60]
"""
List = ['java','python',20,10,60]
convrt_tuple = tuple(List)
print(convrt_tuple)             # ('java', 'python', 20, 10, 60)

"""
QUESTION 7:
--------------------
QUESTION 7.1:
--------------------
Description : To check weather value 200 is present or not in tuple
              Input:  tuple = (105,205,305,405,505,605,705,805)
"""
tuple = (105,205,305,405,505,605,705,805)
print(200 in tuple)                        # False
 
"""
QUESTION 7.2:
--------------------
Description : Create a tuples with values and compare the two tuple
              Input:   tuple = (10,20,30,40,50,60)
              Input:   tuple1 = (10,20,30,40,50,60)
"""
tuple_ = (10,20,30,40,50,60)
tuple_1 = (10,20,30,40,50,60)
print(tuple_ == tuple_1)                    # True

"""
QUESTION 8:
--------------------
QUESTION 8.1:
--------------------
Description : Get the each value of tuple by using  for loop
              Input:   tuple = (105,205,305,405,505,605,705,805)
"""
tuple = (105,205,305,405,505,605,705,805)
for i in tuple:
    print(i)                                # 105,205,305,405,505,605,705,805  (top to bottom)

"""
QUESTION 8.2:
--------------------
Description : Get the each value of tuple by using  Enumarate for loop
              Input:   tuple = (105,205,305,405,505,605,705,805)
"""
tuple = (105,205,305,405,505,605,705,805)
for index, value in enumerate(tuple):
    print(f"The index is : {index} Value : {value}")   # The index is : 0 Value : 105  (top to bottom)

"""
QUESTION 8.3:
---------------------
Description : Get the each value of tuple by using  Enumarate for loop and print only even index value
              Input:   tuple = (105,205,305,405,505,605,705,805)
"""
tuple_2 = (105,205,305,405,505,605,705,805)
for index, value in enumerate(tuple_2):
    if index % 2 == 0:
        print(value)                                    # 105 305 505 705 (top to bottom)