while True:

    Mongatoname = input("What's your name? ")

    while True:
        Mongatopos = input("Position: ")

        if Mongatopos.lower() == "janitor":
            MongatoMthly = 18000
            break

        elif Mongatopos.lower() == "clerk":
            MongatoMthly = 22000
            break

        elif Mongatopos.lower() == "cashier":
            MongatoMthly = 24000
            break

        elif Mongatopos.lower() == "manager":
            MongatoMthly = 40000
            break

        else:
            print("Position Non-existent, Please Try Again")


    Mongatohours = float(input("Actual Hours Worked: "))


    MongatoBasMonthSal = MongatoMthly / 2
    MongatoHourate = MongatoBasMonthSal / 88

    Mongato_Absent_Hours = 0
    Mongato_Absence_Deduc = 0
    Mongato_Overtime_Hours = 0
    Mongato_Overtime_Rate = 0
    Mongato_Overtime_Pay = 0


    match Mongatohours:
        case hours if hours < 88:
            Mongato_Absent_Hours = 88 - Mongatohours
            Mongato_Absence_Deduc = Mongato_Absent_Hours * MongatoHourate

        case hours if hours > 88:
            Mongato_Overtime_Hours = Mongatohours - 88
            Mongato_Overtime_Rate = MongatoHourate * 1.25
            Mongato_Overtime_Pay = Mongato_Overtime_Hours * Mongato_Overtime_Rate

        case 88:
            Mongato_Absent_Hours = 0
            Mongato_Absence_Deduc = 0
            Mongato_Overtime_Hours = 0
            Mongato_Overtime_Pay = 0


    Mongato_NetSal = (
        MongatoBasMonthSal
        - Mongato_Absence_Deduc
        + Mongato_Overtime_Pay
    )


    print("==============================================")
    print(f"Employee Name: {Mongatoname}")
    print("==============================================")
    print(f"Job Position: {Mongatopos}")
    print("==============================================")
    print(f"Actual Hours Worked: {Mongatohours:.2f}")
    print("==============================================")
    print(f"Monthly Salary: {MongatoMthly:,.2f}")
    print("==============================================")
    print(f"Basic Half-Month Salary: {MongatoBasMonthSal:,.2f}")
    print("==============================================")
    print(f"Hourly Rate: {MongatoHourate:,.2f}")
    print("==============================================")
    print(f"Absent Hours: {Mongato_Absent_Hours:.2f}")
    print("==============================================")
    print(f"Absence Deduction: {Mongato_Absence_Deduc:,.2f}")
    print("==============================================")
    print(f"Overtime Hours: {Mongato_Overtime_Hours:.2f}")
    print("==============================================")
    print(f"Overtime Pay: {Mongato_Overtime_Pay:,.2f}")
    print("==============================================")
    print(f"Net Half-Month Salary: {Mongato_NetSal:,.2f}")
    print("==============================================")


    again = input("Do you wanna try again? (Y/N): ")

    if again.upper() != "Y":
        print("Thank you for using the program!")
        break











