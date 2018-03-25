customer_details={1001:"John",1004:"Jill",1005:"Joe",1003:"Jack"}
print(customer_details)
print(len(customer_details))
print(sorted(customer_details.values()))
del(customer_details[1005])
print(customer_details)
customer_details[1003]="Mary"
print(customer_details)
print(1002 in customer_details)