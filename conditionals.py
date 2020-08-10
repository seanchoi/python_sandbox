# If/ Else conditions are used to decide to do something based on something being true or false

x = 10
y = 16


# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# if x == y:
#     print(f'{x} is equal to {y}')

# Logical operators (and, or, not) - Used to combine conditional statements

# if x > y:
#     print(f'{x} is greater than {y}')
# else:
#     print(f'{x} is less than {y}')


if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'{x} is less than {y}')

if x > 2:
    if x <= 10:
        print(f'{x} is less than 10 and greater than 2')

if x > 2 and x <= 10:
   print(f'{x} is less than 10 and greater than 2')

if x>2 or x <=10:
   print(f'{x} is less than 10 and greater than 2')

if not(x == y):
    print(f'{x} is not equal to {y}')

# if x != y:
    
# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1,2,3,4,5,6]


if x in numbers:
    print(x in numbers) # returns True or False value

if x not in numbers: 
    print(x in numbers)

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

if x is y:
    print(x is y) # returns False

if x is not y:
    print(x is not y) # returns True