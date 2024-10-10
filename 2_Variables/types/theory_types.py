# primitives are the most basic building blocks of Python
# they are the most fundamental data types in Python
# examples of primitives are: int, float, str, bool

a = 5 # int
print(a, type(a))

b = 5.0 # float
print(b, type(b))

c = "5" # str
print(c, type(c))

d = True # bool
print(d, type(d))

f = None # NoneType, this is a special type in Python, it represents the absence of a value
print(f, type(f))

print('-'*20) # separator, don't worry about this, it's just for visual purposes

# Python is a dynamically typed language
# this means that the type of a variable is determined at runtime
# the type of a variable can change during the execution of the program
# so the following is valid in Python

variable = None
print(variable, type(variable))

variable = 5
print(variable, type(variable))

variable = "5"
print(variable, type(variable))

variable = 5.0
print(variable, type(variable))
