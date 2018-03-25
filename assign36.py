class customer:
    def setcustomerid(self,id):
        self.__customerid=id
    def settelephoneno(self,telno):
        self.__telephoneno=telno
    def getcustomerid(self):
        return self.__customerid
    def gettelephoneno(self):
        return self.__telephoneno
custobj=customer()
custobj.setcustomerid(1001);
custobj.settelephoneno(9277786123) 
print("Customer  Id:",custobj.getcustomerid()) 
print("Telephone no:",custobj.gettelephoneno())  