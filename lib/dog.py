# lib/dog.py

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

    def sit(self):
        print("The dog is sitting.")

    def get_adopted(self, owner_name):
        self.owner = owner_name
