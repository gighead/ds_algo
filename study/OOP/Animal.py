class Animal:

    def __init__(self, name=None, sound=None):
        self.name = name
        self.sound = sound

    def Animal_details(self):
        print(f"Name: {self.name}")
        print(f"Sound: {self.sound}")


class Dog(Animal):

    def __init__(self, name, sound, family):
        super().__init__(name, sound)
        self.family = family

    def Animal_details(self):
        super().Animal_details()
        print(f"Family: {self.family}")

class Sheep(Animal):

    def __init__(self, name, sound, color):
        super().__init__(name, sound)
        self.color = color

    def Animal_details(self):
        super().Animal_details()
        print(f"Color: {self.color}")

