import math
def Main():
    try:
        num=float(input("please enter a no"))
        number=math.fabs(num)
        print(number)
        radius=float(input("enter radius:"))
        area=math.pi*radius**2
        print(area)
    except:
        print("you did not enter a no.")
if __name__=="__main__":
      Main()