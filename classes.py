# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# create class
class User:
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1



# Init user object
brad = User('Brad Traversy', 'brad@gmail.com', 37)
janet = User('Janet Williams', 'janet@gmail.com', 20)

print(brad.name)
print(brad.age)
print(brad.email)

brad.age = 38
print(brad.age)

print(janet.age)

janet.has_birthday()
print('now I am ', janet.age)


# call method(function) in a class (the name as js)
print(janet.greeting())


class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and I owe a balance of {self.balance}'


# Init Customer

john = Customer('John Doe', 'johdoe@gmail.com', 30)

print(john.name)
john.set_balance(500)
print(john.balance)
print(john.greeting())