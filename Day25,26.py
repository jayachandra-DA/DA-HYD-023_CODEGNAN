#Polymorphism
'''
it is one of the key feature of OOP
poly---> many
Morphism--> Forms
Method with same names can take different parameters (arguments)
--->Method overloading (complie time polymorphism)
--->method over riding (Runtime)
--->Operator Overloading(+,*)(__Add__,__init__)

Hotstar
Free User----->can watch the movies but with adds
Primium User---->movies can watch without any adds
VIP User---->more no of logins and streaming with high quality
'''
#Method overloading
'''
class Hotstar:
    """Understand Polymorphism"""
    def Watch():
        print("User logged into Hotstar.....Opening Home page")
    def Watch(self,movie):
        self.movie=movie
        print("Movie name is:",self.movie)
u1=Hotstar()
u1.Watch("Khaleja")
'''
#1)default arguments
'''
class Hotstar:
    """Method Usage with default arguments"""
    def Watch(self,movie=None):
        if movie is None:
            print("User logged into hotstar")
        else:
            self.movie=movie
            print("movie name is:",self.movie)
u1=Hotstar()
u1.Watch()
u1.Watch("Vikram")
'''
'''
class Hotstar:
    """Method Usage with default arguments"""
    def Watch(self,*movie):
        if len(movie) == 0:
            print("User logged into hotstar")
        else:
            self.movie=movie
            for i in movie:
                print("Movie is",i)
u1=Hotstar()
u1.Watch()
u1.Watch("Vikram","Leo","Pushpa")
'''
'''
class Hotstar:
    """Method overloading with type of arguments usage"""
    def watch(self,content):
        if isinstance(content,str):
            print("Movie name is:",content)
        elif isinstance(content,list):
            for i in content:
                print(i)
u1=Hotstar()
u1.watch('Naruto')
u1.watch(['Naruto','Demon Slayer'])
u2=Hotstar()
u2.watch(['M','N'])
'''

class User:
    """Understanding overriding"""
    def Watch(self,name,place):
        self.name=name
        self.place=place
        print("User logged into Hotstar.....Opening Home page")
class VIP(User): 
    def Watch(self,movie):
        self.movie=movie
        print("Movie name is:",self.movie)
u1=VIP()
u1.Watch("naruto")