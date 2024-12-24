# today i'am Absent and here's the codes
from abc import ABC,abstractmethod
class Bank:
    @abstractmethod
    def roi():
        pass
    def netBanking():
        pass

class SBI(Bank):
    def design(self):
        print("---SBI---")
    def roi(self):
        print("1% rate of interest")
    def netBanking(self):
        print("Yes we provide netbanking service")
class RBI(Bank):
    def design(self):
        print("---RBI---")
    def roi(self):
        print("2% rate of interest")
    def netBanking(self):
        print("nO we provide netbanking service")

s1=SBI()
r1=RBI()
s1.design()
s1.roi()
r1.design()
r1.roi()

class Bank:
    def _init_(self,name,ac,role,bala):
        self.name = name
        self.__ac = ac
        self._role = role
        self.balance = bala
    def _str_(self):
        return f"name = {self.name}\nA/C:{self.__ac}\nRole"
    def setpin(self,pin):
        self.__pin = pin
    def getpin(self,pin):
        return f'pin:{self.pin}'
b = Bank('Uday',2361,"Customer",1500.23)

print(b)
