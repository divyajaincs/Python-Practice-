List1=['Sofa set','Dining table','T.V. stand','Cupboard']
List2=['20,000','8,500','4,599','13,920']
f=input("Which furniture is required:")
q=2
for i in range(len(List1)-1):
    if (List1[i]==f) and (q<=0):
                bill_amount=q*List2[i] 
    else:
            bill_amount=0
print("Bill Amount:Rs.%d"%bill_amount)        