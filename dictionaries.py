# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Simple Dict

person = {
    'first_name' : 'John',
    'last_name' : 'Doe',
    'age' : 30
}

print(person)


person2 = dict(first_name = 'John', last_name = 'Doe', age = 30)
print(person2)


# Access value
print(person['first_name'])
print(person.get('last_name'))

# Add key Value
person['phone'] = '555-555-5555'

# Get keys
print(person.keys())

# Get Values
print(person.items())

# Maek copy
person3 = person.copy()
person3['city'] = 'Boston'
print(person3)

# Remove item
# del(person2 ['age'])
# person2.pop('phone')

# Clear
person2.clear()

# Get Length
print(len(person3))

# List of Dict
people = [
    {'name': 'Martha', 'age': 40},
    {'name': 'Bob', 'age': 20}
]
print(people)
print(people[1]['name'])

print(person)