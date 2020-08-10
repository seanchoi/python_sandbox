# A module is basically a file containing a set of functions to include in your application. 
# There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core Modules
import datetime
from datetime import date

import time
from time import time

today1 = datetime.date.today()
today2 = date.today()

timestamp = time()
print(timestamp)

print(today1)
print(today2)

# # pip modules
# import camelcase

# camel = camelcase.CamelCase()
# text = 'hello there wolrd'
# print(camel.hump(text))


# Custome modules
import validator


email = 'test@test.com'
if validator.validate_email(email):
    print('email is valid')
else:
    print('not and email')



from validator import validate_email

if validate_email(email):
    print('email is valid')
else:
    print('not and email')