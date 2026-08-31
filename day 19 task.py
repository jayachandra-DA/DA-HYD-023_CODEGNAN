# Task-1
'''
def grade_calculation(a):
    if a>=0 and a<=100:
        if a>=80:
            return f"Marks={a}.You obtain A Grade"
        elif a>=60:
            return f"Marks={a}.You obtain B Grade"
        elif a>=40:
            return f"Marks={a}.You obtain C Grade"
        else:
            return f"Marks={a}.You are Fail"
    else:
        return "Negative and greater than 100 numbers are not allowed"
for i in range(3):
    a=int(input("Enter your Marks: "))
    print(grade_calculation(a))
'''
#Task-2
'''
def bill_calculation(prize,quantity=1,discount=0):
    total=prize*quantity
    total=total-total*discount/100
    return total
a=int(input("Enter the Prize"))
print(bill_calculation(quantity=2,prize=a))
print(bill_calculation(prize=a))
print(bill_calculation(discount=20,quantity=2,prize=a))
'''
#Task-3
'''
def calculate_BMI(weight,height):
    BMI=weight/height**2
    return BMI
def BMI_status(value):
    if value<=18.5:
        return 'Under Weight'
    elif value<=24.9:
        return 'Normal'
    elif value<=29.9:
        return 'Over Weight'
    elif value>=30:
        return 'Obese'
    else:
        return "Weight and Height sholud n't be Negative"
for i in range(3):
    name=input("Enter Your Name: ")
    weight=float(input("Enter your weight in kliograms: "))
    height=float(input("Enter your height in meters: "))
    value=calculate_BMI(weight,height)
    print('Name is:',name)
    print("your BMI Value is: %.2f"%(value))
    print("BMI Status is: ",BMI_status(value))
    
'''
#Task-4
def marks_summary(*a):
    total=0
    for i in a:
        if i==0:
            break
        total+=i
    if len(a)!=0:
        avg=total/len(a)
    else:
        print(" ")
    return total,avg       

   
print(marks_summary(20,30))
print(marks_summary())



            
        
    

































































