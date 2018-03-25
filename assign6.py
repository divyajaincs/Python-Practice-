from pip._vendor.distlib.compat import raw_input
obj_x=10
obj_y=obj_x
if (id(obj_x)==id(obj_y)):
    print("Address of obj_x and obj_y is same")
else:
    print("Address of obj_x and obj_y is not same")  
#code2
obj_x=10
obj_y=obj_x
if(obj_x is obj_y):
    print("obj_x and obj_y is same identity")
else:
    print("obj_x and obj_y is not same identity")   
    
#code3
obj_x=10
obj_y=obj_x
obj_y=obj_x+1
if (obj_x is not obj_y):
    print("obj_x and obj_y do not have same identity")
else:
    print("obj_x and obj_y have same identity")
             
#code4
int_a=10
raw_input=input("Enter a number")
print("Type of int_a:",type(int_a))
print("Type of raw_input:",type(raw_input))
print(int_a+raw_input)
             
          
    
    
