# EXERCISE 3 

# GRADE RECORD

total = 0
count= 0
major_note = 0
minor_note = 5

while True:
  grade = float(input(" enter your grade: "))
  if 0 <= grade <= 5:
    total += grade
    count += 1
    if grade > major_note:
        major_note = grade
    if grade < minor_note:
        minor_note = grade
  Continue = input("do you want add another grade? (Y/N) ")
  if Continue == "N":
    break
if count > 0:
    promedio = total / count
    print("grade average: ", promedio)
    print("promedio:", promedio)
    print("major_grade", major_note)
    print("minor_grade", minor_note)
else:
    print("no grades were entered.")
              