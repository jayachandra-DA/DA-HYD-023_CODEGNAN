'''
tokens --> variables,punctuaters
'''
#multi assignment of varibales
name,age,place='jaya',85,'kadapa'
print(name,age,place)
print(name,age,place,sep=',')
'''
a,b=1,2,6
print(a,b)  # value error
'''
a,b=1,2
print(a,b)
a,b=b,a
print(a,b)
'''a,b=b,c
print(a,b)'''  #name error
a=b
c=45
b=c
print(a,b)
'''del a,b
print(a,b)'''   #not defined
name='jaya';age=22;place='516380'
print(name,age,place)
'''data types
        numaric ----> int,float,complex
        sequences---list,touple,sets

'''
age=7
print(age)
print(type(age))
'''age=03
   print(age)'''    #0 is not allowed to before the integer
rise=07.5
print(rise)
print(type(rise))
number=7+10j
print(number)
print(type(number))
'''number=7+j10
print(number)
print(type(number))'''   #not before the number (5+j52)wrong
#boolean ----->True & False
value= True
error=False
print(type(value))    #boolean
print(type(error))
#type casting (or) type convertion
weight=80
print(float(weight))
print(complex(weight))
print(bool(weight))
weight=56.62
print(int(weight))
print(complex(weight))
print(bool(weight))
weight=0+0j
#print(int(weight))
#print(float(weight))
print(bool(weight))
name='jaya'
#print(float(name))
#print(int(name))
print(bool(name))

#combination of bool,int and float

a=int(float(bool(45)))
print(a)
a=bool(float(int(45)))
print(a)
f=1+2+3+5j+True
print(f)













































