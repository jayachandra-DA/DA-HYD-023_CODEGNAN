
dot=boundaries=total=0
l=[4,6,1,0,2,3,6,2,0,1,6,6,6,6,6,6]
for i in l:
    total+=i
    if i==4 or i==6:
        boundaries+=1
    elif i==0:
        dot+=1
print('Total Core:',total)
print('Total Dot balls:',dot)
print('Total Boundaries:',boundaries)
      

            
i=0
original_pin=1248
while i<5:
    pin=int(input('Enter the pin'))
    if pin==original_pin:
        print('Log in success')
        break
    elif i==4:
        print("max attempts")
        break
    else:
        print('try again')
        i+=1

i=0
original_pin=1248
while i<3:
    pin=int(input('Enter the ATM pin'))
    if pin==original_pin:
        print('Log in success')
        break
    elif i==2:
        print("max attempts")
        break
    else:
        print('try again')
        i+=1
