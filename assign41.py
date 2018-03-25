class customer:
    def __init__(self,customer_id,telephoneno,customer_name):
        self.__customerid=customer_id
        self.__customername=customer_name
        self.__telephoneno=telephoneno
        self.__customername=None
        self.__telephoneno=[]
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
    def getcustomername(self):
        return self.__customername
    def validatecustomername(self):
        if(len(self.__customername)>=3 and len(self.__customername)<=20):
            return True
        else:
            return False
telephoneno=[9786443332,8945356745,9986452312]      
custobj=customer(1001,telephoneno,"Kevin")
check1=custobj.validatecustomername();
if(check1== True):
    print("Customer  Id:",custobj.getcustomerid())
    temp=custobj.gettelephoneno() 
    print("Telephone no:",temp[0],",",temp[1],",",temp[2])  
    print("Customer Name:",custobj.getcustomername())
   
else:
    print("Invalid customer name,Customer name should be between 3 and 20 characters")