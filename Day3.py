#input formating--> accepting input from the user --> input()
'''
age=int(input("Enter age: "))
print(age)
print(type(age))
'''

'''
age=float(input("Enter age: "))
print(age)
print(type(age))
'''

'''
age=complex(input("Enter age: "))
print(age)
print(type(age))
'''
'''
#acepting group values
x=input('Enter names: ').split('&')
print(x)


marks=list(map(int,input().split()))
print(marks)

age,marks=(map(int,input('Enter values: ').split()))
print(age)
print(marks)
age,marks=map(float,input("enter your your age and marks: ").split())
print(marks)


#arithmatic operator +,-,*,/,//,%
print(10+5)
print(10-5)
print(10*5)
print(10/5)
print(10//5)
print(10%5)
print(10**5)

length,breadth=map(int,input('enter length and breadth: ').split())
print("area: ",length*breadth)
'''
#assignment operator-----> (+=, -=, =)
'''
a=50
a+=89
print(a)  #increment 

a=50
a-=89
print(a)

a=50
a*=89
print(a)

a=50
a/=89
print(a)

a=50
a//=89
print(a)
'''
#comparission operators -----> (==, !=, <, >, <=, >=)
a=50
print(a==89)

a=50
print(a<=89)


a=50
print(a!=89)


a=50
print(a>=89)


a=50
print(a<89)


a=50
print(a>89)


#membership operators ( is, not is )

a=[25,56,23,89,25]
print(56 in a,23 not in a)

#logic opertators
a=[25,56,23,89,25]
print(56 in a and 23 not in a)

a=[25,56,23,89,25]
print(56 in a or 23 not in a)

a=[25,56,23,89,25]
print((56 in a)not(23 not in a))
 #indentity operators ( is, is not) ----->id()
a=85
b=85
print(a is b)
print(id(a,b))

























