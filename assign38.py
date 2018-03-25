class customer:
    def setcustomerid(self,id):
        self.customerid=id
    def settelephoneno(self,telno):
        self.telephoneno=telno
    def getcustomerid(self):
        return self.customerid
    def gettelephoneno(self):
        return self.telephoneno
custobj=customer()
custobj.setcustomerid(1001);
custobj.settelephoneno(9277786123) 
print("Customer  Id:",custobj.getcustomerid()) 
print("Telephone no:",custobj.gettelephoneno())  