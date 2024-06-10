"""Class Inheritance"""


class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")


class Fish(Animal):

    def __init__(self):
        super().__init__()   #Inheriting from Animal class

    def breathe(self):
        super().breathe()    #inheriting breath() from Animal class
        print("Under water")
    def swim(self):
        print("moving in water")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
