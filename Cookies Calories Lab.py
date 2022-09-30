#This is a calculator to count how many calories were eaten from cookies.

print("Welcome to the cookie calorie counter 3000.")

calorieServ = 200
servings = 10
cookies = 40

cookEaten = int(input("How many cookies did you eat?: "))

totalCalBag = calorieServ * servings
calPerCookie = totalCalBag / cookies
calEaten = cookEaten * calPerCookie

print("Total amount of calories eaten: ",calEaten)

