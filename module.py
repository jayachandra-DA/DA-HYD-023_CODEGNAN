import Day28
print(dir(Day28))
'''
print(type(Day28.details))
print(type(Day28.greeting))

print(Day28.greeting())
print(Day28.details)

# We can access Functions/Datatypes using . operator

Day28.details['Subjects'] = ['Python','SQL','EDA','PowerBI','Excel']
print(Day28.details.keys())
'''

# we can use 'from' keyword to access desired methods / datatypes
'''
from Day28 import details
print(details)
#print(greeting())  # It raises Name Error, As we did not import 'greeting'

details['Subjects'] = ['Python','SQL','EDA','PowerBI','Excel']
print(details)
'''
'''
from Day28 import details,greeting

print(details)
print(greeting())
'''

# If You want to Access all Functions from a Module at a Time
# * is recommended for user defined modules
'''
from Day28 import *

print(details)
print(greeting())
'''

# Aliasing --> we use 'as' keyword shortcut for original file
'''
import Day28 as mod
print(mod.details)
'''

# We will work on some in-built modules --> random, math....

import random
import time 
# random module --> random number generation, random text
'''print(dir(random))'''

# OTP Generation
'''print(random.randint(1,10))'''
'''
for i in range(5):
    print(random.randint(1000,9999))      # Start Limit, Endlimit
    time.sleep(2)      # delays execution time --> sleep(seconds)
'''

'''print(random.random())     # Returns a Random Float Value'''
'''
details = ["A Long Back",'Once Upon a Time',"Appatloo","Ten Years Back"]
print(random.choice(details))
'''
# You can try for Story Generation using choice --> Try in Practice

# match module --> Mathematical Constants, log, exp, Trignometric.....

import math
#print(dir(math))

'''
print(math.ceil(4.5))     # return the next Integer Value (5)
print(math.floor(4.78))   # return the previous Integer value (4)
print(math.factorial(5))
print(math.pi)
print(math.gcd(5,3))    # returns greatest common divisor
print(math.trunc(4.95))

'''

    