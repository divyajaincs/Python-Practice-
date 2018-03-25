string=input("enter string")
newstr=""
for i in range(len(string)):
    if(i%2==0)and(string[i]!=" "):
        newstr+=string[i]
print(newstr)
print(newstr[::-1])     