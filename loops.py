# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['john', 'will', 'janet', 'karen']

for person in people:
    print('Current person: ', person)


#break
for person in people:
    if person == 'janet':
        break
    print('Current person: ', person)

#continue -> skpping
for person in people:
    if person == 'janet':
        continue
    print('Current person: ', person)


# Range
for i in range(len(people)):
    print('Current person: ', people[i])

for j in range(0, 10):
    print('Number ', j)



# While loops execute a set of statements as long as a condition is true.

count = 0
while count <=10:
    print('Count: ', count)
    count += 1
