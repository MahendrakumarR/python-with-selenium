# def (function())

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
QUESTION 2:
-----------
QUESTION 2.1:
-------------
Functions  : add(),sub()

Description: Create the above function and pass two arguments and returntype of one value

"""
def add(x,y):
    
    z = x + y
    print(z)            # 127

def sub(x,y):

    z = x-y
    return z 
add(98,29)
s = sub(5,4)
print(s)               # 1

"""
QUESTION 2.2:
-------------
Functions  : calculator()

Description: Create the above function and pass two arguments and  returntype of multiple values

"""
def calculator(x,y):
    add = x + y
    sub = x - y
    mul = x * y
    return add, sub, mul

t = calculator(2,8)
for i in t:
    print(i)                    #  10 -6 16 (top to bottom)

"""
QUESTION 3:
-----------
QUESTION 3.1:
-------------
Description:Find the output for the below function

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Harry")

"""
# def my_function(fname, lname):
#      print(fname + " " + lname)        # TypeError: my_function() missing 1 required positional argument: 'lname'

# my_function("Harry")             

"""
QUESTION 3.2:
-------------
Description:Find the output for the below function

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

"""
def my_function(country = "Norway"):
      print("I am from " + country)   # I am from Sweden | I am from India | I am from Norway | I am from Brazil

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

"""
QUESTION 4:
-----------
Functions  : company_details(),employee_details()

Description: Create the below functions with three arguments with the default return type

"""
def company_details(name,location,industry):

    return {
        "name":name, 
        "location":location, 
        "industry":industry
        }

def employee_details(name,desticnation,salary):
    
    return {
        "name":name,
        "desticnation":desticnation, 
        "salary":salary
    }

company = company_details("Mahendra","Erode","Tech")
print(company)                                                  # {'name': 'Mahendra', 'location': 'Erode', 'industry': 'Tech'}
employee = employee_details("MahendraN","HR","20000")
print(employee)                                                 # {'name': 'MahendraN', 'desticnation': 'HR', 'salary': '20000'}

"""
QUESTION 5:
-----------
QUESTION 5.1:
-------------
Description:Find the output for the below code 

def computer_names(*names):
  print(names)
computer_names(name1="hp",name2="sony",name3="dell")

"""
def computer_names(**names):
    print(names)
computer_names(name1="hp",name2="sony",name3="dell") # {'name1': 'hp', 'name2': 'sony', 'name3': 'dell'}

"""
QUESTION 6:
-----------
Arguments : country_name,area_covered,country_population,no_of_states,no_of_unionterritories

Description: Create a function named as country_details and pass the above arguments 
             print the values one by one

"""

def country_details(country_name,area_covered,country_population,no_of_states,no_of_unionterritories):
    print("Wlecome to :",country_name)                              # Wlecome to : India
    print("Area's covered :",area_covered)                          # Area's covered : 3200
    print("Country population :",country_population)                # Country population : 100000000
    print("No of states :",no_of_states)                            # No of states : 150
    print("No of unionterritories :",no_of_unionterritories)        # No of unionterritories : 30

country_details(country_name="India",area_covered=3200,country_population=100000000,no_of_states=150,no_of_unionterritories=30)

"""
QUESTION 7:
-----------
QUESTION 7.1:
-------------
Description: Create a recursive function of your own and print the word "Welcome"

Output :
--------
Welcome 1
.
.
.
.

"""
def rec():
    print("Welcome")
#    rec()              # recursive function
rec()                   # Welcome..........infinity times(top to bottom)

"""
QUESTION 7.2:
-------------
Description:Create a recursive function of your own and print the word "python" upto 100 times

Output :
--------
python 1
.
.
.
.
python 99

"""
count = 0

def cou():
    global count
    print('Python',count)
    if count == 100:
        return
    count = count + 1
    cou()
cou()                       # python 1 to python 100 (top to bottom)

