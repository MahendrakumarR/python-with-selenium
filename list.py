# list
# In-place methods (like extend(), sort(), append(), remove(), etc.) modify the object they are called on and usually return None.
# Non-in-place methods (like count(), sorted(), index(), etc.) return a value (e.g., a new list, count, or index) without modifying the original object

# append()
a = [1,2,3,4]
a.append(5)
print(a)         # [1, 2, 3, 4, 5]

# max()
a = [1,2,3,4]
v = max(a)
print(v)         # 4


# min()
a = [1,2,3,4]
v = min(a)
print(v)         # 1

# extend()
a = [1,2,3,4]
b=[24,53,32]
a.extend(b)     # d = a.extend(b) not work 
print(a)        # [1, 2, 3, 4, 24, 53, 32]

# count()
cou = [10,29,10,32,12,10,10]
count = cou.count(10)
print(count)                    # 4

# clear()
cle = [1,2,3,4,5]
cle.clear()                    # clear = cle.clear()  not work
print(cle)                     # []


# del()
delete = [1,2,3,4,5,6,7,8,9,0]
del delete[1:6]
print(delete)                  # [1, 7, 8, 9, 0]

# reverse()
re = [9,1,2,3,6,7,23]
re.reverse()                   # r = re.reverse() not work
print(re)                      # [23, 7, 6, 3, 2, 1, 9]

# remove()
rem = [9,1,2,3,6,7,23]
rem.remove(6)                 # remo = rem.remove not work  
print(rem)                    # [9, 1, 2, 3, 7, 23]

# index()
ind = [9,1,2,3,6,7,23]
i = ind.index(23)              
print(i)                      # 6

# sort()
sor = [9,1,2,3,6,7,23]
sort = sor.sort()
print(sor)              
print(sort) 

# sort()  reverse()
sor = [9,1,2,3,6,7,23]
sort = sor.sort(reverse=True)
print(sor)              
print(sort) 


# sorted()
sorte = [9,1,2,3,6,7,23]
sorted = sorted(sorte)              
print(sorted)                   # [1, 2, 3, 6, 7, 9, 23]

# in not in
num = [1,2,3,4,5]
print(4 in num)                 # True

num = [1,2,3,4,5]
print(6 not in num)             # True

# check the value is equal or not

n1 = [1,2,3,4,5]
n2 = [1,2,3,4,5]
print(n1 == n2)                 # True

# print one by one 

o = [1,2,3,4,5]
for i in o:
    print(i)                    # 12345  (top - bottom)

o1 = "Welcome"
for i in o1:
    print(i)                   # welcome (top - bottom)

