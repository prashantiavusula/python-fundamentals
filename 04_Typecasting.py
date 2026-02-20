WHAT IS TYPECASTING?
Typecasting is the process of converting a variable from one data type to another. In Python, this is particularly useful when you need to perform operations that require specific data types.
Python supports two main types of typecasting:

Implicit Typecasting (Type Conversion done automatically by Python)
Explicit Typecasting (Type Conversion done manually by the programmer)
_________________________________________________________________________________________________________________________________________________________________________________________________
2. Implicit Typecasting (Type Conversion)
This is also called coercion.
Python automatically converts one data type to another without losing information.
Usually happens when performing operations between different data types.

Rules:
Python follows widening conversion: small data types are converted into larger types automatically.
For example: int → float → complex
a = 5      # int
b = 2.5    # float

c = a + b  # a is automatically converted to float
print(c)   # Output: 7.5
print(type(c))  # Output: <class 'float'>

Explicit Typecasting (Type Conversion)
This is done manually by the programmer using Python’s built-in functions.
Common typecasting functions:

Function	Description
int(x)	Converts x to an integer
float(x)	Converts x to a floating-point number
str(x)	Converts x to a string
complex(x)	Converts x to a complex number
list(x)	Converts iterable x to a list
tuple(x)	Converts iterable x to a tuple
set(x)	Converts iterable x to a set
bool(x)	Converts x to a boolean
_________________________________________________________________________________________________________________________________________________________________________________
AOID TYPECASTING
Types are incompatible.
It can silently lose data or precision.
Strings are non-numeric.
The original meaning or order of data matters.
Performance or memory efficiency is important.

