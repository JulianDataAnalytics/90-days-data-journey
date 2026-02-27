# MINI SISTEMA DE LOGIN

password = "Abhjl123"

intentos = 0

while intentos < 3:
    user = input("enter your password: ")
    if user == password: 
         print("Access granted")
         break
    else:
         intentos += 1
         print( "Incorrect password")
if intentos == 3:
        print("account blocked")     

