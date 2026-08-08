'''
i=0
num=123
while True:
    x=int(input("Guess the number: "))
    if num==x:
        print("your guess is correct")
        break
    elif x>123 and x<150:
        print("you are too close but you have to decrease the number")
    elif x<123 and x>100:
        print("you are too close. Increase the number")
    else:
        print("wrong guess")


i=0
num=123
while i<7:
    x=int(input("Enter OTP: "))
    if num==x:
        print("Login sucess")
        break
    elif i==6:
        print("max attempts")
        break
    else:
        i+=1
        print("wrong OTP")


items=0
while True:
    x=input("Enter the item:")
    if x!='exit':
        items+=1
    else:
        print('total items:',items)
        break
'''
attempts=3
while attempts<=3:
    x=input3("Enter goal or not")
    if x=='goal':
        print("gooooooooal")
        print(f'you have {attempts} more left')
        attempts-=1
    elif attempts==3:
        
    



















