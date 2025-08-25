number1 = int(input("enter your first number: "))
number2 = int(input("Enter your second number: "))

if number1 == number2:
    result = "Numbers are equal"
elif number1 > number2:
    result =  str(number1) + " is bigger than " + str(number2)
else:
    result = str(number2) + " is bigger than " + str(number1)
print(result)