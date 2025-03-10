class Employer():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(self.name)
        print(self.age)

class Employee(Employer):
    def __init__(self,id,address,name,age):
        self.id=id
        self.address=address

        super().__init__(name,age)

e=Employee(362,'Bangalore','Dhairya',15)
e.display()