"""
1.Inheritance
2.Types of Inheritance

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

"""