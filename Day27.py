'''
OOP --> Class (Attributes,Methods (Constructor,Instance Method))
Object Creation/Utilisation --> Encapsulation, Inheritance, Polymorphism

'''
# OOP --> Abstraction, Usage of Class Methods & Static Methods

# Class Methods -->These are termed by using @classmethod decorator
# It applies for entire class level data, thereby every object utilisation will be modified...abs

# Let's work on an example related to E-Commerce

'''
class E_Commerce:
    """Usage of Class Method & Class Attribute"""
    company = "Flipkart"         # Class Attribute
    delivery_charge = 50         # Class Attribute
    @classmethod
    def update_delivery(cls):
        cls.delivery_charge = 100
        print(f"New Delivery Charge is {cls.delivery_charge}")

Product = E_Commerce()
# We can call Class Attributes with Object Name or as well as Class Name

print(Product.company)            # Calling class attribute using object.attribute
print(Product.delivery_charge)

print(E_Commerce.company)         # calling class attributes using class name
print(E_Commerce.delivery_charge)

Product.update_delivery()         # Accessing class method
print(Product.delivery_charge)

Mobile = E_Commerce()
print(Mobile.delivery_charge)

'''

# Applying Inheritance and usage of class method, class attributes

# Banking Scenario --> RBI --> SBI, HDFC, .....

'''
class RBI:
    """Inheritance Usage & Class method"""
    available_cash = 5000000         # class attribute
    @classmethod
    def rbi_cash(cls):
        print(f"Available Cash with RBI is {cls.available_cash}")
class SBI(RBI):
    pass
class HDFC(RBI):
    """Now we will also add some cash to it"""
    cash = 3000000
    @classmethod
    def HDFC_cash(cls):
        print(f"Available cash is {cls.cash}")
        print(f"Total Cash Available is {cls.cash + cls.available_cash}")
        print(f"Total Cash Available is {HDFC.cash + RBI.available_cash}")
'''
'''
a = SBI()
print(a.available_cash)
a.rbi_cash()
SBI.rbi_cash()       # We can also access with class name directly

b = HDFC()
print(b.available_cash)
print(b.cash)
b.rbi_cash()
b.HDFC_cash()

'''
'''
class RBI:
    """Inheritance Usage & Class method"""
    cash = 5000000         # class attribute
    @classmethod
    def rbi_cash(cls):
        #print(f"Available Cash with RBI is {cls.cash}")
        print(f"Available Cash with RBI is {RBI.cash}")
class SBI(RBI):
    pass
class HDFC(RBI):
    """Now we will also add some cash to it"""
    cash = 3000000
    @classmethod
    def HDFC_cash(cls):
        print(f"HDFC cash is {cls.cash}")
        
a = HDFC()
print(a.cash)
a.HDFC_cash()
a.rbi_cash()       

'''
# If incase as above scenario, we have same name for class attribute in both parent and child classes, 
# the best approach is to call the class attributes is using class names such as (RBI.cash)

# Static Method --> It doesn't depend neither on object or to the class
# we can create it using @staticmethood decorator
# It is mainly used as utility or helper functions

'''
class E_Commerce:
    """Usage of static method"""
    @staticmethod
    def free_delivery(price):
        return price > 500

u1 = E_Commerce()
print(u1.free_delivery(450))
print(u1.free_delivery(1000))

'''
# Now let's relate 

'''
class E_Commerce:
    """Usage of class & static methods"""
    platform = "Flipkart"        # class attribute
    @classmethod
    def show_platform(cls):
        print("Welcome to the platform")
        print(f"{cls.platform}")
    @staticmethod
    def free_delivery(price):
        #return price > 500
        if price > 500:
            print("You are Eligible for Free Delivery")
        else:
            print(f"Add products worth ${500 - price} to be eligible to free delivery")

user = E_Commerce()
print(user.platform)

user.show_platform()
user.free_delivery(450)
user.free_delivery(1200)

'''
# Abstraction : It is also one of the key feature of OOP, where it shows only relevant details to the user and hides the implementation

# Instagram --> Uploading Photo, Upload Video or Reel

# When we need all child classes to follow same pattern
# we have abc module to implement abstraction
'''

import abc
from abc import ABC,abstractmethod
class Content(ABC):
    @abstractmethod
    def upload(self):
        pass
class Photo(Content):
        def upload(self):
            print("Compressing the Picture")
            print("Edit the Picture")
            print("Photo Uploaded Successfully")
'''
'''
    pass       # As we made upload as Abstract method. It is mandatory to use upload method in every child class
class Video(Content):
    def upload(self):
        print("Encoding the Video")
        print("Video Editing is in Progress")
        print("Video Uploaded Successfully")
class Reel(Content):
    def upload(self):
        print("Adding Effects to the Reel")
        print("Reel is Edited")
        print("Reel uploaded Successfully with Tags...")
'''
'''
Contents = [Photo(),Video(),Reel()]
#print(Contents)
for content in Contents:
    content.upload()

obj = Photo()
print(obj)
a = Video()
print(a.upload())

'''









