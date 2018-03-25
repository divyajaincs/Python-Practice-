bill_id=1001
customer_id=101
bill_amount=200
print("bill_id:%d"%bill_id)
print("customer_id:%d"%customer_id)
print("bill_amount:Rs.%f"%bill_amount)
discounted_bill_amount=0.0;
if bill_amount>500:
    discounted_bill_amount=(bill_amount-bill_amount*(2/100))
else:
    discounted_bill_amount=(bill_amount-bill_amount*(1/100))  

print("Discount bill_amount:Rs.%f"%discounted_bill_amount)