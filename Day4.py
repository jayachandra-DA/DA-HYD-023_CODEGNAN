
a=45
b=45
print(id(a))
print(id(b))           #integers are immutable (the storage location is same and does not change)
print(a is b)


a=[50,60,70,80]
b=[50,60,70,80]
print(id(a))  # the list is mutable (in the list we can add or delete the numbers so the storage address
is different  )
print(id(b))
print(a is b)


# Bitwise Operators ----->we perform the bitwise operation on operands
# (& (AND), | (OR), ^(XOR) ))
print(5&6)   
                 # 0  1  0  1
                 # 0  1  1  0
                 #------------
                  #0  1  0  0
print(5|6)
print(5^6)
#left shift operator '<<'
print(5<<1)             #   16 8 4 2 1
                     #5=       0 1 0 1
                     #<<1    0 1 0 1 0
                     #      -----------
                     #          10
                     #      -----------
print(5>>1)



#conditional block statements
#1) conditional statements ------> if ,else and elif
#2) repetional statements ------> for and while
age=int(input("Enter your age: "))
if age<=0:
    print('enter a valuble age')
    if age > 18:
        print(f"Your Age is :{age}. So, You are not Eligible to Vote")
    else:
        print('you are not Eligible')







                            
