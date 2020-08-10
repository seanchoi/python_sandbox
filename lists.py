# A List is a collection which is ordered and changeable. Allows duplicate members.

numbers = [1,2,3,4,5]
print(type(numbers))

# Using a constructor
numbers = list((1,2,3,4,5))


fruits = ['Apple', 'Oranges', 'Grapes', 'Pears', 12]
print(fruits)
print(fruits[1]) # get value: 'oranges'

print(len(fruits))

# Apeend
fruits.append('Mangos')
print(fruits)

# Remove

fruits.remove('Grapes')
print(fruits)

# Insert into specific position
fruits.insert(2, 'Strawberries')
print(fruits)

# Remove from a position
fruits.pop(3)
print(fruits)

# Reverse List
fruits.reverse()
print(fruits)

names = ['yoori','sean', 'michael', 'kim', 'eunice']

# Sort List
names.sort()
print(names)

# Reverse Sort
names.sort(reverse = True)
print(names)