# CTI-110 
# P2HW2 - Tip Tax Total 
# Pulver, Gill
# 4/22/18
#Calculate total cost of a meal with tip

foodCost= float(input("Input cost of food  $"))
tax = .07
food_and_tax = foodCost * tax
food_and_tax_total= food_and_tax + foodCost



tip = .18
tip_to_pay= food_and_tax_total * tip
print (tip_to_pay)

total_bill= tip_to_pay + food_and_tax_total
print ("$",total_bill)
