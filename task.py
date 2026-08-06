'''
L=list(map(int,input("Enter the cost of the products: ").split()))
total=0
for i in L:
    total=total+i
print(total)


for i in range(len(L)):
    total=total+L[i]
print(total)
'''
'''
u=0
s=0
n=0
l=0
x=input("Enter the password: ")
for i in x:
    if i>=chr(65) and i<chr(92):
        u=u+1
    elif i>=chr(97) and i<=chr(123):
        l=l+1
    elif i>chr(48) and i<chr(57):
        n=n+1
    else:
        s+=1
print("total upper case letters: ",u)
print("total lower case letters: ",l)
print("total decimals: ",n)
print("total special characters: ",u)
'
L=input().split()
for i in L:
    print(L.split("@")[1])
'''
m=['x','y','z']
for i in range(len(m)):
    for j in range(48,58):
        print(chr(j),m[i])
    















