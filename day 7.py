# list []

"""
What is a list?
    
    A list is an ordered, mutable collection of elements, defined with [].

How to remove values from a list?
    
    Use remove(), pop(), or del.

What is the difference between append() and extend()?
    
    append() adds one element; extend() adds multiple elements.

How to find the length of a list?
    
    Use len(list).

What are the methods present in a list?
    
    append(), extend(), insert(), remove(), pop(), clear(), sort(), reverse().

Is negative indexing in a list possible or not?
    
    Yes, negative indexing is possible.

How to delete or remove elements from a list?
    
    Use remove(), pop(), clear(), or del.

How to change or add elements to a list?
    
    Use indexing to change, append(), insert(), or extend() to add.

How to slice lists in Python?
    
    Use list[start:stop:step].

How to access elements from a list?
    
    Use list[index].

What is the difference between pop() and del?
    
    pop() removes and returns an element; del just removes it.

What are ways to remove all values from a list?
    
    Use clear() or assign [].

What is the difference between sort() and sorted()?
    
    sort() modifies the list; sorted() returns a new sorted list.

Write a way to sort values in descending order?
    
    Use sort(reverse=True) or sorted(list, reverse=True).

Is it possible to check whether a value is present or not?
    
    Yes, use value in list.

"""

"""
QUESTION 1:
------------------
Description : Create a new list with values and find the length of it
              Input : List = [10,20,30,90,10,10,40,500]
"""
List_len = [10,20,30,90,10,10,40,50]
print(len(List_len))                        # 8

"""
QUESTION 2:
------------------
Description : Create a new list with values and find the length of it
              Input : List = ['Java','Python','Selenium','java',10,20,10]
"""
list_lenth = ['Java','Python','Selenium','java',10,20,10]
print(len(list_lenth))                                          # 7

"""
QUESTION 3:
------------------
QUESTION 3.1:
--------------------
Description : Get the  index value of 10 
              Input:   List = [10,20,30,90,10,50]
"""
list_index = [10,20,30,90,10,50]
index_value = list_index.index(10)
print(index_value)                                  # 0


"""
QUESTION 3.2:
--------------------
Description : Get the each index value of 90 present in below list 
              Input:   List = [10,20,30,90,40,50,10,90]
"""
list_each_index = [10,20,30,90,40,50,10,90]
for index,value in enumerate(list_each_index):
    if value == 90:
        print(index)                               # 3 7 (top to bottom)

"""
QUESTION 3.3:
--------------------
Description : Add a value [100,200,300] at the last position of list and find index value of 200
              Input : List = [10,20,30,90,10,10,40,50]
"""
list_extend = [10,20,30,90,10,10,40,50]
list_extend.extend([100,200,300])
print(list_extend)                              # [10, 20, 30, 90, 10, 10, 40, 50, 100, 200, 300]
print(list_extend.index(200))                   # 9

"""
QUESTION 4:
------------------
QUESTION 4.1:
--------------------
Description : Get the value present at 2nd index
              Input:   List = [10,20,30,40,50,60]
"""
list_position = [10,20,30,40,50,60]
print(list_position[2])                         # 30

"""
UESTION 4.2:
--------------------
Description : Get the value present at -2nd index
              Input:   List = [105,205,305,40,705,805]
"""
list_position_2 = [105,205,305,40,705,805]
print(list_position_2[-2])                     # 705

"""
QUESTION 5:
------------------
QUESTION 5.1:
--------------------
Description : Remove the value present at 2nd index and print the removed value
              Input:   List = [10,20,30,40,50,60]
"""
list_remove = [10,20,30,40,50,60]
remove_value = list_remove.pop(2)
print(remove_value)                            # 30

"""
QUESTION 5.2:
--------------------
Description : Remove the last value of 10 present in the list  
              Input:   List = [10,20,30,90,10,10,40]
"""
list_last = [10,20,30,90,10,10,40]
list_last.reverse()                            # here reverse the list
list_last.remove(10)                           # remove the reversed list value of 10
list_last.reverse()                            # then reverse again
print(list_last)                               # [10, 20, 30, 90, 10, 40]

"""
QUESTION 5.3:
--------------------
Description : delete the value  present in (-5th to -1st) index in the list  
              Input:   List = [10,20,30,90,10,10,40,60,80,100]
"""
list_delete = [10,20,30,90,10,10,40,60,80,100]
del list_delete[-5 : -1]
print(list_delete)                              # [10, 20, 30, 90, 10, 100]

