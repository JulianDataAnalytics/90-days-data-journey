# Objetivo

# Calcular el promedio general.

# Agregar a cada estudiante una nueva clave:

# "estado": "Aprobado" si nota >= 3.0

# "estado": "Reprobado" si nota < 3.0

# Guardar el promedio en un diccionario final.

estudiantes = [
    {"nombre": "Ana", "nota": 4.5},
    {"nombre": "Luis", "nota": 3.2},
    {"nombre": "Carlos", "nota": 2.8},
    {"nombre": "Maria", "nota": 4.9}
]

suma = 0

for estudiante in estudiantes:
    suma += estudiante["nota"]
promedio = suma / len(estudiantes)

print(promedio) 

for estudiante in estudiantes:
    if estudiante["nota"] >= 3.0:
        print(f"El estudiante {estudiante['nombre']} aprobo")
    else:
        print(f"El estudiante {estudiante['nombre']} reprobo")

for estudiante in estudiantes:
    if estudiante["nota"] >= 3.0:
        estudiante["estado"] = "Aprobado"
    else:
        estudiante["estado"] = "Reprobado"
print(estudiantes)           

resultado_final = {"promedio": promedio,
                   "cantidad_estudiantes": len(estudiantes)
                   }

print(resultado_final.get("promedio"))
print(resultado_final.get("cantidad_estudiantes"))
print(resultado_final)
