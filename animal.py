class Animal:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.health = 100
    def walk(self):
        self.health-=1
        return self
    def run(self):
        self.health-=5
        return self
    def display_health(self):
        print("Health:", self.health)
        return self
class Dog(Animal):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.health = 150
    def pet(self):
        self.health+=5
        return self
class Dragon(Animal):
    def __init__(self, name, health):
        super().__init__(name, health)
    def fly(self):
        self.health-=10
        return self
    def display_health(self):
        super().display_health()
        print("I am a Dragon")
        
        return self
Kitty = Animal("Kitty", 100).walk().walk().walk().run().run().display_health()
Doggo = Dog("Doggo", 150).walk().walk().walk().run().run().pet().display_health()
Draggo = Dragon("Draggo", 170).walk().walk().walk().run().run().fly().display_health()
Platypus = Animal("Perry", 200).walk().walk().walk().run().run().display_health()