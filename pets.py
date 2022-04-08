class Pet:

    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
    
    def play(self):
        self.health += 5
        print(f"I like to play.  My health is now {self.health}!")
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"Meal time is my favorite!! Energy + 5 : {self.energy} , Health + 10: {self.health}")
        return self

    def noise(self):
        print(f"Splish splash! Bathtime")
        return self

    def sleep(self):
        self.energy += 25
        print(f"Sleeping in my comfy bed has given me 25 {self.energy}")
        return self

