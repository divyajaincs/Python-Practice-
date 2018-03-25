class customer:
    def setcustomerid(self,id):
        customerid=id
    def settelephoneno(self,telno):
        telephoneno=telno
    def getcustomerid(self):
        return customerid
    def gettelephoneno(self):
        return telephoneno
custobj=customer()
custobj.setcustomerid(1001);
custobj.settelephoneno(9277786123) 
print("Customer  Id:",custobj.getcustomerid()) 
print("Telephone no:",custobj.gettelephoneno())  