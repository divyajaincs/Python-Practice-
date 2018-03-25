List=[1,3,2,5,4,9]
print(List)
n=len(List)
for i in range(len(List)-1):
    for j in range(len(List)-1):
        if List[j]<List[j+1]:
            temp=List[j]
            List[j]=List[j+1]
            List[j+1]=temp
        else:
            continue    
        
        
print(List)        