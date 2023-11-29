#Classmethod
class Person():
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
        
    @classmethod
    def years(cls,name, byears):
        age=2023-byears
        return cls(name,age)
    
    
p1=Person.years("Fatma",2009)
print("age : ",p1.age)

print()

#Static Method
class Math:
    @staticmethod
    def add_num(x,y):
        return(x+y)
    @staticmethod
    def pi():
        return(3.14)
   
print(Math.add_num(5,2))

class shape:
    def __init__(self,name,color,r):
        self.name=name
        self.color=color
        self.r=r
    def area(self):
        return 2*Math.pi()*self.r
sh1=shape("c1","red",5)
print(sh1.area())
print(Math.add_num(5,4))