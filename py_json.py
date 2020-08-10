# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# sample JSON

userJSON = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# Parse JSON to dict

user = json.loads(userJSON)     # similar to json.parse()

print(user)

print(user['first_name'])

# PArse dict to JSON

car = {'make':'Forst', 'model', 'Mustang', 'year': 1970} 
carJSON = json.dumps(car)
print(carJSON)
