total=0
x=int(input())
for i in range(1,x):
    if x%i==0:
        total=total+i
if total==x:
    print("it is a perfect number")
else:
    print("it is not a perfect number")

