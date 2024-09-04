# def (function)

"""
What is meant by functions in Python?

    Functions are reusable blocks of code that perform a specific task.

What are the types of functions?
    
    Built-in functions, user-defined functions, lambda functions, and recursive functions.

How will you declare the functions?

    Using the def keyword followed by the function name and parentheses.

How many values will it return?

    A function can return zero or more values.

What is the use of * operator in Python functions?

    It allows for variable numbers of positional arguments.

What is a lambda function in Python?

    An anonymous function defined with the lambda keyword.

What is a recursive function?

    A function that calls itself to solve a problem.

What is an anonymous function?

    A function without a name, typically created using lambda.

What is the difference between filter() and map()?

    filter() applies a function to elements and returns those that satisfy a condition, while map() applies a function to all elements and returns a list of results.

What is reduce() and in which module is it present?

    reduce() is a function that performs a cumulative operation on a list, and it is present in the functools module.

What is the keyword used for function declaration?
    def

What is the use of ** operator in Python functions?

    It allows for variable numbers of keyword arguments.

What is the difference between * and ** in functions?

    * is for positional arguments, while ** is for keyword arguments.

Can we change the value of a global variable?

    Yes, using the global keyword inside a function.

"""
"""
QUESTION 1:
-----------
QUESTION 1.1:
-------------
Functions  : emp_Id(),emp_Name(),emp_Dob(),emp_Phone(),emp_Email(),emp_Address()

Description: Create the above functions without arguments

"""
def emp_Id():
    print("Enter your Id:")                     # Enter your Id:
def emp_Name():
    print("Enter your Name:")                   # Enter your Name:
def emp_Dob():
    print("Enter your Date of Birth:")          # Enter your Date of Birth:
def emp_Phone():
    print("Enter your Phone Number:")           # Enter your Phone Number:
def emp_Email():
    print("Enter your Email id:")               # Enter your Email id:
def emp_Address():
    print("Enter your Address:")                # Enter your Address:

emp_Id()
emp_Name()
emp_Dob()
emp_Phone()
emp_Email()
emp_Address()

"""
QUESTION 1.2:
-------------
Functions  : greens_Omr(),greens_Adayar(),greens_Tambaram(),greens_Velacherry(),greens_Anna_Nagar()

Description: Create the above functions with passing some arguments

"""
def greens_Omr(a,b):

    c = a + b
    print(c)                    # 70

def greens_Adayar(a,b):

    c = a * b
    print(c)                    # 1200

def greens_Tambaram(a,b):

    c = a - b
    print(c)                    # 20

def greens_Velecherry(a,b):

    c = a / b
    print(c)                    # 4.5

def greens_Anna_Nagar(a,b):

    c = a % b
    print(c)                    # 10

greens_Omr(30,40)
greens_Adayar(20,60)
greens_Tambaram(40,20)
greens_Velecherry(90,20)
greens_Anna_Nagar(10,89)

"""

"""
