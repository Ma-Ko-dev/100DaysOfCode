print("Welcome to the generous tip calculator!")
# getting the input, converting and saving it in variables
total_bill = float(input("Please tell me what the total bill is: "))
tip_percentage = int(input("And how generous do you feel today? 12, 14 or even 17 percent? "))
total_people = int(input("How many people to split the bill? "))

# calculate the total bill for each person
result = "{:.2f}".format(round((total_bill / total_people) * (1 + (tip_percentage / 100)), 2))

print(f"Each person should pay: ${result}! And dont forget to round up! BE GENEROUS!")
