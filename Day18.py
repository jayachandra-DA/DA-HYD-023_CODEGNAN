'''
tokens-->data types
control flow statements----> if,if else,if elif else,for, for else, while,while else


Functions------> Function is a block of code which performs a specific task
advantages-----> it's a reusable,code maintainability, easy of debugging, avoiding code duplication, modularity
'''
# def -------> keyword of functoin
'''
syntax
 def fname(parameters):   #function defination
     """DOC string"""
     statements,,,,,,     #function body 
     ,,,,,,,,,,           
     return value(s)
 fname(arguments)         #funcion call
'''

def add(a,b):
    """sum of numbers"""
    c=a+b
    d=a*b
    return d
print(add(8,5))

'''
def add(a,b):
    print(f"sum={(a+b)}")
add(12,45)
'''
'''
#usage of return
ram_salary,jaya_salary=50000,60000
def add_salary():
    total=ram_salary+jaya_salary
    return total
print(add_salary())
'''
'''
there are 5 types of arguments:
1. positional argument
2. defalut argumrnts
3. keyword arguments
4. variable arguments(*args)
5. keyword variable length arguments(**kwargs)
'''
#1)
def details(name,place):
    ''' store the strings'''
    #name='jaya'
    #place='kadapa'
    return name,place
print(details('a','b'))

#2)
def details(name='jaya'):
    return name
print(details())

def prizes(banana=63,mango=96):
    return banana,mango
print(prizes())

def employee(name,role,place,salary=25000):
    """employee details"""
    print(name,role,place,salary)
employee('data analyst','jay','kadapa')
employee(name='jaya',place='kadapa',role='data analyst')

























































































































