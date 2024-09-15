# dictionary {}
"""
What is a dictionary in Python?

    A dictionary in Python is an unordered collection of key-value pairs, where each key is unique, and the values can be any data type.

How do you get all values from a Python dictionary?

    Use the values() method to get all values from a Python dictionary.

What are the methods available in Python dictionary?

    Some common methods are keys(), values(), items(), get(), pop(), popitem(), clear(), update(), setdefault(), and copy().

How do you remove a particular pair from a Python dictionary?

    Use the pop(key) method to remove a specific key-value pair from a dictionary.

What is the purpose of popitem() method?

    The popitem() method removes and returns the last inserted key-value pair from the dictionary.

What is the difference between pop() and popitem()?

    The pop() method removes a specified key and returns its value, while popitem() removes and returns the last inserted key-value pair.

How do you add the value to the dictionary?

    Assign a value to a new key using dictionary[key] = value to add a value to the dictionary.

What are the possible ways to get the value of the corresponding key?

    Use dictionary[key] or dictionary.get(key) to get the value of a corresponding key.

What are the possible ways to update more than one key-value pair in a dictionary?

    Use the update() method to update more than one key-value pair in a dictionary.

What is the method used to print all keys?

    Use the keys() method to print all keys.

What is the method used to print all values?

    Use the values() method to print all values.

What is the return type of keys() and values()?

    The return type of keys() and values() is dict_keys and dict_values, respectively.

What is the method used for removing all values in a dictionary?

    Use the clear() method to remove all values in a dictionary.

Is it possible to copy a dictionary?
    Yes, it is possible to copy a dictionary in Python. You can do this using the copy() method or the dict() constructor. Both create a shallow copy of the original dictionary.

"""
"""
QUESTION 1:
------------
QUESTION 1.1:
-------------------
Description : Create a Dictionary with the below key , values and find the length of  it
              key      : {100,200,300,400,500,600,100,500,400}
              values   : {'java','sql','oops','Sql','oracle','DB','selenium','psql','Hadoop'}
"""
dict_1 = {100 :'java', 200 : 'sql', 300:'oops', 400 : 'Sql', 500 : 'oracle', 600 : 'DB', 100 : 'selenium', 500 : 'psql', 400 : 'Hadoop'}
print(len(dict_1))                                      # 6

"""
QUESTION 1.2:
-------------------
Description : Create a Dictionary with the below key , values and find the length of  it
              key    : {'a','b','c','python','oops','welcome',20}
              Values : {10,20,30,40,50.4,'hi',2+2j}
"""
dict_2 = {'a':10, 'b':20, 'c' : 30, 'python':40, 'oops':50.4, 'welcome':'hi', 20:2+2j} # here all datatype used int, float,str,complex for keys and values
print(len(dict_2))                                      # 7

"""
QUESTION 2:
--------------
QUESTION 2.1:
--------------------
Description : Create a Dictionary  with the below key and values and get(print) the keys, values, then keys and values separately in the Dictionary .
               key    : {'a','vel', 30, 4+2j, 39.7}
               Values : {10, 'selenium', 'five', 20.3, 90} 
"""
dict_3 = {'a':10, 'vel':'selenium', 30:'five', 4+2j:20.3, 39.7:90, 'a':20}
print(dict_3.keys())                                                # dict_keys(['a', 'vel', 30, (4+2j), 39.7])
print(dict_3.values())                                              # dict_values([20, 'selenium', 'five', 20.3, 90])
print(dict_3.items())                                               # dict_items([('a', 20), ('vel', 'selenium'), (30, 'five'), ((4+2j), 20.3), (39.7, 90)])

"""
QUESTION 3:
--------------
QUESTION 3.1:
--------------------
Description : Create a Dictionary  with the below key and values and iterate
              Key    : {10,20,30,40,50,60,10,50,40}
              Values : {101,202,303,404,505,606,104,505,404}

"""
dict_4 = {10:101, 20:202, 30:303, 40:404, 50:505, 60:606, 10:104, 50:505, 40:404}
for x in dict_4.keys():
    print(x)                    # 10,20,30,40,50,60  (top to bottom)

