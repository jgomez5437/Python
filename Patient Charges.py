#Jesus Gomez Martinez
#10080 Prog & Prob Solv 1
#Patient Charges Final

from datetime import date
from prettytable import PrettyTable

#This is the Patient class that will hold the patient's information.
class Patient():
    def __init__(self, fullName=None, address=None, phoneNum=None, contact=None):
        self.__patientInfo = fullName
        self.__patientHome = address
        self.__patientPhone = phoneNum
        self.__emContact = contact
    #mutator methods
    def set_patientInfo(self, fullName):
        self.__patientInfo = fullName
    def set_patientHome(self, address):
        self.__patientHome = address
    def set_patientPhone(self, phoneNum):
        self.__patientPhone = phoneNum
    def set_emContact(self, contact):
        self.__emContact = contact
    #accessor methods
    def get_patientInfo(self):
        return self.__patientInfo
    def get_patientHome(self):
        return self.__patientHome
    def get_patientPhone(self):
        return self.__patientPhone
    def get_emContact(self):
        return self.__emContact

#This is the Procedure class that will hold the information
#of a gicen procedure.
class Procedure():
    def __init__(self, namePro=None, datePro=None, practOfPro=None, cost=None):
        self.__nameOfPro = namePro
        self.__dateOfPro = datePro
        self.__practitioner = practOfPro
        self.__costOfPro = cost
    #mutator methods
    def set_nameOfPro(self, namePro):
        self.__nameOfPro = namePro
    def set_dateOfPro(self, datePro):
        self.__dateOfPro = datePro
    def set_practitioner(self, practOfPro):
        self.__practitioner = practOfPro
    def set_costOfPro(self, cost):
        self.__costOfPro = cost
    #accessor methods
    def get_nameOfPro(self):
        return self.__nameOfPro
    def get_dateOfPro(self):
        return self.__dateOfPro
    def get_practitioner(self):
        return self.__practitioner
    def get_costOfPro(self):
        return self.__costOfPro

#This will be the main module in a program to obtain information about a patient
#and the offered procedures and display them.
def main():
    #These are module calls for obtaining patient information.
    patientName = getPatientName()
    patientAddress = getPatientAddress()
    patientPhone = getPatientPhone()
    patientEmContact = getEmergContact()
    #This creates an instance of patient with the patient information we received.
    patient = Patient(patientName, patientAddress, patientPhone, patientEmContact)
    #These are the three instances for the procedures which inherit the Procedure class.
    physicalExam = Procedure("Physical Exam", date.today(), "Dr. Irvine", "Charge: $250")
    xRay = Procedure("X-ray", date.today(), "Dr. Irvine", "Charge: $500")
    bloodTest = Procedure("Blood Test", date.today(), "Dr. Smith", "Charge: $200")
    #These print statements will show the patient's infromation.
    print()
    print("Here is your patient's information:")
    print(patient.get_patientInfo())
    print(patient.get_patientHome())
    print(patient.get_patientPhone())
    print(patient.get_emContact())
    print()
    #This table will show the information about the procedures.
    table = PrettyTable()
    table.field_names = ["Procedure 1", "Procedure 2", "Procedure 3"]
    table.add_row([physicalExam.get_nameOfPro(), xRay.get_nameOfPro(), bloodTest.get_nameOfPro()])
    table.add_row([physicalExam.get_dateOfPro(), xRay.get_dateOfPro(), bloodTest.get_dateOfPro()])
    table.add_row([physicalExam.get_practitioner(), xRay.get_practitioner(), bloodTest.get_practitioner()])
    table.add_row([physicalExam.get_costOfPro(), xRay.get_costOfPro(), bloodTest.get_costOfPro()])
    print(table)
    
#This is the module to get the patient name.
def getPatientName():
    patientName = input("What is the name of the patient? ")
    return patientName
#This is the module to get the address of the patient.
def getPatientAddress():
    address = str(input("Enter the patient's address. \
(Format: Address, City, State, ZIP code): "))

    return address
#This module will get the patient's phone number.
def getPatientPhone():
    counter = 0
    while counter == 0:
      try:  
        number = int(input("Enter the patient's phone number: "))
        counter += 1
      except:
        print("Please enter only numbers for the phone number.")
    return number
#This module will get the patient's emergency contact.
def getEmergContact():
    contact = str(input("Enter the name and phone number of the \
patient's emergency contact: "))
    return contact

main()