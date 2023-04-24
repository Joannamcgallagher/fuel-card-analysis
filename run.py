import gspread
from google.oauth2.service_account import Credentials
#import the os so the screen can be cleard
import os

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("fuelCardAnalysis")

# data = SHEET.worksheet("Data")

# d1 = data.get_all_values()
# print(d1)

def clearConsole():
    """
    Function to clear the terminal for the user
    https://www.delftstack.com/howto/python/python-clear-console/?utm_content=cmp-true
    """
    command = "clear"
    if os.name in ("nt", "dos"):
        command = "cls"
    os.system(command)


def getUserFunction():
    """
    Determine what the user would like to do - enter in data or view the analysis from the survey
    """
    print("Welcome to the Fuel Card analysis program!\nHere you can enter in data from a survery received or view the analysis from the data already received.\n\n")
    while True:
        print("Please select an option below.\n")
        print("Select 1 to enter data or 2 to view the analysis:\n")
        userChoice = input("Enter your option here : ")
        if validateUserChoice(userChoice):
            print("Choice is valid")
            break
    return userChoice

    
def validateUserChoice(choice):
    """
    Take in the users choice as a parameter and using validation, ensure that the choice is correct
    """
    try:
        if int(choice) > 2:
            raise ValueError(f"You need to select either 1 or 2, you selected {choice}")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True


def getUserDataInput():
    """
    Function to retrieve the data the user inputs when they have selected to 
    input more survery data
    """   
    #Use a while true loop so the program can check that the data entered is valid
    while True: 
        customerDetails = [] #array to store the customer details
        print("Please enter the data as received in the survey.\n")        
        county = input("Enter county : ")
        vehicles = input("Enter number of vehicles : ")
        monthlyLiters = input("Enter monthly liters : ")
        monthlyEuro = input("Enter in monthly Euros : ")
        customerType = input("Is customer sole trader or LTD? ")
        print("Please enter a value between 1 and 5 for the below.\n")
        service = input("Enter in rating for service : ")
        price = input("Enter in rating for price : ")
        sites = input("Enter in rating for sites : ")
        reliability = input("Enter in rating for reliability : ")
        customerDetails.append(county, )

def validateUserData(data):
    """
    Function to validate the data the user has entered to add in to the
    survey results.
    """
getUserFunction()
getUserDataInput()

