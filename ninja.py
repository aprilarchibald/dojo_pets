from pets import Pet

class Ninja:

    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self
        
timmy = Pet("Timmy", "dog", "shake", 100, 150)
thomas = Ninja("Tommy", "Thompson", timmy, "bacon", "purina")


thomas.walk()
thomas.feed()
thomas.bathe()