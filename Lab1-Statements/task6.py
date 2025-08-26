smallest = None
for i in range(5):
    next_input = int(input("Enter a positive number: "))
    if smallest is None or next_input < smallest: 
        smallest = next_input 
print ("The smallest numer is: ", smallest)