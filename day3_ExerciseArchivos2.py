#Encontrar automáticamente:

#el mejor estudiante

#el peor estudiante

#cuántos aprobaron y reprobaron

#todo leyendo desde un archivo

#Imaginemos que el archivo notas.txt tiene esto:

#Ana,4.5
#Luis,3.2
#Maria,4.9
#Carlos,2.8
#Pedro,3.5

archivo = open("notas.txt", "r")

estudiantes = []

for linea in archivo:
    nombre, nota = linea.strip().split(",")
    
    estudiantes.append({
        "nombre": nombre,
        "nota": float(nota)
    })

archivo.close()

print(estudiantes)

suma = 0

for estudiante in estudiantes:
    suma += estudiante["nota"]

promedio = suma / len(estudiantes)

print("Promedio:", promedio)

aprobados = 0
reprobados = 0

for estudiante in estudiantes:
    if estudiante["nota"] >= 3:
        aprobados += 1
    else:
        reprobados += 1

print("Aprobados:", aprobados)
print("Reprobados:", reprobados)

mejor = estudiantes[0]

for estudiante in estudiantes:
    if estudiante["nota"] > mejor["nota"]:
        mejor = estudiante

print("Mejor estudiante:", mejor["nombre"], mejor["nota"])