# EXERCISE 1

name = input("what is your name? ")  
age = int(input("what is your age? "))
city = input("what is your city? ")
VIP = input("are you a VIP? (Y/N) ")

if name == "":
    print("you didn't enter your name")
else:    
    print(f"Hello {name}")   
if city == "bogota":   
    print(f"welcome to the show")
else:
    print(f"Welcome from {city} is a honor for us!")
    
if age == 18:
    print("Access granted, you are an adult")
elif age > 60:
    print("Access granted, enter for the preferential area")  
    
else:
    print("Access denied, you are a minor")


if VIP == "Y":
    print("you have access to the VIP area")      
else:
    print("you don't have access to the VIP area and you can go to the normal area")    
    