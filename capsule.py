class PS5:
    def __init__(self):
        self.__price=30000

    def sell(self):
        print("Price of this PS5 is:",self.__price)

    def wprice(self,newprice):
        self.__price=newprice

pf=PS5()
pf.sell()

pf.__price=63500
pf.sell()

pf.wprice(42000)
pf.sell()