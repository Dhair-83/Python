class wolf:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print("Hi! I am a wolf!")
        print(f"My name is {self.name} and I am {self.age} years old.")
    def sound(self):
        print("I howl.")

class panda:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print("Hi! I am a panda!")
        print(f"My name is {self.name} and I am {self.age} years old.")
    def sound(self):
        print("I growl.")

wf=wolf("Woverine",3)
pd=panda("Lonny",6)

for pets in(wf,pd):
    pets.info()
    pets.sound()