"""
QUESTION 5.4:
--------------------
Description : clear all the value  present in the list  
              Input:   List = [10,20,30,90,10,10,40,60,80,100]
"""
list_clear = [10,20,30,90,10,10,40,60,80,100]
print(list_clear.clear())                      # None

"""
QUESTION 6:
------------------
QUESTION 6.1:
--------------------
Description : Replace the value 300 into 350 in the list
              Input : List = [100,200,300,400,500,600,700]
"""
list_replace = [100,200,300,400,500,600,700]
find_index_position = list_replace.index(300)   # find the index position of 300      
list_replace[find_index_position] = 350         # change the value using index 
print(list_replace)                             # [100, 200, 350, 400, 500, 600, 700]

"""
QUESTION 7:
------------------
QUESTION 7.1:
---------------------
Description : Add a value 50 in the 2nd index and display the list after adding.
              Input : List = [10,20,30,90,10,10,40,50]
"""
list_add = [10,20,30,90,10,10,40,50]
list_add.insert(2,50)                   
print(list_add)                                # [10, 20, 50, 30, 90, 10, 10, 40, 50]

"""
QUESTION 8:
------------------
QUESTION 8.1:
----------------------
Description : count the 10 value present in the list
              Input : List = [10,20,30,90,10,10,40,50]
"""
list_count = [10,20,30,90,10,10,40,50]
print(list_count.count(10))                    # 3

"""
QUESTION 8.2:
----------------------
Description : find the maximum and minimum value in the list
              Input : List = ['java','python','selenium','Java','Python','Selenium']
              Input : List = [10,20,30,90,10,10,40,50]
"""
list_max_min_alpha = ['java','python','selenium','Java','Python','Selenium']
list_max_min_num = [10,20,30,90,10,10,40,50]
print(max(list_max_min_alpha))                   # selenium                 
print(min(list_max_min_alpha))                   # Java
print(max(list_max_min_num))                     # 90 
print(min(list_max_min_num))                     # 10

"""
QUESTION 9:
----------------------
QUESTION 9.1:
----------------------
Description : Reverse the values present in list
              Input : List = [10,20,30,50,90,40,100,60,10,70]
"""
list_reverse = [10,20,30,50,90,40,100,60,10,70]
list_reverse.reverse()
print(list_reverse)                             # [70, 10, 60, 100, 40, 90, 50, 30, 20, 10]

"""
QUESTION 9.2:
----------------------
Description : Sort the values (Ascending &Descending ) order present in list
              Input : List = [10,20,30,50,90,40,100,60,10,70]
"""
list_sort = [10,20,30,50,90,40,100,60,10,70]
list_sort.sort()
print(list_sort)                                # [10, 10, 20, 30, 40, 50, 60, 70, 90, 100]
list_sort.sort(reverse=True)
print(list_sort)                                # [100, 90, 70, 60, 50, 40, 30, 20, 10, 10]

"""
QUESTION 9.3:
----------------------
Description : Create a lists with values and compare the two list
              Input : List = [10,20,30,90,10,10,40,50]
              Input : List = [30,40,50,60,80]
"""
list_1 = [10,20,30,90,10,10,40,50]
list_2 = [30,40,50,60,80]
print(list_1 == list_2)                         # False

"""
QUESTION 10:
--------------------
QUESTION 10.1:
--------------------
Description : Get the each value of list by using  for loop
              Input:   List = [105,205,305,405,505,605,705,805]
"""
list = (105,205,305,405,505,605,705,805)
for i in list:
    print(i)                                # 105,205,305,405,505,605,705,805  (top to bottom)

"""
QUESTION 10.2:
--------------------
Description : Get the each value of list by using  Enumerate for loop
              Input:   List = [105,205,305,405,505,605,705,805]
"""
list_loop = [105,205,305,405,505,605,705,805]
for index, value in enumerate(list_loop):
    print(f"The index is : {index} Value : {value}")   # The index is : 0 Value : 105  (top to bottom)

"""
QUESTION 10.3:
---------------------
Description : Get the each value of list by using  Enumerate for loop and print only even index value
              Input:   List = [105,205,305,405,505,605,705,805]
"""
list_loop_1 = [105,205,305,405,505,605,705,805]
for index, value in enumerate(list_loop_1):
    if index % 2 == 0:
        print(value)                                    # 105 305 505 705 (top to bottom)