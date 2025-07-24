# YayaAhmed

def validate_input(func):
    def wrapper(rect, value):
        if value < 0:
            print("Value must be non-negative")
            return 
        return func(rect, value)
    return wrapper

rectangle_instances = []

def create_rectangle(length, width):
    rect = Rectangle(length, width)
    rectangle_instances.append(rect)
    return rect

def get_instance_count():
    return len(rectangle_instances)

@validate_input
def set_length(rect, value):
    rect.length = value

@validate_input
def set_width(rect, value):
    rect.width = value

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width

    @property
    def perimeter(self):
        return 2 * (self.length + self.width)


r1 = create_rectangle(10, 5)
print("Area:", r1.area)                 
print("Perimeter:", r1.perimeter)       
print("Count:", get_instance_count())   

set_length(r1, 7)                        
set_width(r1, -2)                        

print("Updated Area:", r1.area)          

print(" ------------------")
#-----------------------

import math


def validate_input(func):
    def wrapper(self, value):
        if value < 0:
            print("Value must be non-negative")
        return func(self, value)
    return wrapper

class Circle:
    instance_count = 0

    def __init__(self, radius):
        self.set_radius(radius)
        Circle.instance_count += 1

    @validate_input
    def set_radius(self, value):
        self._radius = value

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return math.pi * self._radius ** 2

    @property
    def circumference(self):
        return 2 * math.pi * self._radius

    @classmethod
    def get_instance_count(cls):
        return cls.instance_count
    
c1 = Circle(5)
print("Area:", round(c1.area, 2))             
print("Circumference:", round(c1.circumference, 2))  
print("Circles created:", Circle.get_instance_count())  

c2 = Circle(10)
print("Circles created:", Circle.get_instance_count())  


c1.set_radius(7)
print("Updated area:", round(c1.area, 2))     

