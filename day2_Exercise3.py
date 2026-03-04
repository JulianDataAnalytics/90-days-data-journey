# GUARDAR ESTUDIANTES EN UNA LISTA 


estudiantes = [
    {"nombre": "Ana", "nota": 4.5, "estado": "Aprobado"},
    {"nombre": "Luis", "nota": 3.2, "estado": "Aprobado"},
    {"nombre": "Carlos", "nota": 2.8, "estado": "Reprobado"},
    {"nombre": "Maria", "nota": 4.9, "estado": "Aprobado"}
]

nota_mayor = estudiantes[0]["nota"]


for estudiante in estudiantes:
    if estudiante["nota"] > nota_mayor:
        nota_mayor = estudiante["nota"]
        
mejores_estudiantes = []

for estudiante in estudiantes:
    if estudiante["nota"] == nota_mayor:
        mejores_estudiantes.append(estudiante)

print(mejores_estudiantes)

print("Nota más alta:", nota_mayor)
print("Mejores estudiantes:", mejores_estudiantes)


# mas optimizado el recorrido seria

nota_mayor = estudiantes[0]["nota"]
mejores_estudiantes = [estudiantes[0]]

for estudiante in estudiantes[1:]:
    if estudiante["nota"] > nota_mayor:
        nota_mayor = estudiante["nota"]
        mejores_estudiantes = [estudiante]
    elif estudiante["nota"] == nota_mayor:
        mejores_estudiantes.append(estudiante)

print("Nota mayor:", nota_mayor)
print("Mejores estudiantes:", mejores_estudiantes)