def calRun():
    while True:
        try:
            sName = input("\nEnter Students Name: ")
            regNum = input("Enter Registration Number: ")
            mathMarks = int(input("Enter Math marks: "))
            engMarks = int(input("Enter English marks: "))
            scienceMarks = int(input("Enter science marks: "))
            humanityMarks = int(input("Enter Humanities marks: "))
            
            average = (mathMarks + engMarks + scienceMarks + humanityMarks) / 4
            
            if 90 <= average <= 100:
                grade = 'A'
            elif 80 <= average < 90:
                grade = 'B'
            elif 70 <= average < 80:
                grade = 'C'
            elif 60 <= average < 70:
                grade = 'D'
            elif average <= 60:
                grade = 'E'
            else:
                print("Invalid")
                grade = None

            print(f"\nStudent Name: {sName}"
                  f"\nRegistration Number: {regNum}"
                  f"\nAverage score is: {average:.2f}"
                  f"\nFinal Grade: {grade}\n")
                  
        except ValueError:
            print("Error: Please enter valid numerical values for marks")

calRun()