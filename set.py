# set 
# mutable data type
"""
    * Ignore duplicate values
    * Not index based 
    * Not maintain any order 
    * values are mentioned in {} curly brackets
"""
# set methods 
"""
    len()           discard()       sorted()            difference()        symetric difference()
    add()           pop()           union()             remove()        
    update()        copy()          intersection()      clear()         
    
"""
# len() :- Returns the length of the set

num = {10,20,30,60}  
le = len(num)
print(le)                   # 4

# add() :- it is used to add a single value

num1 = {0,20,30,80}
num1.add(100)
print(num1)                 # {0, 100, 20, 80, 30}

# update() :- it is used to add a more than one value

    #   * set
n = {1,2,3,4,5}
n.update({6,7,8,9})
print(n)                   # {1, 2, 3, 4, 5, 6, 7, 8, 9}

    #  * list
m = {1,2,3,4,5}
m.update([99,10,23,14])    # using square brackets for add values into set
print(m)                   # {1, 2, 3, 4, 5, 10, 14, 23, 99}

    #  * tuple
t = {100,300,80,10}
t.update((2,9,44))         # using perantes brackets for add values into set
print(t)                   # {2, 100, 9, 10, 300, 44, 80}

    #  * string
s = {100,300,80,10}
s.update("welcome")        # here string are seperately add induvidualy
print(s)                   # {'c', 100, 'w', 'e', 10, 300, 80, 'o', 'l', 'm'}

# remove() :- remove the specific value

r = {9,4,2,3,6}
r.remove(9)
print(r)                   # {2, 3, 4, 6}

"""
r1 = {9,4,2,3,6}
r1.remove(100)            # here 100 not set value so give keyError
print(r1)                 # KeyError: 100

"""
# discard() :- remove the specific value

d = {9,4,2,3,6}
d.discard(2)              # same as remove() method
print(d)  

"""
d1 = {9,4,2,3,6}
d1.discard(100)           # here not give error this is the defference of remove and discard  
print(d1)                 # {2, 3, 4, 6, 9}

"""

# pop() :- if going to remove anyone of the value from set

p = {11,32,45,62}
p.pop()                   # here any one vlaue remove from set 
print(p)                  # {11, 45, 62}

# clear() :- it will clear all set value

c = {100,200,300,400}
c.clear()                   
print(c)                  # set()

# sorted() :- sort the values in ascending order

s = {9,2,3,1,5}
s1 = sorted(s)
print(s1)                 # [1, 2, 3, 5, 9]

# union() :- joining the two sets

n1 = {1,9,3,4,5,2}
n2 = {9,8,5,3,6,7}
n3 = n1.union(n2)
print(n3)                 # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# intersection() :- it returns the common values

i = {0,2,4,6,8}
i1 = {9,5,4,7,0}
i3 = i.intersection(i1)
print(i3)                 # {0, 4}

# difference() :- 

d = {15,10,100}
d1 = {10,15,20}
d2 = d.difference(d1)  # here same values are remove but remaining will print from 'd' not in 'd1'
print(d-d1)            # {100}
print(d2)              # {100}                 

# symmetric difference() :- 

d = {15,10,100}
d1 = {10,15,20}
d2 = d.symmetric_difference(d1)    # here same values are remove but remaining will print from 'd' and in 'd1'
print(d ^ d1)                      # {100,20}
print(d2)                          # {100,20}

# copy() :-

c = {9,4,5,2,1}
c1 = c.copy()
print(c)                           # {1, 2, 4, 5, 9}

# To compare two sets 

n1 = {9,2,3,4}
n2 = {4,3,9,2}
print(n1 == n2)                    # True

# To check the value is present or not in set

n2 = {9,2,35,64}
print(64 in n2)                    # True

# convert anything into set

#  * int :- this is not convert into set because int is immutable then this single value so.

"""
a = 10
b = set(a)
print(b)

"""

#  * float :- this is not convert into set because float is immutable then this is single value so.

"""
f = 10.3
f1 = set(f)
print(f1)

"""

#  * string :- this is  convert into set. string also immutable but  they have sequence of value so.

s = "Welcome"
s1 = set(s)
print(s1)                   # {'l', 'W', 'e', 'o', 'c', 'm'}

# * list :- list also convert into set

l = [3,5,6,9]
l1 = set(l)
print(l1)                   # {9, 3, 5, 6}

# iteration :-

s = {91,43,233}
for i in s:
    print(i)               # 233 91 43  (top - bottom)







