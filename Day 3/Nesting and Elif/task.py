print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("How old are you? \n"))

if height >= 120:
    if age >= 18:
        print("You can ride the rollercoaster. The price is $12.")
    elif age <= 12:
        print("You can ride the rollercoaster. The price is $5.")
    else:
        print("You can ride the rollercoaster. The price is $7.")
else:
    print("Sorry you have to grow taller before you can ride.")
