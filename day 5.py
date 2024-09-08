# Operators
"""
1.Arithmetic Operator
2.Relational Operator (or) Comparision Operator
3.Equality Operator
4.Logical Operator
5.Special Operator
6.Assignment Operator
7.Bitwise Operator

"""
"""
What are operators in Python?
    
    Operators are symbols that perform operations on variables and values.

What are the arithmetic operators in Python?

    The arithmetic operators in Python are +, -, *, /, %, **, and //.

What is the assignment operator with example?

    The assignment operator = assigns a value to a variable, e.g., x = 5.

How can the ternary operators work in Python?

    Ternary operators in Python use the syntax x if condition else y.

Mention the use of // operator in Python?

    The // operator performs floor division, returning the largest integer less than or equal to the division result.

What do you mean by relational operator?

    Relational operators compare values and return True or False, e.g., ==, !=, >, <, >=, <=.

How do you use comparison operators in Python?

    Comparison operators like ==, !=, >, <, >=, <= are used to compare two values.

What are the logical operators possible in Python?

    The logical operators in Python are and, or, and not.

Can we use && in Python?

    No, Python uses and instead of && for logical AND operations.

What is Membership operator?

    Membership operators in and not in check for membership in a sequence, like lists or strings.

What is the difference between / and // in Python?

    / performs floating-point division, while // performs floor division.

Does the relational operator work for complex numbers?

    No, relational operators do not work with complex numbers in Python.

What arithmetic operators are supported by the string datatype?

    The + operator (concatenation) and * operator (repetition) are supported by strings.

Is post-increment/decrement possible in Python?

    No, Python does not support post-increment (++) or post-decrement (--).

What is meant by chaining of relational operators?

    Chaining relational operators means combining multiple comparisons, e.g., 3 < x < 7.

"""
"""
QUESTION 1:
-------------------
QUESTION 1.1:
-------------------
Description : Perform following  arithmetic operator and return value
a=9
b=4
i)a+b       ii)a-b      iii)a*b      iv)a/b     v)a%b     vi)a//b

"""
a,b = 9,4.8
print(a+b)      # 13.8
print(a-b)      # 4.2
print(a*b)      # 43.199...
print(a/b)      # 1.875
print(a%b)      # 4.2
print(a//b)     # 1.0

"""
QUESTION 1.2: 
------------------
Description : Perform following  arithmetic operator and return value
              a=20+2j
              b=5+5j

              i)a+b       ii)a-b      iii)a*b      iv)a/b     v)a%b     vi)a//b
"""
a,b = 20+2j,5+5j
print(a+b)        # (25+7j)
print(a-b)        # (15-3j)
print(a*b)        # (90+110j)
print(a/b)        # (2.2-1.8j)
#print(a%b)       # TypeError: unsupported operand type(s) for %: 'complex' and 'complex'
#print(a//b)      # TypeError: unsupported operand type(s) for //: 'complex' and 'complex'

"""
QUESTION 1.3:
------------------
Description : Perform following  arithmetic operator and return value
              x=False
              y=True

              i)x+y       ii)x-y      iii)x*y      iv)x/y     v)x%y     vi)x//y
"""
x,y = False,True
print(x+y)      # 1
print(x-y)      # -1
print(x*y)      # 0
print(x/y)      # 0.0
print(x%y)      # 0
print(x//y)     # 0

"""
QUESTION 1.4:
------------------
Description : Perform following  arithmetic operator and return value
              a='mahendra'
              b='kumar'

              i)a+b       ii)a-b      iii)a*b      iv)a/b     v)a%b     vi)a//b
"""
a,b = "mahendra","kumar"
print(a+b)       # mahendrakumar
#print(a-b)      # TypeError: unsupported operand type(s) for -: 'str' and 'str'
#print(a*b)      # TypeError: unsupported operand type(s) for -: 'str' and 'str'
#print(a/b)      # TypeError: unsupported operand type(s) for -: 'str' and 'str'
#print(a%b)      # TypeError: not all arguments converted during string formatting
#print(a//b)     # TypeError: unsupported operand type(s) for //: 'str' and 'str'

"""
QUESTION 1.5:
------------------
Description : Perform following  relational operator and return value
              x=6
              y=3
   
              i)x<y       ii)x <= y      iii)x>y      iv)x>=y   
"""
x,y=6,3
print(x<y)       # False
print(x<=y)      # False
print(x>y)       # True
print(x>=y)      # True
