def add(*args):
    print(args[2])
    sum=0
    for arg in args:
        sum+=arg
    return sum


print(add(5,5,10,15,-8))


def calculate(n,**kwargs):
    print(kwargs)
    print(kwargs['add'])
    n+=kwargs['add']
    n*=kwargs['multiply']
    print(n)

calculate(2,add=3,multiply=5)

class Car:

    def __init__(self,**kw):
        self.make=kw.get("make")
        self.model=kw.get("model")


my_car=Car(make="Nissan", )

print(my_car.model)