bill_id=1001
customer_id=101
bill_amount=1200.0
print("bill_id:%d"%bill_id)
print("customer_id:%d"%customer_id)
print("bill_amount:Rs.%f"%bill_amount)
discounted_bill_amount=0.0;
discount=0
if bill_amount>=1000:
    discount=5
elif bill_amount>=500:
    discount=2   
else:
    discount=1
    
discounted_bill_amount=(bill_amount-bill_amount*(discount/100))  

print("Discount bill_amount:Rs.%f"%discounted_bill_amount)
