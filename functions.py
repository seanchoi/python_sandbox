# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Create function

def sayHello(name):
    """ comment
    Prints Hello and then name, 
    """
    print('Hello ' + name )

sayHello('Yoori')

def getSum(num1, num2):
    total = num1 + num2
    return total

print(getSum(4,6))

numSum = getSum(2, 4)
print(numSum)

def addOneToNum(num):
    num += 1
    return num

num = 5 # we can set variable num because it's outside of function scope
new_num = addOneToNum(num)
print(new_num)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2 : num1 + num2
print(getSum(9, 2))

