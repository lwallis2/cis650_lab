number = input("Please insert an Integer: ")
if number.isdigit():
    number = int(number)
    multiple = 0
    while multiple <= 100:
        print(multiple)
        multiple += number
else:
    print("Input has to be a number")

