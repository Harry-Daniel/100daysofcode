print("Welcome to the tip calculator!")
total_bill=float(input("What was your total bill? $"))
percentage_tip=int(input("How much tip would you like to give? 10, 12, or 15?"))
people_paying=int(input("How many people to split the bill?"))

each_person_bill=round((total_bill+(total_bill*(percentage_tip/100)))/people_paying,2)

print(f"Each person should pay: ${each_person_bill}")
