# NOTE *args enables unlimited number of arguments in the form of a tuple
def add(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)

add(1, 2, 3)
add(1)
add(4, 5, 6, 7)
add(1, 2, 3, 4, 5, 6, 7, 8, 9)


# NOTE **kwargs enables unlimited number of keyword arguments in the form of a dictionary
def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make") # NOTE get function is the same as kw["make"], but if there isn't a value it doesn't crash it
        self.model = kw.get("model")
        self.color = kw.get("color")

my_car = Car(make="Nissan", model="GTR")
print(my_car.model)