# EXERCISE 4


# CLASIFICATION OF NUMBERS
while True:
    try:
        number = int(input("enter a number:"))
        break 
    except ValueError:
        print("invalid input. Please enter a valid integer.")   

if number > 0:
    print("the number is positive")
elif number < 0:
    print("the number is negative")
else:
    print("the number is zero")

if number % 2 == 0:
    print("the number is even") 
else:
    print("the number is odd") 
      
        