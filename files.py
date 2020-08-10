# Python has functions for creating, reading, updating, and deleting files.

# open a file
myFile = open('myfile.txt', 'w')

# Get some info
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

myFile.write('I love python')
myFile.write(' and JaveScript')
myFile.close()

# open again and Append to file
myFile = open('myfile.txt', 'a')
myFile.write(' I also like PHP')
myFile.close()

# Read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(10) # will read first 10 character
print(text)

