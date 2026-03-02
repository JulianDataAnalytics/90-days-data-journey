# EXERCISE


def contar_mayores(lista, limite):
    count = 0
    
    for numero in lista:
        if numero > limite:
           count += 1
         
    
    return count


print(contar_mayores([5, 10, 15, 20], 12))
# 2

lista = [1, 2, 3]
lista.extend("45")

print(lista)
# 3

lista = [1, 2, 3]
lista.append("45")

print(lista)

# 4

persona = {
    "nombre": "Andres",
    "edad": 25
}

print("edad" in persona)
print("altura" in persona)

# 5

persona = {
    "nombre": "Andres",
    "edad": 25
}

for clave in persona:
    print(clave)
    
    