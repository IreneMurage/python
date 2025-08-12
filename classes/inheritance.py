class Shapes:

    def __init__(self,name):
        self.name = name


    def describe(self):
        print(f"This shape is called", self.name)

shape1 = Shapes(name = "Circle")
shape1.describe()


class Rectangle (Shapes):

    def __init__(self,length,width):
        super().__init__(name = "Rectangle")
        self.length = length
        self.width = width
        
    def area(self):
        a = self.length * self.width
        print(f"The area is{a}")
        return a
        
r1 =Rectangle()
r1.describe()








class Dogs:

    def __init__(self, name,breed):
        self.name = name
        self.breed = breed
        if self.name == "Rene"
            self.age = 5
            self.lunch = "Hotdog"
            self.Dinner = "Broiler"
        else:
            self.age = 7
            self.lunch = "A full Chicken"
            self.Dinner = "Dog treats"
        