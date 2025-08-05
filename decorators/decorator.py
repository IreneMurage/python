# Decorators.
## Extend or modify the behaviour of 
## functions or without changing their code
## CALLBACKS<-->

#crown <--->
def my_deco(func):
    def wrapper():
        print("Calling hello world function")
        func()
        print("Finished calling hello world")
    
    return wrapper


@my_deco
def hello():
    print("hello world")

hello()



def mine_deco(logic):
     def wrapper ():
        print("wrapper call")
        for i in range (20,1,-3):
            print("i is",i)
            logic ()
            print ("your answer is",i)
     return wrapper

@mine_deco
def moon():
    for i in range (1,20,3):
        print ("your answer is",i)

moon()