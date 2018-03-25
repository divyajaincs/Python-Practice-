string=input("Enter a string")
a=set()
c=0
count=[]
for i in string.upper():
    a.add(i)
print(a) 
for i in a:
    for j in string.upper():
        if(i==j):
         c+=1
    count.append(c)    
    print(c,end='')
    print(i)
    c=0