## this  is when we have area  method in the superclass, and we also have area method in the rec class.
## so now,one when one calls area for the rec, the method area in the area class will be called
## if we have a triangleclass and it does not have an area method,when area is called,it will call
## the area method the superclass(Shape) and npt that of the rec class.
class Shapes:

    def __init__(self,name):
        self.name = name


    def describe(self):
        print(f"This shape is called", self.name)

    def area(self):
        print(f"For shape {self.name}, area is not defined")
        return None

shape1 = Shapes(name = "Circle")
shape1.describe()


class Rectangle(Shapes):

    def __init__(self,length,width):
        super().__init__(name = "Rectangle")
        self.length = length
        self.width = width
        
    def area(self):
        a = self.length * self.width
        print(f"For {self.name} area is{a}")
        return a

class Triangle(Shapes):
    def __init__(self,length,height):
        super().__init__("Triangle")
        self.length = length
        self.height = height
        
r1 =Rectangle(4,5)
r1.describe()
r1.area()

t1 = Triangle(length = 5, height = 10)
t1.area()

