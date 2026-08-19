#variable length argument (*args)---->the no of positional arguments are not limited.We can pass any no of args
#but , we need to use the star(*) representation


def simple(*args):
    """ simple demo"""
    print(args)
    print(type(args))
    print(len(args))
simple()
simple(1,2,3,6,5)
simple('jaya','chandra',21)
simple([52,20,63,96],[52,63],'cndf')


a,b,c=13,45,78
print(a,b,c)
a,*b,c=1,2,3,4,5,6,9,87,8,9
print(a,b,c)


a,*b,c=34,52
print(a,b,c)




'''
#task--->we want to calculate sum of objectives
def adding(*args):
    """sum of given numbers"""
    sum=0
    for i in args:
        if type(i)==str:        # or type(i) <class 'int'>
            continue
        sum=sum+i               # or if type(i) in (int,float,complex)
    print(sum)
adding(52,52,85,'jaya','chandra')
'''


'''
def add(*a):
    """sum of given objects"""
    print(a)
    print(type(a))
    #take output variable as result
    result=0
    for i in a:
        #print(i)
        #if type(i)==int or type(i)== float or type(i) == complex:
         if type(i) in (int,float,complex):
            result=result+i
    return result
#print(add())
#print(add(12,3,4,5))
#print(add(1,2,3,4.5))
#print(add(20,24,25))
print(add(3,4,5,'poll','dear',4.5))
print(add(23,4,5.5,2+4j,56,'code',23))
b=list(map(int,input("Enter the values:").split(',')))
print(add(*b))          # * is used to unpack the values

# print(b)
#print(*b)         # it returns each value side by side

for i in b:
    print(i,end=' ')   #same as here
'''

#keyword variable length arguments----> We can pass any number of keyword arguments we use **args and it stores int dictionary

def details(**kwargs):
    print(kwargs)
    print(type(kwargs))
details()
details(name='jaya',score=100,age=20)
b={"name":'chandra',"score":95,"age":21}
details(**b)
    


def sample(*a,**b):
    """Usage of both Variable length and keyword variable length argument"""
    result = 0
    for i in a:
        if type(i) in (int,float,complex):
            result+=i
    print(result)
    for key,value in b.items():
        print(f'key is {key}')
        print(f'value is {value}')
sample(2,2,5,8,'jaya',name='jaya',age=52,score=85)












































