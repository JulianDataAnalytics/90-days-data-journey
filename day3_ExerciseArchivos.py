# Ahora algo MUY usado: leer archivo línea por línea 📂

# Supongamos que el archivo notas.txt tiene esto:

#Ana  4.5
#Luis 3.2
#Maria 4.9
#Carlos 2.8

# Código

archivo = open("notas.txt", "r")

for linea in archivo:
    print(linea)

archivo.close()