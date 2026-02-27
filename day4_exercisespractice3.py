# EXERCISE 3

try:
    ingresos = float(input("enter monthly income: "))
    puntaje = int(input("enter credit score (0 - 850): "))
except ValueError:
 print("invalid numeric input")

if puntaje < 0 or puntaje > 850:
   print("credit score out of valid range.")

while True:
    try:
       puntaje = int(input("enter credit score (0 - 850)"))
       if 0 <= puntaje >= 850:
           break
       else:
           print("credit score must be between 0 and 850")
    except ValueError:
        print("Invalid numeric input.")

while True:
    try:
        income = float(input(" enter your income: "))        
        if income >= 0:
            break
        else:
            print("income cannot be negative")
    except ValueError:
        print("Invalid numeric input")   

while True:
    debts = input("Do tou have debts ? (Y/N)").lower()                    
    if debts == "Y" or debts == "N"
       break
    else: 
        print("Please enter only  Y or N.")
if income < 1000  or puntaje < 500:
    print("credit reject")
elif (1000 <= income <= 2000) or (500 <= puntaje <= 650) or debts == "y":
    print("Credit Under Review")                 
else: 
     print("Credit approved")
                