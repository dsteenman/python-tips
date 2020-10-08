class Dog():
    def __init__(self, name) -> None:
        self.name = name

    def speak(self):
        return self.name + " says woof!"


class Cat():
    def __init__(self, name) -> None:
        self.name = name

    def speak(self):
        return self.name + " says meow!"


def pet_speak(pet):
    print(pet.speak())


niko = Dog("niko")
felix = Cat("felix")

# print(felix.speak())

# for pet in [niko, felix]:
#     print(pet.speak())

pet_speak(niko)
