class Parrot:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    species="bird"

wik=Parrot("Wink", 3)
oly=Parrot("Olympus",5)

print("Wink is {}.".format(wik.species))
print("Olympus is {}.".format(oly.species))
print("{} is {} years old.".format(wik.name,wik.age))
print("{} is {} years old.".format(oly.name,oly.age))