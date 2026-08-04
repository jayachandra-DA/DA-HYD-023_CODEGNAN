'''
conditional statements----------> control flow of excuition of the program
                                ------>condition statements
                                 -----> repetation statements (for, while, for with else, while with else)

                                 ----->jumping statements    (break continue pass )
'''
#syntax
'''
for <tem_var> in sequence / range:
    statement()


for i in range(1,12):
    print("jaya")
for i in range(1,12):
    if i>5 and i%2==0:
        print(f" number ---->{i}")
#range (start, stop, step)

for i in range(2,12,2):
    print(i)
for i in range(-10,0,1):
    print(i)

names=["jaya","chandra","jay"]
for i in range(1,10):
    print(names,i)
'''
'''
#write a program to print sum of first 10 numbers
result=0
for i in range(11):
    result+=i
print(result)
'''
#write a program to print sum of first 10 even numbers
'''
result=0
for i in range(21):
    if i%2==0:
        result+=i
print(result)
'''
highest=0
current=0
work_log=[0,1,1,1,0,1]
for i in work_log:
        if i==1:
            current+=1
            if current>highest:
              highest=current
        else:
          current=0
print(highest)
        
        
        




















