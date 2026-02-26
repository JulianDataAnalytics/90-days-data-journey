# SISTEMA DE INTENTOS

intentos = 0
password = "abcd"

while intentos < 3:
    user_password = input("enter your password:")
    if user_password == password:
        print(" Access granted")
        if intentos == 0 :
            print( "excelent memory")
                   
        elif intentos == 1:
            print("narrowly")
            
            
        break
    else:
            intentos += 1
            print("incorrect password")
            
if intentos == 3:
         print("acount blocked, you have {3 - intentos} attempts left")       
            
