"""
If the bill was $150.00, split between 5 people, with 12% tip.
Each person should pay (150.00 / 5) * 1.12 = 33.6
Format the result to 2 decimal places = 33.60
"""

print("Welcome to the trip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much % of tip would you like to give? 10, 12 or 15? "))
people_to_split = int(input("How many to split the bill? "))

total_bill_with_tip = total_bill * (tip / 100 + 1)
result = total_bill_with_tip / people_to_split

print(f"Each person should pay: ${round(result, 2)}")
#print(f"Each person should pay : ${'{:.2f}'.format(result)}")
