# Problem 2: Duck Typing

class Car:
    def move(self):
        print("The car is driving!")


class Person:
    def move(self):
        print("The person is walking!")


class Robot:
    def move(self):
        print("The robot is moving!")


# Duck typing function
def make_it_move(thing):
    thing.move()


# Create objects
car = Car()
person = Person()
robot = Robot()

# Put all objects in a list
objects = [car, person, robot]

# Use a for loop
for obj in objects:
    make_it_move(obj)