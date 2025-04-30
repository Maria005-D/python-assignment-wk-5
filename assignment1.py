# Base class
class Superhero:
    def __init__(self, name, power, strength):
        self.name = name
        self.power = power
        self._strength = strength  # Protected attribute (encapsulation)

    def display_info(self):
        print(f"{self.name} has the power of {self.power}.")

    def get_strength(self):
        return self._strength

    def set_strength(self, new_strength):
        if new_strength > 0:
            self._strength = new_strength
        else:
            print("Strength must be positive!")

# Subclass with additional behavior
class FlyingSuperhero(Superhero):
    def fly(self):
        print(f"{self.name} is flying through the sky!")

# Test
hero = FlyingSuperhero("Skybolt", "Lightning", 85)
hero.display_info()
hero.fly()
print("Strength:", hero.get_strength())
