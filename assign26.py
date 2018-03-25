List=[]
n=5
q=1
i=0
while i<n:
    if i==0:
        p=0
        List.append(p)
        i+=1
    else: 
        List.append(q)
        q1=p+q
        p=q
        q=q1
        i+=1
    
print(List)   
    