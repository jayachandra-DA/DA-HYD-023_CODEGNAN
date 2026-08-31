# List --> Mutable, Ordered, Heterogeneous
# index(), count(), copy(), sort(), reverse()

'''
details = ['Codegnan',7,2018,'Hyderabad']
print(len(details))
print(details.index(7))
print(details.index("Codegnan"))

details.extend([7,21,45,21])
print(details.index(21))        # it returns first occurance

print(details.index(21,6))
# print(details.index('Python'))    # ValueError

print(details.count(21))
print(details.count('Python'))    # it returns 0. As we don't have that element in the List

'''

# copy() --> Shallow copy of the given collection
'''
data = ['Codegnan','Saketh','python','java']
new = data.copy()
print(new)
print(type(new))
print(len(data))

new[2] = "Agentic AI"
print(new)
print(data)

data.append("Varun")
print(data)
print(new)

data.extend(("Sai","Ram",30))
print(data)
print(new)

'''
'''
data = [1,4,5,[21,34,45],23]
print(data)
new = data.copy()
print(new)

new[3][2] = 'Agents'        # Whenever we make changes in nested list, original will also get effected
print(new)
print(data)

new[2] = 'Python'         # But doesn't change the outside elements in original data
print(new)
print(data)

'''
# sort()
'''
marks = [14,24,-45,27,35]
marks.sort()
print(marks)                # return in ascending order
print(marks.sort())       # returns None

marks.sort(reverse = True)       # returns in descending order
print(marks)

marks.reverse()         # reverses the list
print(marks)

'''

# sort() cannot compare int and str
'''
names = ['Varun','Sai','Ram']
names.sort()
print(names)

'''

# type(), len(), max(), min(), print()
'''
print(sorted('Varun'))       # return List in Ascending Order

'''

# Tuples --> Tuples are also Indexed, Ordered, Heterogeneous. and Immutable Collection

# we use them in Dimension, Coordinates, Database records. we use () for tuple notation
'''
a = ()
print(type(a))
print(len(a))

dimensions = 1.5,2.5
print(dimensions)
print(type(dimensions))
print(len(dimensions))
'''

# Operations --> Indexing, Slicing, Striding, Membership, Merging, Repetition
'''
Courses = ('PFS','JFS',('DA','DS'),'AgenticAI',[100,6,6])
print(len(Courses))

print(Courses[3][-2:])    # return AI
'''

# We Cannot change tuples, but can change the list inside a tuple
'''
Courses[-1].append('Codegnan')
print(Courses)

print('PFS' in Courses)

d = Courses * 2  # Repetition
print(d)

e = Courses + (2,3,4,5)   # Merging
print(e)
'''

# Tuples are immutable
'''
Courses = ('PFS','JFS',('DA','DS'),'AgenticAI',[100,6,6])

print(Courses.index('AgenticAI'))      # return first occurance
print(Courses.count('Agents'))

print(sorted(Courses[-1]))

d = tuple(sorted((23,12,3,4,5)))     # Typecasting
print(d)
'''

# Accept group of integers space separated

# eval()
'''
print(eval('9+4'))      # Usually gives output '9+4'. But, as we use "eval", it gives Output 13.

a = eval(input("Enter a List:"))
print(a)
print(type(a))

'''


# TASK --> Take a User input as String, Do this in Two Ways
'''
1) Give the Count of Each Repeating Character
Test Case-1: Programming

r is repeating 2 times
g is repeating 2 times
m is repeating 2 times

2) Different Output

r is repeating 2 times
index = [1,4]
g is repeating 2 times
index = [3,10]
m is repeating 2 times
index = [6,7]

'''










