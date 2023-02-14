#Jesus Gomez Martinez
#22561 Prog & Prob Solv 2
#7% Investment Return

"""This is a program that will take input from the user and show them based off
their age, what their maximum heart rate is and their target heart rate."""

#This is the main module that calls all the other functions.
def main():
    baselineToSubtract = 220
    minTargetMultiple = .50
    maxTargetMultiple = .85
    userAge = getUserAge()
    maximumHeartRate = getMaxHeartRate(userAge, baselineToSubtract)
    minTargetRate = getMinTargetRate(maximumHeartRate, minTargetMultiple)
    maxTargetRate = getMaxTargetRate(maximumHeartRate, maxTargetMultiple)
    printInformation(userAge, maximumHeartRate, minTargetRate, maxTargetRate)

#This function will ask the user for their age.
def getUserAge():
    counter = 0
    while counter == 0:
        try:
            userAge = int(input("Please enter your age: "))
            counter += 1
        except:
            print("Please enter a whole number for your age.")
    return userAge

#This function is used to get the maximum heart rate based on age provided.
def getMaxHeartRate(userAge, baselineToSubtract):
    maxHR = baselineToSubtract - userAge
    return maxHR

#This function will get the minimum target heart rate based on maximum heart rate.
def getMinTargetRate(maximumHeartRate, minTargetMultiple):
    minTargetHR = maximumHeartRate * minTargetMultiple
    return minTargetHR

#This function will get the maximum target heart rate based on maximum heart rate.
def getMaxTargetRate(maximumHeartRate, maxTargetMultiple):
    maxTargetHR = maximumHeartRate * maxTargetMultiple
    return maxTargetHR

#This function will be used to print the information to the user.
def printInformation(userAge, maximumHeartRate, minTargetRate, maxTargetRate):
    print("The maximium heart rate for the age of", userAge, "is " + str(maximumHeartRate) + ".\n"
            "Your minimum target heart rate is " + str(minTargetRate) + ".\n"
            "Your maximum target heart rate is " + str(maxTargetRate) + ".")

main()