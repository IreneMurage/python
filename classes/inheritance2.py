class User:

    def __init__(self,name,email,phone,user,password,discount = 0):
        self.name = name
        self.email = email
        self.phone = phone
        self.user  = user
        self.password = password
        self.discount = discount
        self.is_locked = False

    def say_my_name(self):
        print(f"My name is {self.name}")

    def print_details(self):
        print("---------------------")
        print(self.name)
        print(self.email)
        print(self.phone)
        print(self.discount)
        print(self.password)
        print(self.user)
        print("---------------------")


    def login(self):
        if self.is_locked:
            print("Account is Locked")
            return  ##exit

        for i in range(0,3):
            password = input(f"Enter your password")
            if self.password == password:
                print("Logged in successfully")
                return
        
        self.is_locked = True
        print("Account locked. Contact Admin")


class Employee(User):
    def __init__(self, name, email, phone, password,salary):
        super.__init__(name = name,email = email,phone = phone,user = "employee",discount = 10,salary = salary)
        self.salary = salary

class Customer(User):
    def __init__(self, name, email, phone, user, password, discount = 0):
        super.__init__(name = name,email = email, phone = phone,user = user,password = password,discount = discount)

emp1 = Employee(name = "Irene",email = "irene@irene.com",phone = 1234567, user = "employee",Discount = 0,password = "1234",salary = 50000)
custom1 = Customer(name = "Wayne",email="Wayne@wayne.com",phone = 7654321,user = "customer",password = "password",discount = 10)

emp1.say_my_name()
custom1.say_my_name()

emp1.login()

c1.print_details()


