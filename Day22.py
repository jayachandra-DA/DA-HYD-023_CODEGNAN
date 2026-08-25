'''
class Car_Details:
    name=input("Enter Brand: ")
    price=int(input("Enter Price"))
    colour=input("Enter Colour ")
    
    def details(self):
        print(f"Brand of the Car is {self.name}")
        print(f"Price of the Car{self.price}")
        print(f"Colour of the Car{self.colour}")
u1=Car_Details()
u1.details()
'''
'''
Constructor --> Instance Methods --> Public Attributes
Encapsulation

Constructor --> It is a Special Method (_init_())
which will automatically initialize the attributes and met to the object in the class
'''

'''
class Cars:
    """Understanding the usage of OOP"""
    def __init__(self,Brand,Name,Price,Colour):
        self.Brand = Brand
        self.Name = Name
        self.Price = Price
        self.Colour = Colour
    #Methods(behaviour)
    def details(self):
        print(f"Car Brand is {self.Brand}")
        print(f"Car Model Name is {self.Name}")
        print(f"Car Price is {self.Price}")
        print(f"Car Colour is {self.Colour}")
u1=Cars('Toyota','jaya',52000,'Black')
u1.details()
u2=Cars('TATA','Name',580000,'black')
u2.details()
'''
'''
class Cars:
    """Understanding the usage of OOP"""
    def __init__(self):
        self.Brand = 'TATA'
        self.Name = 'JAYA'
        self.Price = 520000
        self.Colour = 'BLACK'
    #Methods(behaviour)
    def details(self):
        print(f"Car Brand is {self.Brand}")
        print(f"Car Model Name is {self.Name}")
        print(f"Car Price is {self.Price}")
        print(f"Car Colour is {self.Colour}")
u1=Cars()
u1.details()
u2=Cars()
u2.details()
'''
# Encapsulation --> It is One of the main Feature of OOP
# It binds (bundles) the data (Attributes) and the methods (behaviour) into a single unit (class) --> Multiple Objects
# Attributes --> Public, Protected, Private

# Public Attributes --> Attributes defined inside the class (Co) and can be modified outside the class
'''

class CodegnanPortal:
    """Codegnan Portal with Users"""
    def __init__(self,username):
        self.user = username   # Public attribute
    # To Access Student details
    def display(self):
        print(f"Student Username is {self.user}")
U1 = CodegnanPortal("Saketh")
U1.display()
U1.user = "Saketh Kallepu"
U1.display()
print(U1.__dict__)
U2 = CodegnanPortal("Jay")
U2.display()
print(U2.__dict__)
'''
'''
class CodegnanPortal:
    """Codegnan Portal with Users"""
    def __init__(self,username,_OTP):
        self.user = username      # Public attribute # To Access Student details
        self._OTP = _OTP   
    def display(self):
        print(f"Student Username is {self.user}")
        print(f"Student User OTP is {self._OTP}")
U1 = CodegnanPortal("Saketh",2563)
U1.display()
U1._OTP = 5236
U1.display()
'''
'''
class CodegnanPortal:
    """Codegnan Portal with Users"""
    def __init__(self,username,_OTP,__Password):
        self.user = username      # Public attribute # To Access Student details
        self._OTP = _OTP   
        self.__Password = __Password
    def display(self):
        print(f"Student Username is {self.user}")
        print(f"Student User OTP is {self._OTP}")
        print(f"Student User Password is {self.__Password}")
U1 = CodegnanPortal("Saketh",2563,5896112)
U1.display()
U1._OTP = 5236
x=U1.__dict__
for i,j in x.items():
    print(j)
U1.display()
print(U1._CodegnanPortal__Password)

'''

class CodegnanPortal:
    """Codegnan Portal with Users"""
    def __init__(self,__Password): 
        self.__Password = __Password
    def display(self):
        print("Password is: ",self.__Password)
    def get_password(self):
        return "********"
    def set_password(self,new_password):
        if len(new_password)>=8:
            self.__Password=new_password
            print("new password",new_password)
        else:
            print("Password should be 8 charecters")
u1=CodegnanPortal(25631452)
u1.display()
u1.get_password()
u1.set_password('5698')

