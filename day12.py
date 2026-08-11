'''
strings---> case converstion, searching& finding,testing methods,replace, space removal
'''
#searching,finding,replace,joining...
'''
a="jaya chandra"
print(len(a))
print(max(a))
print(min(a))

b=a.index('a')
print(b)
c=a.index('c')
print(c)
d=a.index("a",2)
print(d)
e=a.index("d")
print(e)
'''
#rindex----> gives last occurance
a="jaya chandra"
'''
b=a.rindex('a')       #it gives 11 as output
print(b)
c=a.rindex('n')
print(c)
print(a.count('a'))
'''
#find()
'''
print(a.find('a'))
print(a.find('b'))

'''

count=0
d=0
s='jaya chandra '
b='aeiou'
for i in b:
    if s.find(i)!=-1:
        count+=1
    else:
        d+=1
print(count,d)
'''
#replace

a='jaya chandra'
print(a.replace('c','$'))
print(a.replace(' ','$'))
b=a.replace('c','0')
print(b)
'''
#join()
'''
print(" ".join("jayachandra"))
print("#".join("jayachandra"))
'''
#string testing method (boolean)
'''
a='jaya chandra123'
print(a.isalnum())
print(a.isdigit())
print('26548694169562'.isdigit())
print("30/5".isnumeric())
print(a.islower())
print(a.isupper())
print('jaya'.startswith('j'))

print('jayachandra'.startswith('c',4))

print('jaya'.endswith('a'))
print('Jaya Chandra'.istitle())
'''
#strip
'''
print("    jaya     ".strip())
x=input("Enter a name").strip().upper()
print(x)
'''
#.zfill()
print('123'.zfill(4))
#center()
print('jaya'.center(8,"$"))
print('jaya'.ljust(8,"$"))
print('jaya'.rjust(8,"$"))













































































