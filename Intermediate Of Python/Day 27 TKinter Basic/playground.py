# def add(*args):
#     return sum(args)
#
# print(add(23, 34, 56, 78))
#
# def calculate(n, **kwargs):
#     n += kwargs["sum"]
#     n *= kwargs["mul"]
#     print(n)
#     print(kwargs)
class Car:
    def __init__(self, **kw):
        self.color = kw.get("color")
        self.seats = kw.get("seats")
        self.model = kw.get("model")
        self.make = kw.get("make")
my_car = Car(color="Red", make="SUV", model="GWagon")
print(my_car.model)
