# Sequences --> Strings, Lists, Tuples, Set, Frozen Set
# Mapping -->Dictionary

# Sets --> A Set is a Unique Collection of Elements (Objects) --> Unordered, Mutable
# Hashing, Unindexed, Unique, Heterogeneous

# set(), {}

# a = {} --> it is an empty dictionary
'''
a = set()
print(type(a))
student_id={20,50,50,23,23}
print(student_id)
print(type(student_id))
print(len(student_id))
print(student_id)

#print(student_id[2])          #type error
#print(student_id*2)             #type error----->set can't be repete
#print(student_id + student_id )  #set can't me merged


#data={52,20,[50,52,52],52,52}    # list can't be in dist or set
data={52,63,41,(52,45,95),'rajesh',52}
print(data)
for i in data:
    print(i)
names={'jaya','chandra','sai','ram',36,78}
print(names)

#add

names.add('python')
print(names)
names.add((50,'rajesh',58))
print(names)
da_names={52,20,36,9,56,3,2,78}

#update

names.update(da_names)
print(names)
print(len(names))
da_names.update(names)
print(da_names)
print(len(da_names))

#remove

name={'jaya','gun','error','chandra'}

name.remove('gun')
print(name)
#name.remove('gun')     it will shows an error there no "gun" in th the set
name.discard('gun')
print(name)         #it doesn't shows error it skips
name.pop()
print(name.pop())
print(name)
name.clear()
print(name)
name={'jaya','gun','error','chandra'}
d=name.copy()
print(d)
d.update([52,50,25,52])
print(d)
'''
#mathematical operations --->
d={52,85,96,3,67,85,63,56}
e={52,63,56,3}
g={52,25,56}
f=d.union(e,g)
print(f)
x=d.intersection(e,g)
print(x)
'''

y=d.intersection_update(e)
print(y)
print(d)

# difference() --> removes common elements and prints remaining elements from first set

diff = da_23.difference(da_24)
print(diff)

      #or

f = da_23 - da_24
print(f)

symm = da_23.symmetric_difference(da_24)
print(symm)

       #or

s = da_23 ^ da_24
print(s)


# issubset() --> checks for all elements to be present in other set

da_24.remove(46)
da_24.remove(47)

print(da_24.issubset(da_23))
print(da_23.issuperset(da_24))

# isdisjoint() --> return False for sets having common elements

print(da_23.isdisjoint(da_24))



# Length of Unique student ids in a class, where user can  enter first input
# He should be giving number of student_ids, He will enter student_ids

n = int(input("Enter No.of Ids: "))
student_ids = input("Enter Student Ids: ").split()

# print(student_ids)

result = set(student_ids)
print(result)
print(len(result))
'''




















































































