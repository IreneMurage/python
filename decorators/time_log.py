# how long function get executed
import time

def time_fn(fn):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        fn(*args,**kwargs)
        end_time=time.time()
        diff=end_time-start_time
        print("Time taken to run",diff)
    return wrapper

@time_fn
def counter():
    for n in range(0,10000000):
        print(n)

@time_fn
def counter2():
    for n in range(0,10000):
        print(n)

@time_fn
def sum(*args):
    ans=0
    for n in args:
        # print(f"{ans}={ans}+{n}")
        print(ans,"=",ans,"+",n)
        ans=ans+n
    
    print("Ans is ",ans)
    return ans

sum(1,2,3,1000,10002,5345,34535,12234234,654645,23423)



# Decorators.
## Extend or modify the behaviour of 
## functions or without changing their code
## CALLBACKS<-->



def my_deco(fn):
    def wrapper():
        print("Decorator before calling function")
        fn()
        print("Decorator after calling function")
    return wrapper

@my_deco
def hello():
    print("hello world")

@my_deco
def greet():
    print("Greetings from above")



#result the 
# greet()
# hello()
#hello()-> my_deco(hello) -> wrapper -> wrapper()
# my_deco(hello)()

