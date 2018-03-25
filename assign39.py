class customer:
    def setcustomerid(self,id):
        self.__customerid=id
    def setcustomername(self,name):
        self.__customername=name    
    def settelephoneno(self,telno):
        self.__telephoneno=telno
    def getcustomerid(self):
        return self.__customerid
    def gettelephoneno(self):
        return self.__telephoneno
    def validatecustomername(self):
        if(len(self.__customername)>=3 and len(self.__customerid)<=20):
           return True
        else:
            return False
      
custobj=customer()
print("Customer  Id:",custobj.getcustomerid()) 
print("Telephone no:",custobj.gettelephoneno())  
print("Customer Name:",custobj.getcustomernamez)