'''
Inheritance----> it is one of the key feature of OPP where the inherit the proprties (attributes/method) from onr class to another
base clas (parent class)-----> derived class (child class)
'''
#Types of Inheritance
#1)single Inheritance (Finger Prints) one parent class have only one child class
#2)Multipule Inheritance (Mothyer and Father) one child class Inheritaning form tow Parent classes
#3)Multivel Inheritance (Grand Father----> Father---->Child)
#4)Hierarchical Inheritance: multipule child class inheritance properties form single parent class
#5)hybrid Inheritance: it carries one or more inheritances

'''
Syntax

Single inheritance

class BasicClass:
    statements
    ,,,,,,,

class DerivedClass(BaseClass):
    ,,,,,,,,,,,,,,
    ,,,,,
'''
'''
class User:
    """Single inheritance Usage"""
    def send_message(self):
        print("Message sent")
    def voice_call(self):
        print("Voice call")
    def veido_call(self):
        print("Veido call")
class ChildClass(User):
    pass
u1=ChildClass()
u1.__dict__

u1.veido_call()
u1.veido_call()

'''
class FirstClass:
    company='codegnan'
    def __init__(self,fname,sname):
        self.fname=fname
        self.sname=sname
    def fullname(self):
        print(self.sname+ ' '+self.fname)
'''   
u1=FirstClass(sname='Jaya Chandra',fname='Giriboina')
print(u1.fullname())
print(u1.company)
'''
class Chandra(FirstClass):
    def __init__(self):
        self.age=52
    def show_age(self):
        print(f"{self.fullname} has age of {self.age}")
u2=Chandra()
u2.show_age()  



class FatherClass:
    def __init__(self):
        self.cash=20000
    def fullname(self):
        print(self.sname+ ' '+self.fname)

class Kid(FatherClass):
    def __init__(self):
        self.property=520000
    def total_property(self):
        print(self.cash)
        print(self.property)
        print(self.cash+self.property)
obj=Kid()
obj.total_property()
