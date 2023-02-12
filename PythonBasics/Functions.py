# Lets now to move to function in python

# Basic structure of the function

"""
 def function_name(parameter : data_type) -> return_type:

"""


# A simple function in python

def function():
    print("Hello from function ")

#  Now for a function to run we need to call it 
function()


# Now lets create a function adding two numbers

def add(num1:int, num2:int) -> int:
    num3 = num1 + num2
    return num3

# Now lets call it by passing some arguments

Value = add(2,3)
print(Value)


# Even/odd checker


