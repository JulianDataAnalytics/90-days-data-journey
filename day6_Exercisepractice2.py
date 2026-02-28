# Exercise list comprehension
# Haz una nueva lista que:
# Si el número es mayor que 10 → guarda el número multiplicado por 2
# Si el número es menor o igual a 10 → guarda el número tal cual


numbers = [3, 18, 5, 42, 7, 12, 9]


New_list = [ n * 2 if n > 10  else n for n in numbers ]

print("the new list is:", New_list)



