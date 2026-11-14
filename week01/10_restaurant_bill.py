#Shan_72387_PFAI_Week01
food_price = float(input("Enter food price: "))
tax_percent = float(input("Enter tax percentage: "))
discount_percent = float(input("Enter discount percentage: "))
service_charge = float(input("Enter service charge: "))

tax_amount = (food_price * tax_percent) / 100
amount_with_tax = food_price + tax_amount

discount_amount = (amount_with_tax * discount_percent) / 100
amount_after_discount = amount_with_tax - discount_amount

final_bill = amount_after_discount + service_charge

final_bill_rounded = round(final_bill, 2)
print("Final bill is:", final_bill_rounded)
#Shan_72387_PFAI_Week01