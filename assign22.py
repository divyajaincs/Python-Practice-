string1=input("Enter first string:")
string2=input("Enter second string:")
str1=""
str2=""
List2=[]

for i in string1:
    if i.isupper():
        str1+=i
for i in string2:
    if i.isupper():
        str2+=i
str1+=str2
print(str1)                