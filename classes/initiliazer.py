class Human:

    def __init__(self):
        print("Iam human")

    def another_human(self):
        print("Y.O.L.O")

# Irene = Human()
Irene = Human()
Irene.another_human()


_______________________________________________________________
class robot:

    def __init__(self,color,age,name):
        print(color, age, name)

robot1= robot(color= "red", age = 3, name = "Robo")
       
_______________________________________________________________
#class Name:First letter Cap<> 
class Student:
     name="Sam"
     email="sam@sam.com"
     phone="25472390423"

#student 1
student1=Student() #Object datatype: dot notation
student2=Student()

print("student 1")
print("name",student1.name)
print("email",student1.email)
print("phone",student1.phone)

print("student 2")
print("name",student2.name)
print("email",student2.email)
print("phone",student2.phone)


