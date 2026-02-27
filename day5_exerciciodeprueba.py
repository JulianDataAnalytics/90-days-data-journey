
# Exercise 2 interview

# Tu programa debe:

#  Mostrar solo los números mayores que 10
# Guardarlos en una nueva lista llamada greater_than_10
# Al final imprimir:

# La nueva lista

# Cuántos números se guardaron

# El número más grande de esa nueva lista

numbers = [18, 7, 25, 30, 4, 11, 50, 3]

greater_than_10 = []
count = 0


for n in numbers:
    if n > 10:
        print(n)
        greater_than_10.append(n)
        count +=1
print("Lista nueva:", greater_than_10)
print("Cantidad:", count)
print("Mayor:", max(greater_than_10))