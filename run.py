import gspread
from google.oauth2.service_account import Credentials
# import the os so the screen can be cleard
# https://www.delftstack.com/howto/python/python-clear-console/?utm_content=cmp-true
import os
# https://www.geeksforgeeks.org/get-current-date-using-python/
from datetime import datetime, date
# https://www.w3schools.com/python/pandas/pandas_getting_started.asp
import pandas as p

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("fuelCardAnalysis")


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
    Determine what the user would like to do - enter in data or view the
    analysis from the survey

    Args: None

    Returns: Validated user choice
    """
    print("\n*******Welcome to the Fuel Card analysis program!*******\n\n"
          "Here you can enter in data from a survery received or view the"
          "analysis from the data already received.\n\n")
    while True:
        print("Please select an option below.\n")
        print("Select 1 to enter data, 2 to view analysis or 3 to exit:\n")
        userChoice = input("Enter your option here : ")
        if validateUserChoice(userChoice):
            print("\nChoice is valid")
            break
    return userChoice


def validateUserChoice(choice):
    """
    Take in the users choice as a parameter and using validation,
    ensure that the choice is correct

    Args: User choice

    Results: None
    """
    try:
        if int(choice) > 3:
            raise ValueError(f"You need to select either 1 or 2, \
                you selected {choice}")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True


def getUserDataInput():
    """
    Function to retrieve the data the user inputs when they have selected to
    input more survery data

    Args: None

    Returns: None
    """
    # Use a while true loop so the program can check that the data entered is
    # valid
    while True:
        customerDetails = []  # array to store the customer details
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
        customerDetails.extend((county, vehicles, monthlyLiters,
                                monthlyEuro, customerType, service,
                                price, sites, reliability))
        if validateUserData(customerDetails):
            print("Customer data is valid")
            break
    updateDataSheet(customerDetails)
    getUserFunction()


def validateUserData(data):
    """
    Function to validate the data the user has entered to add in to the
    survey results.
    Get the data in as a string, check to make sure it's a string, int, int,
    int, string(either sole or ltd), then ints for all ratings

    Args: Values that user has entered
    Returns: None
    """
    detailsStrings = []
    detailsInts = []
    detailsStrings.extend((data[0], data[4]))
    detailsInts.extend((data[1], data[2], data[3], data[5], data[6], data[7],
                        data[8]))

    # now there are 2 arrays - one for strings and one for integers
    try:
        for detail in detailsStrings:
            if detail.isdigit():
                raise ValueError("You have entered a number instead of text")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.")
        return False
    try:
        for num in detailsInts:
            if int(num) < 0:
                raise ValueError("You have entered text instead of a number")
    except ValueError as e:
        print(f"Invalid data: {e}, {num} please try again.")
        return False
    return True


def updateDataSheet(values):
    """
    Function to update the Data google sheet with the values entered

    Args: List of values to be entered

    Return: None
    """
    print("Updating data worksheet....")
    data_worksheet = SHEET.worksheet("Data")
    data_worksheet.append_row(values)
    print("Data worksheet updated successfully....")


def getCustomerCount():
    """
    Function to get calculate the total number of customers

    Args: None

    Return: Total number of customers
    """
    data = SHEET.worksheet("Data")
    cells = data.get_all_values()
    customerCount = (len(cells) - 1)  # Subtract the first row (header)
    return customerCount


def highestCustomerCounty():
    """
    Function to calculate the highest county by customer count.

    Args : None

    Returns : county name and number of customers
    """
    data = SHEET.worksheet("Data")
    column = []
    # get the first column and remove the first element which is the header
    column = data.col_values(1)
    del column[0]
    custCount = []
    # use the pandas library to count the number of times the values appear
    custCount = p.Series(column).value_counts()
    # seperate the first line in the series which is the county with the
    # highest customers
    topCounty = custCount[:1]
    # convert to a string array so it can be split and the values taken
    stringArray = str(topCounty)
    stringArraySplit = stringArray.split()
    # seperate the county and number of customers so it can be returned
    # and then used to enter in sheet
    county = stringArraySplit[0]
    numCustomers = stringArraySplit[1]
    return county, numCustomers


def getAverage(value):
    """
    Function to be used to get the average number of the values passed in

    Args: List of values

    Returns : Average
    """
    # delete the first element as this is the header for the column
    del value[0]
    # convert the list of strings to a list of ints
    valueInts = []
    for x in value:
        valueInts.append(int(x))
    totalSum = sum(valueInts)
    average = round(totalSum / len(value))
    return average


def getAnalysis():
    """
    Function to retrieve the stat from the Data spreadsheet,
    analyze it, display to the user and enter it into the
    Analysis spreadsheet

    Args: None

    Return : None
    """
    # Retrieve the data from the Data worksheet so it can
    # be passed into the functions
    data = SHEET.worksheet("Data")
    liters = data.col_values(3)
    euros = data.col_values(4)
    serviceRatings = data.col_values(6)
    priceRatings = data.col_values(7)
    sitesRatings = data.col_values(8)
    reliabilityRatings = data.col_values(9)
    # create list to contain data to be entered to sheet
    # (convert to strings to be entered)
    analytics = []
    today = str(datetime.now().date())
    analytics.append(today)
    customerCount = getCustomerCount()
    analytics.append(str(customerCount))
    county, numberCustomers = highestCustomerCounty()
    analytics.append(str(county))
    analytics.append(str(numberCustomers))
    averageLiters = getAverage(liters)
    analytics.append(str("{:,}".format(averageLiters)))
    averageEuros = getAverage(euros)
    analytics.append(str("{:,}".format(averageEuros)))
    avgService = getAverage(serviceRatings) 
    analytics.append(str(avgService))
    avgPrice = getAverage(priceRatings)
    analytics.append(str(avgPrice))
    avgSites = getAverage(sitesRatings)
    analytics.append(str(avgSites))
    avgReliability = getAverage(reliabilityRatings)
    analytics.append(str(avgReliability))

    # Call the printAnalysis function to display the details
    printAnalysis(analytics)


def printAnalysis(values):
    """
    Function to print the values passed to the user

    Args: List of the values calculated

    Returns: None
    """

    print("\nSee analysis below of customers whose details",
          "have been entered.\n")
    print(f"Date: {values[0]}\n")
    print(f"Total customer count: {values[1]}\n")
    print(f"County with the highest customers: {values[2]}\n")
    print(f"Number of customers in highest county: {values[3]}\n")
    print(f"Average number of liters used per month: {values[4]}\n")
    print(f"Average Euro's spent per month: {values[5]}\n")
    print(f"Average service rating (1-5): {values[6]}\n")
    print(f"Average price rating (1-5): {values[7]}\n")
    print(f"Average sites rating (1-5): {values[8]}\n")
    print(f"Average reliability rating (1-5): {values[9]}\n")

    # Enter the above into the Analysis speadsheet
    enterAnaylsis(values)


def enterAnaylsis(results):
    """
    Function to enter the values passed in to the Analysis sheet

    Args: List of values calculated from getAnalysis function

    Returns: None
    """
    print("Updating analysis worksheet, please wait.......\n")
    worksheet = SHEET.worksheet("Analysis")
    worksheet.append_row(results)
    print("Analysis worksheet updated successfully!\n")
    print("************************************************")


def main():
    """
    Runs all the main functions
    """
    choice = getUserFunction()
    # check the choice variable to see what the user has chosen
    if int(choice) == 1:
        clearConsole()
        getUserDataInput()
    elif int(choice) == 2:
        clearConsole()
        getAnalysis()
    else:
        print("\nExiting.......")
        exit()


main()
