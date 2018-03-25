from abc import ABC,abstractmethod
class Emp(ABC):
    @abstractmethod
    def calculateSalary(self,sal):


        pass

class sub (Emp):

    def calculateSalary(self,sal):
         finalSal=sal*1.10
         return finalSal
emp1=sub()
print(emp1.calculateSalary(12000))



