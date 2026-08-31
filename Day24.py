'''
class Father:
    """Usage of Constructor in Single Inheritance"""
    def __init__(self,property):
        self.property = property
    def father_property(self):
        print(f'Father Property is {self.property}')
class Kid(Father):
    """Now Child class will have constructor"""
    def __init__(self,cash,property):
        self.cash = cash
        super().__init__(property)
    def kid_property(self):
        print("Kid Property is",self.cash)
        print("Total Property is",self.property + self.cash)

obj = Kid(250000,1000000)
obj.kid_property()
obj.father_property()
'''
#what if child is have same method as parent class
#Method overriding
'''
class Rectangle:
    """method overriging usage"""
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def rarea(self):
        print(f"the area of the rectangleis{self.x*self.y}")
class Square(Rectangle):
    def __init__(self,x):
        self.x=x
    def area(self):
        print(f"the are of the square is{self.x**2}")
u1=Square(5)
u1.area()
#u1.rarea()              
'''
'''
class Square:
    """method overriging usage"""
    def __init__(self,x):
        self.y=y
    def area(self):
        print(f"the area of the Square{self.x**2}")
class Rectangle(Square):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        super().area()
        print(f"the are of the Reactangle is{self.x*self.y}")
u1=Rectangle(5,2)
u1.area()
'''
#Multiple Inheritance
'''
class Parent1:
    statement
    ,,,,,,,,,
class Parent2:
    statemnet
    ,,,,,,,,
class child(Parent1,Parent2):
    ,,,,,,,
,,,,
'''
'''
class User:
    def voice(slef):
        print("Making voice calls")
class Notification:
    def Notification(self):
        print("Sending notification........")
class Premium_User(User,Notification):
    def verification_badge(self):
        print("Blue ticks")
u1=Premium_User()
u1.verification_badge()
u1.Notification()
u1.voice()
'''
#Multilevel
#Syntax
'''
class Grandd_Parent:
    ,,,,,,,,,,
class Parent(Grand_Parent):
    ,,,,,,,,,
class Child(Parent):
    ,,,,,,,,
'''
'''
class User:
    def voice(slef):
        print("Making voice calls")
class Notification(User):
    def Notification(self):
        print("Sending notification........")
class Premium_User(Notification):
    def verification_badge(self):
        print("Blue ticks")
u1=Premium_User()
u1.verification_badge()
u1.Notification()
u1.voice()
u2=Notification()
u2.voice()
u2.Notification()
u3=User()
u3.voice()
'''
'''
class Parent:
    def __init__(self):
        self.property=500000
        #self.property=property
class Child1(Parent):
    def net1(self,child1_property):
        self.child1_property=child1_property
    def Total(self):    
        print(f"Total Property of Child1: {self.property+self.child1_property}")
class Child2(Parent):
    def net2(self,child2_property):
        self.child2_property=child2_property
    def Total(self):
        print(f"Total Property of Child2: {self.property+self.child2_property}")
class Child3(Parent):
    def net3(self,child3_property):
        self.child3_property=child3_property
    def Total(self):
        print(f"Total Property of Child3: {self.property+self.child3_property}")
Child1=Child1()
Child2=Child2()
Child3=Child3()
Child1.net1(500000)
Child2.net2(200000)
Child3.net3(100000)
Child1.Total()
Child2.Total()
Child3.Total()
'''
class Grandd_Parent:
    def __init__(self):
        self.g_property=200000
class Parent(Grandd_Parent):
    def __init__(self):
        super().__init__()
        self.p_property=500000+self.g_property
        #self.property=property
class Child1(Parent):
    def net1(self,child1_property):
        self.child1_property=child1_property
    def Total(self):    
        print(f"Total Property of Child1: {self.p_property+self.child1_property}")
class Child2(Parent):
    def net2(self,child2_property):
        self.child2_property=child2_property
    def Total(self):
        print(f"Total Property of Child2: {self.p_property+self.child2_property}")
Child1=Child1()
Child1.net1(500000)
Child1.Total()