number_items = input("How many items do you want to enter: ")

sum_extended_prices = 0.0
if number_items.isdigit():
    number_items = int(number_items)
    for i in range(number_items):
        name = input("Enter item name: ")
        unit_price = float(input("Enter unit price: "))
        quantity = int(input("Enter quantity: "))

        extended_price = unit_price * quantity

        print(f"{name} : {unit_price} * {quantity} = {extended_price:.2f}")

        sum_extended_prices += extended_price

    print(f'All together cost {sum_extended_prices:.2f}')
else: 
    print("Input has to be a number!")    