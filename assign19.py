#code1
string1=input("Enter a string")
count=0
for i in string1:
    if (i.isupper()):
        count+=1
print("No. of capital letters:%d"%count)        
#code2
def reverse(s):
    return s[::-1]

def isPalindrome(s):
    rev=reverse(s)
    if(rev==s):
     return True
    else:
     return False    
        
ans=isPalindrome(string1)
print(ans) 
#code3
count=0
List=['a','A','E','e','I','i','O','o','U','u']
for i in string1:
    if(i in List ) :
        count+=1
print("No. of Vowels:%d"%count)              
#code4
string=input("enter string with punctuation")
punctuation='''!()-[]{}:;'"\,<>./?@#$%^&*_~'''
for i in string:
    if(i in punctuation):
        string=string.replace(i,"")
print(string)              