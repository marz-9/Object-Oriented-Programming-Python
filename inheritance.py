#Inheritance classes
#Person class parent | Student class child
class Person:
    def __init__(self, name, age=22):
        self.name= name
        self.age= age
    def __str__(self):
        return "hello {} you are {} years old".format(self.name, self.age)
    def say_hi(self):
        print("hello {} from parent class".format(self.name, self.age))

class Student(Person):
    def __init__(self, name, age=22):
        super().__init__(name,age)
    def say_hi(self):
                                    #if not added in {} for the age attribute it won't be printed
        print("hello {} from student class".format(self.name, self.age))
