choice = None
while choice is None:
    input_value = input("Greetings Professor. Please enter 1 or 2: ")
    try:
        choice = int(input_value)
    except ValueError:
        print("{input} is not an option, please enter 1 or 2".format(input=input_value))
if choice == 1:
    while True:    
            print('Paycheck calculator. Great choice!')
            user=input("\nPlease enter name:")     
            hoursWorked=(float(input("Enter hours:",)))
            payRate=(float(input("Enter payrate:$",)))
            if hoursWorked <=40:
                print("Looks like there's too much month at the end of your check", user)
                print("Employee's name:",user)
                print("Hours worked:" ,hoursWorked)
                print("Hourly rate:$" ,payRate)
                pay=(hoursWorked*payRate)
                print("Paycheck amount $", pay)
            elif hoursWorked >40:
                print("File a wage claim! You should be getting overtime.")
                print("Employee's name:",user)
                print("Hours worked:" ,hoursWorked)
                print("Hourly rate:$" ,payRate)
                pay=(hoursWorked*payRate)
                print("Paycheck amount $",pay)
            answer = input("Would you like to try again? Y/N:")
            if answer not in ("y","n"):
                print("Invalid")
                break
            if answer =="y":
                continue
            else:
                input("\nPress the enter key to exit")
                break 
          
if choice == 2:
    while True:
            print("Fine choice!")      
            print('Miles per Gallon')
            user=input("\nPlease enter vehicle name:")
            milesDriven=(float(input("Enter miles drove:",)))
            gallonsUsed=(float(input("Enter gallons used:",)))
            if milesDriven >0:
                print("Fuel calc")
                print("Vehicle name:",user)
                print("Miles driven:" ,milesDriven)
                print("Gallons used:" ,gallonsUsed)
                mpg=(milesDriven/gallonsUsed)
                print("Miles per gallon", mpg)
                answer = input("Would you like to try again? Y/N:")
            if answer not in ("y","n"):
                print("Invalid")
                break
            if answer =="y":
                continue
            else:
                break
