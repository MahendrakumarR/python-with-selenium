
# Polymorphism

"""
What is meant by Polymorphism?

    Polymorphism allows one interface to be used for a general class of actions, enabling multiple forms.

What are Types of Polymorphism?

    Compile-time polymorphism (overloading) and run-time polymorphism (overriding).

What are Types of Overloading?

    Method overloading and operator overloading.

Difference between Operator Overloading and Method Overloading?

    Operator overloading defines custom behavior for operators, while method overloading uses the same method name with different parameters.

Give any 5 Examples of Operator Overloading?

    + (addition), - (subtraction), * (multiplication), [] (indexing), == (equality comparison).

What is Method Overriding and Purpose of Method Overriding?

    Method overriding allows a subclass to provide a specific implementation of a method defined in its superclass to change or extend functionality.

If we use a different method name, will it override or not?

    No, it will not override; overriding requires the same method name.

What is the Difference Between Method Overloading and Method Overriding?

    Overloading is compile-time, same method with different parameters; overriding is runtime, same method with same signature in a subclass.

If a Method is Present in Both Super and Sub Class, Which Logic Will Be Given Importance?

    The subclass method logic is given importance.

"""

"""
QUESTION 1:
------------
Description: Perform Operator Overloading Using +
             
               s="Greens"
               s1="Tech"

               a=10
               b=30

"""
s = "Greens"
s1 = "Tech"
a = 10
b = 30

print(s+s1)     # GreensTech
print(a+b)      # 40

"""
QUESTION 2:
------------
Description: Perform Operator Overloading Using *
             
               s="Python"
               s2 = 3
               a=10
               b=30

"""

s = "Python" 
s2 = 3         
a = 10
b = 30

print(s*s2)   # PythonPythonPython
print(a*b)    # 300

"""

"""