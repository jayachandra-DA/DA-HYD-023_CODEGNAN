'''
squences------>strings,list,tuples and sets.
mapping---->dictionary
'''
#list------------>collection of heterogenous elements(iteams)

marks=[45,20,30,52]
print(marks)
print(len(marks))
print(type(marks))

#operations--->indexing,slising,strding,membership,merging and repetition
#nested list
names=['Codegnan',5,5.0,[8,5,2,6,3,4],50,'chandra']
print(len(names))
print(names[0])
print(names[0][0:8:2])
print(names[3])
names[0]=names[0][::-1]
print(names)
names[3]=names[3][::-1]
print(names)
names[5]=[1,5,6]
print(names)
names[2:4]='chandra'
print(names)
print(len(names))
names=['Codegnan',25,'abhiram','sai','saketh','sairam','DA23',23]
names[3:6:2]='python',"java"
print(names)


names=["jaya",'chandra']
names.append('data')
print(names)    #at a we can append
names.append(['data','movie'])
print(names)
names[3].append(546)
print(names,names.append("append"))#we can't be use in the print functions.it print none
#extend
names=[52,25]
'''
names.extend('jaya')
print(names)
names.extend(['jaya'])
print(names)
'''
names.insert(0,'chandra')
print(names)
#names.insert(0:2,45,52)                     syntax error
#print(names)

#pop()
names.pop()
print(names)
names.pop(1)
print(names)
names=[10,10,15,15,20,20]
names.remove(10)
print(names)
names.remove(10)
print(names)


































































