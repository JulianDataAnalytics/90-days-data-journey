# EJERCICIOS DE PRACTICA

name = input(f" enter  your name: ")
edad = int(input(f" enter your age: "))  
ciudad = input(f" enter your city: ")   
altura = float(input(f" enter your height in meters:  "))
peso = float(input(f" enter your weight in kilograms:  "))
IMC = peso / (altura ** 2)


print(f" hello {name} ")
print(f" actualmente vives en {ciudad} ")
print(f" tu edad es {edad} años y en 5 años tendras {edad + 5} años ")
print(f" segun tu edad actual naciste en el año {2026 - edad} ")
print(f" tu IMC ES DE : {peso} / ({altura ** 2}) = {IMC}")


if IMC < 18.5:
    print("BAJO PESO")
if IMC >= 18.5 and IMC < 24.9:
    print("PESO NORMAL")
if IMC > 25: 
    print("SOBREPESO")



