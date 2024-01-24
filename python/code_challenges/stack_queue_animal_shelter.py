from data_structures.queue import Queue


class AnimalShelter:
    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()

    def enqueue(self, animal):

        if animal.species == "cat":
            self.cat.enqueue(animal)
        elif animal.species == "dog":
            self.dog.enqueue(animal)
        else:
            return "Sorry, we only accept cats and dogs."

    def dequeue(self, pref):
        try:
            if pref == "cat" and not self.cat.is_empty():
                return self.dequeue()
            elif pref == "dog" and not self.dog.is_empty():
                return self.dog.dequeue()
            else:
                return None
        except: InvalidOperationError("Method not allowed on empty collection")
        return None

class Dog:
    def __init__(self, name):
        self.name = name
        self.species = "dog"

class Cat:
    def __init__(self, name):
        self.name = name
        self.species = "cat"



