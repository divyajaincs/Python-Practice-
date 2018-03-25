def fun():
     print("hello")
     print("hello")
def getInteger(p):
    result=int(input(p))
    return result
def Main():
    print("started")
fun()
r=getInteger("enter aa value")
print(r)
if __name__=="__main__":
    Main()