from typing import Self
from data_structures.queue import Queue


class AnimalShelter:
    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()
        self.animals_in_shelter = Queue()

    def enqueue(self, animal):

        if animal.species == "cat":
            self.cat.enqueue(animal)
            self.animals_in_shelter.enqueue(animal)
        elif animal.species == "dog":
            self.dog.enqueue(animal)
            self.animals_in_shelter.enqueue(animal)
        else:
            return "Sorry, we only accept cats and dogs."

    def dequeue(self, pref=None):
        if pref == "cat" and not self.cat.is_empty():
            return self.cat.dequeue()
        elif pref == "dog" and not self.dog.is_empty():
            return self.dog.dequeue()
        elif pref == None:
            return self.animals_in_shelter.dequeue()
        return None

#super class Animal with sub classes Dog and Cat
# initializes with name and species so Dog and Cat classes can inherit
    #and don't have to init themselves

class Animal:
    def _init_(self, name="unknown"):
        self.name = name

class Dog(Animal):
    species = "dog"

class Cat(Animal):
    species = "cat"



