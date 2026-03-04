# 1 Contar cuántos aprobaron y cuántos reprobaron
# 2 Encontrar la nota más alta
# 3 Encontrar automáticamente el mejor estudiante

estudiantes = [
    {"nombre": "Ana", "nota": 4.5, "estado": "Aprobado"},
    {"nombre": "Luis", "nota": 3.2, "estado": "Aprobado"},
    {"nombre": "Carlos", "nota": 2.8, "estado": "Reprobado"},
    {"nombre": "Maria", "nota": 4.9, "estado": "Aprobado"}
]

aprobados = 0
reprobados = 0

for estudiante in estudiantes:
    if estudiante ["estado"] == "Aprobado":
        aprobados +=1
    else:
        reprobados +=1

print("Aprobados:", aprobados)
print("Reprobados:", reprobados)        