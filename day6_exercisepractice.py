# exercise

def contar_pares (numbers):
    return len([n for n in numbers if n % 2 == 0])

   
print(contar_pares([2, 3, 4, 5, 6, 7, 8]))

# exercise filtrar y limite


def major_filter(lista, limite):
    return [numero for numero in lista if numero > limite]

print(major_filter([5, 10, 15, 20], 12))