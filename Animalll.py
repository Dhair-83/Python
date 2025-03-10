from abc import ABC,abstractmethod

class animal(ABC):
    def move(self):
        pass

class human(animal):
    def move(self):
        print("I walk!")

class panda(animal):
    def move(self):
        print("I roll!")

class bunny(animal):
    def move(self):
        print("I hop!")

h=human()
h.move()
p=panda()
p.move()
b=bunny()
b.move()