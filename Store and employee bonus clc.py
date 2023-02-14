#Jesus Gomez Martinez
#10/15/2022
#10080
#This program will be calculating what bonuses the store and employees receive.

def main():
    monthlySales = getSales()
    salesIncrease = getIncrease()
    storeAmount = storeBonus(monthlySales)
    empAmount = empBonus(salesIncrease)
    printBonus(storeAmount, empAmount)

def getSales():
    monthlySales = float(input("Enter the monthly sales $"))
    return monthlySales

def getIncrease():
    salesIncrease = float(input("Enter percent of sales increase: "))
    salesIncrease = float(salesIncrease)
    salesIncrease = salesIncrease / 100
    return salesIncrease

def storeBonus(monthlySales):
    if monthlySales >= 110000:
        storeAmount = 6000
    elif monthlySales >= 100000:
        storeAmount = 5000
    elif monthlySales >= 90000:
        storeAmount = 4000
    elif monthlySales >= 80000:
        storeAmount = 3000
    else:
        storeAmount = 0
    return storeAmount

def empBonus(salesIncrease):
    if salesIncrease >= .05:
        empAmount = 75
    elif salesIncrease >= .04:
        empAmount = 50
    elif salesIncrease >= .03:
        empAmount = 40
    else:
        empAmount = 0
    return empAmount

def printBonus(storeAmount, empAmount):
    print("The store bonus amount is $", storeAmount)
    print("The employee bonus amount is $", empAmount)
    if storeAmount == 6000 and empAmount == 75:
        print("Congrats! You have reached the highest bonus amounts possible!")

main()