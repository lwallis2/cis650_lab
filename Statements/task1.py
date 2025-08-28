name = input("Enter your name: ")
age = input("Enter your age: ")
my_name = "Luc"

if name == "":
    print("Name cannot be blank!")
elif not age.isdigit():
    print("Age has to be a number")
else: 
    age = int(age)
    if name == my_name:
        if age <= 0:
            print("You are not born yet.")
        elif age < 18:
            print('You are a minor')
        elif age <= 99:
            print("Adult")
        elif age > 99:
            print("Nice to meet you ")
    else: 
        print (f'{name} is not my Name ({my_name})')
