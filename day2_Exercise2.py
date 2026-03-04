# EXERCISE 2
# ENCONTRAR LA NOTA MAS ALTA

estudiantes = [
    {"nombre": "Ana", "nota": 4.5, "estado": "Aprobado"},
    {"nombre": "Luis", "nota": 3.2, "estado": "Aprobado"},
    {"nombre": "Carlos", "nota": 2.8, "estado": "Reprobado"},
    {"nombre": "Maria", "nota": 4.9, "estado": "Aprobado"}
]

nota_mayor = estudiantes [0]["nota"]
for estudiante in estudiantes: 
 if estudiante["nota"] > nota_mayor:
     nota_mayor = estudiante["nota"]
     
     print("la nota mas alta es:", nota_mayor )
     
# hacemos el codigo para saber tambien el n ombre dle mejor estudiante     
mejor_estudiante = estudiantes[0]

for estudiante in estudiantes:
    if estudiante["nota"] > mejor_estudiante["nota"]:
        mejor_estudiante = estudiante

print("El mejor estudiante fue:", mejor_estudiante["nombre"])
print("Con nota:", mejor_estudiante["nota"])    