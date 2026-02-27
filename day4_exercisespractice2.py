# EXERCISE 3

total = 0  
count = 0
major_note = None
minor_note = None
approved = 0
failed = 0

while True:
    entrada = input("enter grade ( or 'fin' to exit): ")
    if entrada.lower() == "fin":
        break
    try:
        grade = float(entrada)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
    if grade < 0 or grade > 5:
        print("grade out of range")
        continue
    total += grade
    count += 1
    if grade >= 3:
        approved +=1
    else: 
        failed +=1
    if major_note is None  or grade > major_note:
        major_note = grade 
    if minor_note is None or grade < minor_note:
        minor_note = grade
if count > 0:
 promedio = total / count
 print(f"total grades: {count}")
 print(f"Average: {promedio}")
 print(f"Highest: {major_note}")
 print(f"Lowest: {minor_note}")
 print(f"Approved: {approved}")
 print(f"Failed: {failed}")
 
else: 
 print("no valid grades entered")           
