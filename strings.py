# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Brad'
age = 37

# String Formatting
# print('Hello I am ' + name + ' and I am ' + age)  # will be error because 'age' is int

print('Hello I am ' + name + ' and I am ' + str(age))

# Arguments by position
print('{}, {}, {}'.format('a','b','c'))

print('{1}, {2}, {0}'.format('a','b','c'))

# Arguments by name
print('My name is {name} and I am {age}'.format(name='Brad', age='37'))


# f-strings
print(f'My name is {name} and I am {age}')


# String Methods

s = 'hello there world'

# Capitalize first letter
print(s.capitalize())

print(s.upper())

print(s.lower())

print(s.swapcase())


# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub)) 

