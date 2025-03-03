class Parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
   
    def singing(self,song):
        return "{} sings {}.".format(self.name,song)

    def dancing(self):
        return "{} is dancing.".format(self.name)

pol=Parrot("Lunar",15)

print(pol.singing("Jinglebells"))
print(pol.dancing())