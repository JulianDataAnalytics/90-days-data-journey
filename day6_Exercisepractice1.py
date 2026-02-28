# EXERCISE 1


numbers = [3, 18, 5, 42, 7, 12, 9]

major = []
minor_equals = []
count = 0
count_1 = 0
for n in numbers:
    if n > 10:
        print(n)
        major.append(n)
        count +=1  
        
major = [n for n in numbers if n > 10]        
        
for x in numbers:        
 if x <= 10:
    print(x)
    minor_equals.append(x)     
    count_1 +=1
    
               
print("major numbers is", major)
print("amount is:", count)
print("minor and equals numbers is", minor_equals)                
print("amount is:", count_1)


# EXERCISE WITH List Comprehensions
numbers = [3, 18, 5, 42, 7, 12, 9]
major = []
minor_equals = []


major = [n for n in numbers if n > 10 ]   
minor_equals = [n for n in numbers if n <= 10 ]   

print("the major numbers is:", major)
print(len(major))
print("minor equals numbers is:", minor_equals)
print(len(minor_equals))