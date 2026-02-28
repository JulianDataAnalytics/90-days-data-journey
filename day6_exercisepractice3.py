#EXERCISE 3 
# Haz una nueva lista que contenga:

# Solo los números que son múltiplos de 5

# Pero elevados al cuadrado


numbers = [10, 15, 20, 25, 30]


new_list = [n * n for n in numbers if n % 5 == 0 ]

print("numbers is:", new_list)

def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(resultado)