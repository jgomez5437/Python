#Jesus Gomez Martinez
#10080 Prog & Prob Solv 1
#Programming Lab

#This will be a function that asks the user information about their pet and displays it to them.
#This is the pet class that will carry the fields and the methods.
class Pet():
    def __init__(self, name=None, type=None, age=None):
        self.__namePet = name
        self.__typePet = type
        self.__agePet = age
    def set_name(self, name):
        self.__namePet = name
    def set_type(self, type):
        self.__typePet = type
    def set_age(self, age):
        self.__agePet = age
    def get_name(self):
        return self.__namePet
    def get_type(self):
        return self.__typePet
    def get_age(self):
        return self.__agePet
#This is the main function for the program.
def main():
    animal = Pet()
 #This loop will ask for and make sure the name entered only contains letters.
    counter = 0
    while counter == 0:
      animalName = input("Enter your pet's name: ")
      #This will check if the name only contains the alphabet.
      checkName = animalName.isalpha()
      if checkName:
       animal.set_name(animalName)
       counter += 1
      else:
       print("Please enter a valid pet name.")
       counter = 0
 #This loop will ask for the pet type and makes sure it only contains the alphabet.
    counter = 0  
    while counter == 0:
       animalType = (input("Enter your pet's type: "))
       checkType = animalType.isalpha()
       if checkType:
        animal.set_type(animalType)
        counter += 1
       else:
        print("Please enter a valid pet type.") 
        counter = 0
 #This loop will ask for the age and make sure it is a float type since some users might enter "4.5" for example.
    counter = 0
    while counter == 0:  
      try: 
       animalAge = float(input("Enter your pet's age: "))
       animal.set_age(animalAge)
       counter += 1 
      except:
       print("Please enter a valid number.") 
 #These print statements display the info to the user.
    print("Your pet name:", animal.get_name())
    print("Your pet type:", animal.get_type())
    print("Your pet age:", animal.get_age())
#This calls the main() module.
main()