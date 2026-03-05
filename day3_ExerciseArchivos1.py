#Vamos a leer estudiantes desde un archivo y calcular el promedio.

#Supongamos que el archivo notas.txt tiene esto:

#Ana,4.5
#Luis,3.2
#Maria,4.9
#Carlos,2.8


archivo = open("notas.txt", "r")

estudiantes = []
suma = 0

for linea in archivo:
    nombre, nota = linea.strip().split(",")
    
    nota = float(nota)
    
    estudiantes.append({"nombre": nombre, "nota": nota})
    
    suma += nota

archivo.close()

promedio = suma / len(estudiantes)

print("Promedio:", promedio)
print(estudiantes)
