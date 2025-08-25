miles_driven = input("Enter of miles driven: ")
gallons_used = input("Enter numver of gallons used: ")
if miles_driven.isdigit() and gallons_used.isdigit():
    miles_driven = int(miles_driven)
    gallons_used = float(gallons_used)
    print("Miles per gallon: ", miles_driven/gallons_used)
else: 
    print("Invalid Input! Please enter only numbers")