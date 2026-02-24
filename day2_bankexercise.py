# EXERCISE 2

name = input("what is your name: " )
age = int(input("what is your age: "))
monthly_income = int(input("what is your monthly income:  ")) 
do_you_have_debs = input("do you have debs? (Y/N) ")    
Length_of_service = int(input("what is your length of service in years:  "))

print(f"evaluating your loan application...")


if age < 21:
    print("you are not eligible for the loan, you are a minor")
else:
    if monthly_income > 1500 and do_you_have_debs == "N":
        print("you are eligible for the loan")
        
        if monthly_income >= 3000:
            print("Your are a premium cliente")
        if Length_of_service >= 5:
            print("you are a loyal customer")
    elif monthly_income > 1500 and do_you_have_debs == "Y":
        print("you are eligible for the loan, but subject to review")
                     
    else: 
        print("you are not eligible for the loan, your income is too low")