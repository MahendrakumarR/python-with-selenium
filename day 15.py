
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
QUESTION 3:
------------
Description: Perform Operator Overloading Using len() method
             
               s="Greens"
               
               a=[10,20,30,40]

               e=(20,67,99,89,30)

               b={90,40,50,60,70}
"""
s="Greens"              
a=[10,20,30,40]
e=(20,67,99,89,30)
b={90,40,50,60,70}

print("Lenth of s is:",len(s))    # Lenth of s is: 6
print("Lenth of a is:",len(a))    # Lenth of a is: 4
print("Lenth of e is:",len(e))    # Lenth of e is: 5
print("Lenth of b is:",len(b))    # Lenth of b is: 5

"""
QUESTION 4:
------------
     Project   :EmployeeDetails
     Package   :org.emp

     Class     :Employee 
     Methods   :emp_Id()

Description : overload the method emp_Id() based on different Number of arguments

"""
class Employee:
    def emp_Id(self,a):
        print("The Value of a is:",a)
    def emp_Id(self,b):
        print("The Value of b is :",b)
    def emp_Id(self,a,b):
        print("The Value of a is:",a)
        print("The Value of b is :",b)
e = Employee()
# e.emp_Id(12)   TypeError: Employee.emp_Id() missing 1 required positional argument: 'b'
e.emp_Id(12,12)  # The Value of a is: 12  The Value of b is : 12

"""
QUESTION 5:
------------
     Project   :BankDetails
     Package   :org.bank
     Class     :BankInfo
     Methods   :saving(),fixed(),deposit()

     Class     :AxisBank
     Methods   :deposit()

Description: override the method deposit in BankInfo.

"""
class BankInfo:
    def saving(self):
        print("The Curent savings are : 10000")
    def fixed(self):
        print("The fixed is : 1000")
    def deposit(self):
        print("The deposite is : 30000")
class AxisBank(BankInfo):
    def deposit(self):
        print("The deposite is : 60000")
b = BankInfo()
a = AxisBank()

b.saving()          # The Curent savings are : 10000
b.fixed()           # The fixed is : 1000
b.deposit()         # The deposite is : 30000

a.deposit()         # The deposite is : 60000


# ------------------------------ End -----------------------------------------
        