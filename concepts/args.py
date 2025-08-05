# arguments

def greet(*args):
    print(*args)
    for arg in args:
        print("Name is ", arg)

greet("Irene", "Monicah", "John", "Doe")


def sum(*args):
    ans=0
    for n in args:
        print(f"{ans}={ans} + {n}")
        ans= ans + n

    print("Sum is", ans)
    return ans

sum(100,200,300,500,23)



