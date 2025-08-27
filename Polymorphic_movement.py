from abc import ABC, abstractmethod

# Abstract base class
class Mover(ABC):
    @abstractmethod
    def move(self):
        pass

# Animal classes
class Dog(Mover):
    def move(self):
        return "Running 🐶"

class Bird(Mover):
    def move(self):
        return "Flying 🐦"

# Vehicle classes
class Car(Mover):
    def move(self):
        return "Driving 🚗"

class Plane(Mover):
    def move(self):
        return "Flying ✈️"

# Function to demonstrate polymorphism
def demonstrate_movement(movers):
    for mover in movers:
        print(f"{mover.__class__.__name__}: {mover.move()}")

# Main execution
if __name__ == "__main__":
    movers = [Dog(), Bird(), Car(), Plane()]
    demonstrate_movement(movers)