for y in dict_4.values():
    print(y)                   # 104,202,303,404,505,606 (top to bottom)


for z in dict_4.items():
    print(z)                   # (10, 104) (20, 202) (30, 303) (40, 404) (50, 505) (60, 606) (top to bottom)

"""
QUESTION 3.2:
--------------------
Description : Create a Dictionary  with the below key and values and iterate
               Key     : {'vel','Ganesh','Dinesh','Vengat','subash'}
               Values  : {'Selenium','framework','oracle','python','jira'}
"""
dict_5 = {'vel':'Selenium' ,'Ganesh':'framework' ,'Dinesh':'oracle' ,'Vengat':'python' ,'subash':'jira'}
for x in dict_5.keys():
    print(x)                   # vel Ganesh Dinesh vengat subash (top to bottom)

for y in dict_5.values():
    print(y)                   # Selenium framework oracle python jira (top to bottom)

for z in dict_5.items():
    print(z)                   # ('vel', 'Selenium') ('Ganesh', 'framework') ('Dinesh', 'oracle') ('Vengat', 'python') ('subash', 'jira') (top to bottom)

"""
QUESTION 4:
-----------------
QUESTION 4.1:
--------------------
Description : Add a key and value pair [10:sql] at the last position of Dictionary
              Key    : {10, 20 ,30,40,50,60}
              Values : {'python','selenium','java','c','c++','oracle'}
"""
dict_6 = {10:'python', 20:'selenium', 30:'java', 40:'c', 50:'c++', 60:'oracle'}
dict_6[10]='sql'
print(dict_6)                  # {10: 'sql', 20: 'selenium', 30: 'java', 40: 'c', 50: 'c++', 60: 'oracle'}

"""
QUESTION 5:
--------------------
QUESTION 5.1:
--------------------
Description : Create a Dictionary with below key and Value  and Remove the key [50]
              Key    : {10,20,30,40,50,60}
              Values : {100,200,300,400,500,600}
"""
dict_7 = {10:100,20:200,30:300,40:400,50:500,60:600}
dict_7.pop(50)
print(dict_7)                  # {10: 100, 20: 200, 30: 300, 40: 400, 60: 600}

"""
QUESTION 6:
------------------
QUESTION 6.1:
--------------------
Description : Create a Dictionary with below key and Value and Add the value(900) using " Slice " operator
              Key    : {10,20,30,40,50,60}
              Values : {100,200,300,400,500,600} 
"""
dict_8 = {10:100,20:200,30:300,40:400,50:500,60:600}
dict_8[90] = 900
print(dict_8)                  # {10: 100, 20: 200, 30: 300, 40: 400, 50: 500, 60: 600, 90: 900}

"""
QUESTION 6.2:
--------------------
Description : print all value in list
        [{'id':10,'name':'vel','email':'vel@gmail.com'},{'id':20,'name':'nisha','email':'nisha@gmail.com'},{'id':30,'name':'bala','email':'bala@gmail.com'}]
"""

data = [
        {'id':10,'name':'vel','email':'vel@gmail.com'},        # dict_values([10, 'vel', 'vel@gmail.com'])
        {'id':20,'name':'nisha','email':'nisha@gmail.com'},    # dict_values([20, 'nisha', 'nisha@gmail.com'])
        {'id':30,'name':'bala','email':'bala@gmail.com'}       # dict_values([30, 'bala', 'bala@gmail.com'])
    ]
for item in data:
    print(item.values())

"""
QUESTION 7:
------------------
QUESTION 7.1:
--------------------
Description : print all value in tuple
              ([10,'vel','vel@gmail.com'],[20,'nisha','nisha@gmail.com'],[30,'bala','bala@gmail.com'])

"""
data = (
    [10,'vel','vel@gmail.com'],        
    [20,'nisha','nisha@gmail.com'],
    [30,'bala','bala@gmail.com']
    )

for item in data:                   # (10, 'vel', 'vel@gmail.com')
    v = tuple(item)                 # (20, 'nisha', 'nisha@gmail.com')
    print(v)                        # (30, 'bala', 'bala@gmail.com')