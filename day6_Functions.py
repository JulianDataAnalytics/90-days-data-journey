# Functions 
# a block of  reusable code
# place () after the function name to invoke it

# Crea una función llamada es_par que:
# Reciba un número
# Devuelva True si es par
# Devuelva False si es impar 

#def es_par(number):
 #   return number % 2 == 0

#print(es_par(7)) 


def major_list (list):
    if not list:
        return None
    
    major = list[0]
    for number in list:
        if number > major:
            major = number
    return major
 
print(major_list([2, 4, 5, 5, 6]))
