# Base class: Superhero
class Superhero:
    def __init__(self, name, power_level, secret_identity):
        self._name = name  # Protected attribute
        self.__power_level = power_level  # Private attribute (encapsulation)
        self.__secret_identity = secret_identity  # Private attribute (encapsulation)

    # Getter for power_level (encapsulation)
    def get_power_level(self):
        return self.__power_level

    # Setter for power_level with validation (encapsulation)
    def set_power_level(self, power_level):
        if power_level >= 0:
            self.__power_level = power_level
        else:
            raise ValueError("Power level cannot be negative")

    # Method to use power
    def use_power(self):
        return f"{self._name} uses their power at level {self.__power_level}!"

    # Method to reveal secret identity (encapsulation)
    def reveal_identity(self):
        return f"{self._name}'s secret identity is {self.__secret_identity}"

    # Method for polymorphism (to be overridden by child classes)
    def special_ability(self):
        return f"{self._name} has no special ability defined."

# Derived class: FlyingSuperhero (inherits from Superhero)
class FlyingSuperhero(Superhero):
    def __init__(self, name, power_level, secret_identity, flight_speed):
        super().__init__(name, power_level, secret_identity)  # Call parent constructor
        self.flight_speed = flight_speed  # Additional attribute for FlyingSuperhero

    # Override special_ability to demonstrate polymorphism
    def special_ability(self):
        return f"{self._name} soars through the sky at {self.flight_speed} km/h!"

    # Additional method specific to FlyingSuperhero
    def fly(self):
        return f"{self._name} is flying at {self.flight_speed} km/h!"

# Example usage
if __name__ == "__main__":
    try:
        # Create a Superhero instance
        hero = Superhero("Captain Courage", 80, "Alex Smith")
        print(hero.use_power())  # Output: Captain Courage uses their power at level 80!
        print(hero.reveal_identity())  # Output: Captain Courage's secret identity is Alex Smith
        print(hero.special_ability())  # Output: Captain Courage has no special ability defined.
        
        # Create a FlyingSuperhero instance
        flying_hero = FlyingSuperhero("Sky Blazer", 95, "Jane Doe", 300)
        print(flying_hero.use_power())  # Output: Sky Blazer uses their power at level 95!
        print(flying_hero.special_ability())  # Output: Sky Blazer soars through the sky at 300 km/h!
        print(flying_hero.fly())  # Output: Sky Blazer is flying at 300 km/h!
        
        # Demonstrate encapsulation
        print(flying_hero.get_power_level())  # Output: 95
        flying_hero.set_power_level(100)  # Update power level
        print(flying_hero.get_power_level())  # Output: 100
        # flying_hero.__power_level  # Error: AttributeError (direct access restricted)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")