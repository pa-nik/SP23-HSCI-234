# relational operators compare value on the right and left
# the result of this comparison is a keyword True or False
x = 0
y = 1
print(x == y)  # False because x is not equal to y
print(y == 1)  # True because y is equal to 1
print(x > y)   # False because x is not greater than y
print(x != y)  # True because x is not equal to y
print(x <= 0)  # True because x is less or equal to zero

# logical operators (and, or, not) combine value on the right and left
# the result is the keyword True or False
x = True
y = False
# and operator is True if both x AND y are True, False otherwise
print(x and y) # prints False
# or operator is True if either x OR y are True, False otherwise
print(x or y) # prints True
# not operator makes True into False and vice versa
print(not x) # prints False

# example of using logical operators with numbers:
x = 5
print(x > 0 and x < 10)  # True because x is more than 0 and less than 10
print(x < 0 or x < 10)  # True because x is either less than 0 or less than 10

# modulus operator gives the remainder of dividing 2 values:
print(20 % 3)  # remainder of 20 / 3 is 2
print(21 % 3)  # remainder of 21 / 3 is 0
print(21 % 2)  # remainder of 21 / 2 is 1 

# examples of conditional statements using if:
x = 5
if(x > 0):
    print('x is positive')
y = -5
if(y < 0):
    print('y is negative')
z = 0
if(z == 0):
    print('z is zero')

# example of conditional statement with if and else:
if(x % 2 == 0):
    print('x is even')
else:
    print('x is odd')

# example of conditional statement with if, elif, else:
y = 10
if(x > y):
    print('x is greater than y')
elif(x < y):
    print('x is less than y')
else:
    print('x is equal to y')

# nested conditional statement:
if(x == y):
    print('x is equal to y')
else:
    if(x > y):
        print('x is greater than y')
    else:
        print('x is less than y')

# example of a local variable inside a function:
def my_function():
    my_variable = 1
    print(my_variable)

my_function()  # call the function to run it
# my_variable is a local variable inside my_function
# it is created when my_function is run and destroyed when it is finished
# that means we can't use my_variable outside of my_function
# print(my_variable)  # results in an error

# example of a global variable:
my_global_variable = 0

def my_function():
    global my_global_variable  # tell Python to use my_global_variable
    my_global_variable = 1

my_function()
# this time we can use my_global_variable because it exists outside of functions
print(my_global_variable)  # prints 1