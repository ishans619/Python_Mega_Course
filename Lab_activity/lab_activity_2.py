English = int(input("enter the marks of English out of 100: "))
Mathematics = int(input("enter the marks of Mathematics out of 100: "))
Physics = int(input("enter the marks of Physics out of 100: "))
Chemistry = int(input("enter the marks of Chemistry out of 100: "))
Computer_Science = int(input("enter the marks of computer_science out of 100: "))
print("\n")

Max_marks = 500

Total = English+Mathematics+Physics+Chemistry+Computer_Science
print("Total marks of the student are: ",Total,"\n")

Average = (English+Mathematics+Physics+Chemistry+Computer_Science)/5
print("Average marks of the student are: ",Average,"\n")

Percentage = (Total/Max_marks)*100
print("Percentage of the student is: ",Percentage)
print("ISHAN SHUKLA , 21BCS7129")
