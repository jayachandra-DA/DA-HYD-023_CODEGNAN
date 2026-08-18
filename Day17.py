'''
mapping--->dictionary--->collection of key-value pair used to store
related data--->JSON, APIs and database related

dict()--->data={}-->data={key:value}
dict-->mutable,indexed thorough,hetrogenous, key must me unique
'''
details={}
print(type(details))
details={'Id':'CGH4020','Name':'Jaya','Gender':'M','Batch':'DA23','Place':'HYD'}
print(details)
print(len(details))

#Accessing the data from the dict
#print(details[0])
'''
print(details.keys())
print(details['Id'])
'''
#print(details['marks'])   key error
'''
details['marks']=[]
print(details)
print(type(details['marks']))

details['marks'].append(29)
print(details)

details['marks'].extend([20,6,20,30])
print(details)

details['PS']=('Tue','Thus','Sat')
print(details.keys())

details['MI']=('Mon','Wed','Fry')
print('Wed' in details)
print('MI' in details)

for i in details:             #it will print the keys of the dict
    print(f"keys={i}",end=" ")
    
for i in details:
    print(f"values={details[i]}",end=' ')

for i in details.values():
    print(i)

for i,j in details.items():
    print(f"key is:{i} = {j}")

details.update({'marks':[],'PS':('Tue','Thus','Sat')})
print(details)

details['marks'].extend([20,6,20,30])
print(details)

marks=list(map(int,input("Enter the marks:").split()))
details['marks'].extend(marks)
print(details)
'''
print(details.keys())
print(details.get('name'))
print(details.get('branch'))     # it will be print none

print(details.setdefault('branch'))
print(details)
print(details.setdefault('Name'))
details.setdefault('NAME','AKASH')
print(details)


print(details.pop("NAME"))
print(details)
del details['Id']
print(details)
details.clear()
print(details)


data=['name','name','id','branch']
dict=dict.fromkeys(data)
print(dict)
dict['name']='jaya'
print(dict)

b=dict.fromkeys(['name','branch'],['jaya','EEE'])

print(b)






























    












