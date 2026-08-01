'''
#with using 'and' logical operator
marks=int(input('Enter the obtained marks: '))
if marks >=0 and marks<=100:
    if marks>90 and marks<=100:
        print('Grade A')
    if marks>=80 and marks<90:
        print('Grade B')
    if marks>=70 and marks<80:
        print('Grade C')
    if marks>=60 and marks<70:
        print('Grade D')
    if marks>=50 and marks<60:
        print('Grade E')
else:
    print('Marks should not be in Negative and must be in between 0 to 100')
#without using 

marks=int(input('Enter the obtained marks: '))
if marks >0:
    if marks<=100:
        if marks>=90:
            print('Grade A')
        elif marks>=80: 
            print('Grade B')
        elif marks>=70:
            print('Grade C')
        elif marks>=60:
            print('Grade D')
        elif marks>=50:
            print('Grade E')
        else:
            print('Fail')
    else:
        print('Marks should not greater than 100')
else:
    print('Marks should not be in Negative ')



marks=int(input('Enter the obtained marks: '))
if marks >=0:
    if marks<=100:
        if marks>90:
            if marks<=100:
                print('Grade A')
        if marks>=80:
            if marks<90:
                print('Grade B')
        if marks>=70:
            if marks<80:
                print('Grade C')
        if marks>=60:
            if marks<70:
                print('Grade D')
        if marks>=50:
            if marks<60:
                print('Grade E')
else:
     print('Marks should not be in Negative and must be in between 0 to 100')


age=int(input('Enter your age'))
if age>=18 and age<=100:
    print("your are Eligible for vote")
elif age<18 and age>0:
    print('you are not eligible for vote')
else:
    print('enter a positive value')
'''
a,b=20.25896,50
print(a,b,sep=',')
print('his marks are %d'%(a))
print('his marks are %.2f'%(a))
print('his marks are %.f'%(a))
#dot .formate()
print("{} is in {}".format(a,b))
#f string usage
print(f' his marks are {a} so he is fail')



    
        





















    
