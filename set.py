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

# pop() :- if going to remove anuone of the value from set

p = {11,32,45,62}
p.pop()                   # here any one vlaue remove from set 
print(p)                  # {11, 45, 62}



