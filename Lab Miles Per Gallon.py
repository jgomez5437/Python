#Jesus Gomez Martinez
#22561 Prog & Prob Solv 2
#Miles Per Gallon

"""This is a program that will calculate the average miles/gallon after receiving
input from the user."""

#Initializes the variables used.
gallons = 0
miles = 0
gallonsTotal = 0
milesTotal = 0

#This will ask for the initial data from the user and display the average
#for the entered trip.
try:
    gallons = float(input("Enter the gallons used (type -1 to end): "))
    if gallons != -1:
     try:    
        miles = float(input("Enter the miles driven: "))
        initialAverage = miles / gallons
        print(f'The miles/gallon for this tank was {initialAverage: .6f}.')
     except:
        print("Please only use numbers.")
except:
    print("Please enter a valid number.")

#This loop will ask for the following trips until the user enters "-1" and will 
#show the average per trip.
while gallons != -1:
    gallonsTotal += gallons
    milesTotal += miles
    try:    
        gallons = float(input("Enter the gallons used (type -1 to end): "))
        if gallons != -1:
            miles = float(input("Enter the miles driven: "))
        average = miles / gallons
        print(f'The miles/gallon for this tank was {average: .6f}.')
    except:
        print("Please enter a valid number.")

#This if statement will only run if numbers were entered by the user.
#It will then calculate a total average of all trips and display it.
if gallonsTotal != 0:
    average = milesTotal / gallonsTotal
    print(f'The overall average miles/gallon was {average: .6f}.')
else:
    print("Goodbye.")
