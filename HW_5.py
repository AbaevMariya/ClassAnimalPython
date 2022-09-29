class Animal:
    def __init__(self, classOfAnimal,detachment,families, genus, prospects):
        self.classOfAnimal = classOfAnimal
        self.detachment = detachment
        self.families = families
        self.genus = genus
        self.prospects = prospects

    def walk(self):
        return "I can walk"

class Mammal(Animal):
    def __init__(self,classOfAnimal,detachment,families, genus, prospects, sounds):
        super().__init__(classOfAnimal,detachment,families, genus, prospects)
        self.__sounds = sounds


    def get_sounds(self):
        return f"My sounds is {self.__sounds}"


    def set_sounds(self, newSounds):
        self.__sounds = newSounds


class Fish(Animal):
    def __init__(self,classOfAnimal,detachment,families, genus, prospects, skeletalStructure, habitat):
        super().__init__(classOfAnimal,detachment,families, genus, prospects)
        self.skeletalStructure = skeletalStructure
        self.habitat = habitat

    def walk(self):
        return "I can swim, because I have fins"



animal1 = Mammal('mammal','predatory','canine','dog','wolf','RR')
print(animal1.classOfAnimal)
print(animal1.detachment)
print(animal1.families)
print(animal1.genus)
print(animal1.prospects)
print(animal1.get_sounds())
animal1.set_sounds = "Auuuuuu"
print(animal1.__dict__)

fish1 = Fish('fish','cyprinids','ray-finned fish', 'carp family','cyprinus bartatus','bone','freshwater')
print(fish1.classOfAnimal)
print(fish1.prospects)
print(fish1.habitat)
print(fish1.skeletalStructure)
print(fish1.walk())
print(fish1.__dict__)





