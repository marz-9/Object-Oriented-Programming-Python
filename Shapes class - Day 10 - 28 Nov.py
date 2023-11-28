class Shape:   
    def __init__(self,name,color,description):
        self.name=name
        self.color=color
        self.description=description
    def __str__(self):
        return("the color of the shape: {} and the name: {}. {}".format(self.name,self.color,self.description))
        
class Square(Shape):
    def __init__(self,name,color,description,leng):
        super().__init__(name,color,description)
        self.leng=leng    
    def SArea(self):
        sarea=self.leng*self.leng
        return sarea   
    def __str__(self):
        return("The name of the shape: {} and the color of it: {}. {} ".format(self.name,self.color,self.description))
    
class Circle(Shape):
    def __init__(self,name,color,description,rad):
        super().__init__(name,color,description)
        self.rad=rad
    def CArea(self):
        carea=(3.14*(self.rad**2))
        return carea
    def __str__(self):
        return("The name of the shape: {} and the color of it: {}. {}".format(self.name,self.color,self.description))
    
    

square=Square("Square","Blue","This shape has 4 sides.",5)
circle=Circle("Circle","Red","This shape has no sides or corners,it's in a round shapelike.",3)

print(square)
print(circle)
print("The area of the square is: ",square.SArea())
print("The area of the circle is: ",circle.CArea())

    
