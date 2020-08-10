# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# simple tuple

fruit_tuple = ('Apple', 'Orange' ,'Mango')

# Using constructor
# fruit_tuple = tuple (('apple', 'orange', 'mango'))

# print(fruit_tuple)
# print(fruit_tuple[1])

# fruit_tuple[1] = 'Grape' # cannot change


# Tuples with one  value should have trailing comma
# fruit_tuple_2 = ('Apple', )
# print(len(fruit_tuple_2))



# A Set is a collection which is unordered and unindexed. No duplicate members.

fruit_set = {'Apple', 'Orange', 'Mango', 'Apple'}
print(fruit_set)

# Check if in set
print ('Apple' in fruit_set)

# Add to set
fruit_set.add('Grape')

# Remove from set
fruit_set.remove('Grape')

# Clear set
fruit_set.clear()

# Delete set
del fruit_set