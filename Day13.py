
#task---->1
'''
String = input("Enter a string: ")
print("Upper: ",String.upper())
print("Lower: ",String.lower())
print("Title: ",String.title())
print("Capitalize: ",String.capitalize())
print("Swapcase: ",String.swapcase())
'''
#task----->1
'''
x=input("Enter a Sentance")

if x.isupper():
    print("The original text is entirely in UPPERCASE.")
elif x.islower():
    print("The original text is entirely in lowercase.")
elif x.istitle():
    print("The original text is in Title Case.")
else:
    print("The original text is in a mixed or uncategorized case.")

y=['upper','lower','title','capitalize','swap']
for i in y:
    if i=='upper':
        print('Upper: ',x.upper()) 
    elif i=='lower':
        print('lower: ',x.lower())
    elif i=='title':
        print('title: ',x.title())
    elif i=='capitalize':
        print('capitalize: ',x.capitalize())
    elif i=='swap':
        print('swap: ',x.swapcase())
'''
x=input("Enter names")
while x!="quit":
    if x.isalnum():
        print('contains only letters and numbers')
    else:
        print('does not contains only letters and numbers')
    if x.isalpha():
        print('begins with letters')
    else:
         print('Not begins with letters')
    if x.isascii():
        print('Contains only ASCII characters')
    else:
        print('Not Contains only ASCII characters')
    if x.isidentifier():
        print("Valid python identifier")
    else:
         print(" Not a Valid python identifier")
    x=input("Enter names")

























        
    

























    




