# DICTIONARIES   A collections of {key : value} pairs orders and changeable, No duplicates.



capitals = {"USA": "WASHINGTON D.C.",
            "INDIA": "NEW DELHI",
            "COLOMBIA":"BOGOTA"}

# print(capitals["USA"])

# podemos agregar tambien una condicion en caso de escribir paises que no esten

if capitals.get("JAPAN"):
    print("that capital exist")
else: 
    print("that capital deosn't exist")
    
# capitals.update() agregar nuevos datos o modificarlos en el diccionario
# capitals.pop () eliminar un dato dentro del diccionario
# capitals.popitem() elimina el ultimo valor del diccionario sin escribirlo
# capitals.clear()  elimina todo dentro del diccionario
# key = capitals.key() lo usamos para traer solo las llaves dentro del diccionario
# for key in capitals.key () podemos usar un loop for para datos que se pueden iterar y tener una lista de las llaves del diccionario

# print(key)    

# values = capitals.values() lo mismo que lo anterior pero con los datos de valor dentro del diccioario
