Employee_id=1001
basic_salary=15000.00
allowances=6000.00
Monthly_gross_salary=basic_salary+allowances
if Monthly_gross_salary>10000:
    incometax=(Monthly_gross_salary*(20/100));
else:
    incometax=0.0
net_salary=Monthly_gross_salary-incometax
print("Employee Id:%d"%Employee_id)
print("basic salary:Rs.%f"%basic_salary)
print("allowance:Rs.%f"%allowances)
print("gross pay:Rs.%f"%Monthly_gross_salary)
print("income tax:Rs.%f"%incometax)
print("net_salary:Rs.%f"%net_salary)
    

