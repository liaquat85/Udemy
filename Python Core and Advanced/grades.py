import math 

mathmarks = int(input("Enter maths marks : "))
physicsmarks = int(input("Enter physics marks : "))
chemistrymarks = int(input("Enter chemistry marks : "))

if mathmarks < 35 or physicsmarks < 35 or chemistrymarks < 35:
    print("Student has failed the exams")
else:
    average = (mathmarks + physicsmarks + chemistrymarks) / 3
    
    if average <= 59:
        grade = 'C'
    elif average <= 69 and average >=60:
        grade = 'B'

    else: 
        grade = 'A'
    print(f"The average marks is {average}")
    print(f"The grade is {grade}")
