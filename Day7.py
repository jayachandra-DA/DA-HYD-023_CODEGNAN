'''
l=[1,0,1,1,1,0,1]
streak=0
highest_streak=0
for i in l:
    if i==1:
        streak+=1
        if streak>highest_streak:
            highest_streak=streak
    else:
        streak=0
else:
    print(highest_streak)

notifiction=[0,0,0,0]
for i in notification:
    if i==1:
        print("unread notification")
        break
else:
    print("all catch up")


notifiction=list(map(int,input("enter values").split(",")))
for i in notification:
    if i==1:
        print("unread notification")
        break
else:
    print("all catch up")
'''
#while-----> it relies on condition, it will be completely excuited until the condition is satisfied
#syntax
'''
while <condition>:
    statement
'''
'''
i=0
while i<=10:
    print(i)
    i+=1

i=0
while i<=9:
    print(10-i)
    i+=1
'''
#bank scenario -------> PIN authentucation if more than 3 attempts
max_attempts=3
attempts=0
while attempts<max_attempts:
    pin=input('enter pin')
    if pin!='1234':
        attempts+=1
    if attempts==max_attempts:
        print("max attempts are over")
    elif pin=='1234':
        print('login succesful')
        break
    
    

    






























    







    
