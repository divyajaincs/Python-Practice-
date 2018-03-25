bill_id=1001
customer_id=101
bill_amount=200.0
print("bill_id:%d"%bill_id)
print("customer_id:%d"%customer_id)
print("bill_amount:Rs.%f"%bill_amount)
discounted_bill_amount=0.0;
if ((customer_id>100) and (customer_id<=1000)) is True:
    if bill_amount>=500:
        discounted_bill_amount=(bill_amount-bill_amount*(10/100))
        print("Discount bill_amount:Rs.%f"%discounted_bill_amount)
    else:
        print("No Discount")
else:
    print("Invalid Customer id,customer id must between 101 and 1000")