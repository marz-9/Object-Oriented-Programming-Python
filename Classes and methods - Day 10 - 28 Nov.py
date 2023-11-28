#Creating class
class Person:
#Global Attribute
    num_object =0
#Defining attributes in a method called initializing
#self means taking infromation from the same class
                            #defualt value to avoid error if not mentioned in the object
    def __init__(self, name, age=22):
        #instant attribute
        self.name= name
        self.age= age
        #counts number of calls of method for objects
        Person.num_object+=1
#Defining string method, reads self attributes from the init method
    def __str__(self):
        return "hello {} you are {} years old".format(self.name, self.age)
    def say_hi(self):
        print("hello {} from parent class".format(self.name, self.age))

#creating object to a class
person1= Person("Fatma",24)
person2= Person("Sara")
#address of the object where it's saved | without str method it'll return it
#with str method it'll return the string so no need to type person1.age
print(person1)
#for person 1 because in the object is defined it'll not take the defualt value for it
print(person2)

#address of object printed
print(id(person1))

#printing values by calling it from class
print(person1.name, person1.age)

#printing th type of the object's class
print(type(person1))

#printing number of calls
print(Person.num_object)

#Encapsulation | private attributes
class Person3:
    num_object1 =0
    def __init__(self, name1, age1=28):
        #To make attributes private double undescores have o be written
        self.__name1= name1
        self.__age1= age1
        Person3.num_object1 +=1
    def set_name(self,new_name):
        self.__name1=new_name
    def get_name(self):
        print("hello {} you are {} years old".format(self.__name1, self.__age1))
    def __str__(self):
        return "hello {} you are {} years old".format(self.__name1, self.__age1)
    #defining setters and getters
    
    
    
person3= Person3("Fahad",24)
person4= Person3("Mohammad")
person3.set_name("Reem")
person4.get_name()
print(person3)

    
