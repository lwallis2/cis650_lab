smallest = None
while True: 
    next_input = int(input('Enter a number or -1 to stop: '))
    if next_input == -1:
        break
    else: 
        if smallest is None or smallest > next_input:
            smallest = next_input
print('Smallest is: ', smallest)