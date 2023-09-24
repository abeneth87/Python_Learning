#keyword arguments

def calculate(n, **kwargs):
    print(kwargs)
    #for key, value in kwargs.items():
    #   print(key)
    #   print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]
        self.color = kw.get("color")
        self.range = kw.get("range")

my_car = Car(make="Hyundai", model="Ioniq")
print(my_car.model[0:3])
print(my_car.range)