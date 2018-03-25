#code1
counter=1
while counter<=3:
    print(counter)
    counter+=1
print("End of Program")    
    
 #code2
print("To find the sum of first 10 integers:")
result=0
for value in range(1,11):
     result=result+value
print("Sum:%d"%result)  
#code3
number=1
result=0
while number<5:
    result+=number
    number+=1
print(result)
#code4
result=0
for index in range(40,10,-2):
    if(index%5==0):
        result+=index
        print(result)
#code5
amount=100.0
interest=0.0
months=1
while months<6:
    interest=amount*0.2 
    amount+=interest
    months+=1
print(amount)    
           