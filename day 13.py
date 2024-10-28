
# Class,Method,Object
# Constructor
# Object aliasing

"""
What is a class?

    A class is a blueprint for creating objects that define attributes and methods.

What is a method?

    A method is a function defined within a class that operates on the instance of the class.

What is an object?

    An object is an instance of a class containing data and behavior defined by the class.

What is the difference between a function and a method?

    A function is independent and can be called anywhere, while a method is associated with an object and called on it.

What is the syntax of a class?

    class ClassName:
        def method(self):
            pass

What is self?

    self refers to the instance of the class, allowing access to its attributes and methods.

What is a constructor?
    
    A constructor is a special method called when an object is created, used to initialize the object's state.

What is the reason for a constructor?

    The constructor sets up the initial state of an object when it is created.

What is object aliasing?

    Object aliasing occurs when multiple variables reference the same object.

Are objects in object aliasing stored at different locations?

    No, aliased objects are stored at the same memory location.

What is the syntax for a constructor?

    def __init__(self, parameters):
        # Initialization code

What is a special variable?

    Special variables like __name__ or __init__ have a special meaning in Python.

Is there any restriction for passing arguments in methods?

    There is no restriction, but the first argument must refer to the instance (commonly self).

In which order will methods execute?
    
    Methods execute in the order they are called.

"""
"""
QUESTION 1:
-----------
     Class     :Employee 
     Methods   :emp_Id(),emp_Name(),emp_Dob(),emp_Phone(),emp_Email(),emp_Address()

Description: Create an object for employee class and call above methods 

"""
"""

class Employee:

    def emp_Id(id):
        print("Employee Id is :",id)

    def emp_Name(name):
        print("Employee Name is :",name)

    def emp_Dob(dob):
        print("Employee Dob is :",dob)
    
    def emp_Phone(phone):
        print("Employee Phone Number is :",phone)

    def emp_Email(email):
        print("Employee Email is :",email)
        
    def emp_Address(address):
        print("Employee Address is :",address)

obj = Employee()

obj.emp_Id(9847)
obj.emp_Name("MahendraN")
obj.emp_Dob("21.10.2001")
obj.emp_Phone(9876543210)
obj.emp_Email("mahe@gmail.com")
obj.emp_Address("Erode")

"""

"""
QUESTION 2:
-----------
     Class     :GreensTech
     Methods   :greens_Omr(id),greens_Adayar(name),greens_Tambaram(address),greens_Velacherry(count)

Description: Create an object for GreensTech class and call above methods and also pass the arguments
"""
"""
class GreensTech:

    def greens_Omr(self,id):
        print(f"The id is {id}")

    def greens_Adayar(self,name):
        print(f"The name is {name}")
    
    def greens_Tambaram(self,address):
        print(f"The address is {address}")

    def greens_Velacherry(self,count):
        print(f"The count is {count}")
gt = GreensTech()

gt.greens_Omr("12345")
gt.greens_Adayar("Adayar")
gt.greens_Tambaram("chennai")
gt.greens_Velacherry("6")

"""
"""
Question 3:
-------------
Description : Find the output
class Employee_details:
      def __init__(self):
          print("constructor")

      def add(self):
          print("add")

d = Employee_details()
d.add()

"""
"""
class Employee_details:
      def __init__(self):
          print("constructor")

      def add(self):
          print("add")

d = Employee_details()
d.add()

"""

"""
Question 4:
-------------
Description : Find the output

class Employee_details:
      def __init__(self,id,name,email):
          self.id=id
          self.name=name
          self.email=email

      def add(self):
          print(self.id)

d = Employee_details(10,"vel","vel@gmail.com")
d.add()

"""
"""
class Employee_details:
      def __init__(self,id,name,email):
          self.id=id
          self.name=name
          self.email=email

      def add(self):
          print(self.id)

d = Employee_details(10,"vel","vel@gmail.com")
d.add()

"""
"""
Question 5:
-------------
Description : Find the output

class Employee_details:
      def __init__(self,id,name,email):
          self.empid=id
          self.empname=name
          self.empemail=email
      def getId(self):
          print(self.empid)
      def getName(self):
          print(self.empname)
      def getemail(self):
          print(self.empemail)
d = Employee_details(10,"vel","vel@gmail.com")
d.getId()
d.getName()

"""
"""
class Employee_details:
      def __init__(self,id,name,email):
          self.empid=id
          self.empname=name
          self.empemail=email
      def getId(self):
          print(self.empid)
      def getName(self):
          print(self.empname)
      def getemail(self):
          print(self.empemail)
d = Employee_details(10,"vel","vel@gmail.com")
d.getId()
d.getName()

"""

# ------------------------------ End -----------------------------------------



