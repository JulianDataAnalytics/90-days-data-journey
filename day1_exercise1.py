# EXERCISE 1
# 📝 Tu misión:

# 1️⃣ Recorrer la lista
# 2️⃣ Imprimir solo los estudiantes que tienen nota mayor o igual a 3.0
# 3️⃣ Mostrar algo así:


estudiantes = [
    {"nombre": "Ana", "nota": 4.5},
    {"nombre": "Luis", "nota": 3.2},
    {"nombre": "Carlos", "nota": 2.8},
    {"nombre": "Maria", "nota": 4.9}
]


suma = 0
for estudiante in estudiantes:
    if estudiante["nota"] >= 3.0:
        print(estudiante["nombre"], "aprobó con", estudiante["nota"])

for estudiante in estudiantes:
    suma += estudiante["nota"]

promedio = suma / len(estudiantes)

print(promedio)       


# list comprehnsion

promedio = sum(estudiante["nota"] for estudiante in estudiantes) / len(estudiantes)

print(promedio)