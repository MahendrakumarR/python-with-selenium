
# Inheritance
# Types of Inheritance

"""

QUESTIONS(Theory)
--------------

What is meant by inheritance?

    Inheritance allows a class to acquire properties and behaviors of another class.

Types of inheritance and explain all types?

    Single Inheritance: A class inherits from one superclass.
    
    Multiple Inheritance: A class inherits from more than one superclass.
    
    Multilevel Inheritance: A class is derived from another derived class.
    
    Hierarchical Inheritance: Multiple classes inherit from a single superclass.
    
    Hybrid Inheritance: A combination of two or more types of inheritance.

What is meant by Super Class?

    A superclass is the class from which other classes inherit.

Difference between hybrid and hierarchical inheritance?

    Hybrid inheritance combines multiple inheritance patterns, while hierarchical inheritance involves multiple subclasses inheriting from a single superclass.

What is meant by Sub Class?

    A subclass is a class that inherits from another class (superclass).

Difference between Multilevel and Multiple inheritance?

    Multilevel inheritance has a chain of inheritance, while multiple inheritance involves a class inheriting from more than one superclass.

Give diagrammatic representation of each type of inheritance?

    Single Inheritance:

        Superclass  
            ↓  
        Subclass

    Multiple Inheritance:

        Superclass1  Superclass2  
             ↓           ↓  
               Subclass

    Multilevel Inheritance:

        Superclass  
            ↓  
        Intermediate Class  
            ↓  
        Subclass

    Hierarchical Inheritance:

        Superclass  
            ↓      ↓  
        Subclass1  Subclass2

    Hybrid Inheritance:

        Combination of the above patterns

Write Syntax of Inheritance?

    class ChildClass(ParentClass):
        # class body

In multilevel inheritance, intermediate class will contain how many class properties?

    It contains properties from both its superclass and its own.

"""
"""
QUESTIONS(Programs)
--------------------
QUESTION 1:
------------
    Description:
    create all class methods into the Languageclass [derived class]  using multilevel inheritance.

     package name: org.all
     Project name: LanguageDetails

     Class name  : Languageclass
     Methods     : all_Language

     Class name  : Tamil
     Methods     : tamil_Language
  
     Class name  : English
     Methods     : english_Language

     Class name  : Telgu
     Methods     : telugu_Language

"""

class Languageclass:
    def all_Language(self):
        print("This block contain all languages")
class Tamil(Languageclass):
    def tamil_Language(self):
        print("This is Tamil language block")
class English(Tamil):
    def english_Language(self):
        print("This is English language block")
class Telugu(English):
    def telugu_Language(self):
        print("This is Telugu language block")

T = Telugu()                                        
T.all_Language()                                    # This block contain all languages
T.tamil_Language()                                  # This is Tamil language block
T.english_Language()                                # This is English language block
T.telugu_Language()                                 # This is Telugu language block

"""
QUESTION 2:
------------
Description:
create all class methods 
Assume India as Parent Class and all class as Derived Class Using Hierarchical Inheritance

     package name: org.india
     Project name: SouthIndia

     Class name  : India
     Methods     : india

     Class name  : TamilNadu
     Methods     : tamil_Language

     Class name  : kerala
     Methods     : malayalam

     Class name  : AndhraPradesh
     Methods     : telugu

"""
class India:
    def india(self):
        print("This block contain India")
class TamilNadu(India):
    def tamil_language(self):
        print("This is Tamil language block")
class Kerala(India):
    def malayalam(self):
        print("This is Malayalam language block")
class AndhraPradesh(India):
    def telugu(self):
        print("This is Telugu language block")
    
a = AndhraPradesh()
a.india()
a.telugu()

k = Kerala()
k.malayalam()

t = TamilNadu()
t.tamil_language()

"""
QUESTION 3:
-------------
Description:
create above 4 class methods 
Assume Student as derived class and all class as Parent class using Multiple inheritance.

     Project   :CollegeInformation
     Package   :org.college

     Class     :College
     Methods   :college_Name(),college_Code(),college_Rank()

     Class     :dept
     Methods   :dept_Name()

     Class     :Student
     Methods   :student_Name(),student_Dept(),student_Id()

"""
class College:
    def college_Name(self):
        print("Your College Name here")
    def college_Code(self):
        print("Your College code here")
    def college_Rank(self):
        print("Your College Rank here")

class dept:
    def dept_Name(self):
        print("Your College Departments")

class Student(College,dept):
    def student_Name(self):
        print("Enter Student Name")
    def student_Dept(self):
        print("Enter Student Department")
    def student_Id(self):
        print("Enter Student Id")

s = Student()
s.student_Name()
s.student_Dept()
s.student_Id()
s.dept_Name()
s.college_Rank()
s.college_Code()
s.college_Name()

"""
QUESTION 4:
-----------
Description:
create above 2 class 
Assume Desktop as derived class and computer class as Parent Class using single inheritance.

     Project   :COmputer
     Class     :Computer
     Methods   :computer_Model()

     Class     :Desktop
     Methods   :desktop_Size()

"""
class Computer:
    def computer_Model(self):
        print("Your Computer Model")
class Desktop(Computer):
    def desktop_Size(self):
        print("Your Desktop size is")

d = Desktop()
d.desktop_Size()  
d.computer_Model()


# ------------------------------ End -----------------------------------------



