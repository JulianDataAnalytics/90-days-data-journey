# EXERCISE 1

numbers = [5, 12, 7, 20, 3, 15]
total = 0
count = 0
count_odd = 0

for number in numbers:
   if number > 10:
      print(number)    
      count += 1
print("total major to 10:" , count)

for number in numbers:
   if number % 2 == 0:
        
        count += 1         
    else:
        if number % 2 != 0:
           
           count_odd += 1
print("the numbers is even:", count)    
print("the numbers are odd:", count_odd)  

numbers = [5, 12, 7, 20, 3, 15]
total = 0
count = 0
count_odd = 0

for number in numbers:
   if number > 10:
      print(number)    
      count += 1
print("total major to 10:" , count)

for number in numbers:
   if number % 2 == 0:
        
        count += 1         
print("the numbers is even:", count)



# Haz una list comprehension que cree una nueva lista solo con los números pares.
numbers = [18, 7, 25, 30, 4, 11, 50, 3]

greater_than_10 = [n for n in numbers if n % 2 == 0 ] 

print(greater_than_10)