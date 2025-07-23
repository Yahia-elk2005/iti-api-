# يحيي احمد
class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def start_engine(self):
        return "Engine started"

    def describe(self):
        return f"{self.name} moves at {self.speed} km/h"

class Car(Vehicle):
    def __init__(self, name, speed, brand):
        super().__init__(name, speed)
        self.brand = brand

    def describe(self):
        base_description = super().describe()
        return f"{base_description} (Brand: {self.brand})"

class ElectricCar(Car):
    def __init__(self, name, speed, brand, battery_range):
        super().__init__(name, speed, brand)
        self.battery_range = battery_range

    def start_engine(self):
        return "Electric motor activated!"


class Bicycle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def start_engine(self):
        return "No engine to start—just pedal!"

    def describe(self):
        return f"{self.name} rolls at {self.speed} km/h on two wheels"

def start_and_describe(vehicle_like):
    print(vehicle_like.start_engine())
    print(vehicle_like.describe())


v = Vehicle("Generic Vehicle", 80)
c = Car("Sedan", 120, "Toyota")
e = ElectricCar("Model E", 150, "Tesla", 300)
b = Bicycle("Roadster", 30)


for obj in [v, c, e, b]:
    start_and_describe(obj)
    print("---")
    