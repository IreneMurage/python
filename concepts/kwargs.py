## key words arguments

def greet(name, nationality):
    print("Name is", name)
    print("Nationality from", nationality)

##kwargs solves the mixup
greet("John", "India")

greet(nationality="Kenyan", name="Hailey")


def employee(**kwargs):
    print(kwargs)
    print("Name is", kwargs["name"])
    print(kwargs.items())
    for key,value in kwargs.items():
        print("for key", key, "The value is",value)

employee(name = "Irene", age=23, country="Kenya") 
employee(name = "Monicah", age=25, country="USA", city="New York")
