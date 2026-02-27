# EXERCISE 2


numbers = [18, 7, 25, 30, 4, 11, 50, 3]

major = numbers[0]

   
for n in numbers:
    if n > major:
        major = n
print("the major numeber is: " , major)


# EXERCISE 2


numbers = [18, 7, 25, 30, 4, 11, 50, 3]

major = numbers[0]
second_major = numbers [0]
   
for n in numbers:
    if n > major:
        second_major = major
        major = n
    elif n > second_major and n != major:
        
            second_major = n
            
print("the major numeber is: " , major)
print("the second major numeber is: " , second_major)