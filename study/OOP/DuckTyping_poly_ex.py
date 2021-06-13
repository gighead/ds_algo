class Dog:
    def Speak(self):
        print("Woof Woof")

class Cat:
    def Speak(self):
        print("Meow Meow")


class AnimalSound():
    def Sound(self, animal_obj):
        animal_obj.Speak()

class Humans():
    def Sound(self, human):
        human.Speak()

    def Speak(self):
        print("hahaha")

sound = AnimalSound()
dog = Dog()
cat = Cat()
human = Humans()

sound.Sound(dog) #Dynamic typing means we can change the type of an object later in the code.
sound.Sound(cat)
sound.Sound(human)

