![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!

# Fuel Card Analysis Program

This is an online data entry program for a user in the Fuel Card Team to enter in survey results returned by customers or to view the analysis of the surveys already entered. The analysis will also be entered into the Analysis worksheet.

## User Story

+ As a member of a Fuel Card team, we have issued out surveys to all current customers to analyze our customer base and see how they rate our service. We want to be able to enter
data returned and also view the analysis and have it entered into a spreadsheet so it can be monitored and differences viewed as more results are entered.

## Implementation flow chart

![Image of flow chart](docs/Flow-chart-pp3.png)

## Features

+ Allows the user to enter in recevied survey results from customers
+ Data is validated and if invalid, it will inform the user and ask for the data to be entered again.
+ Display the analysis of all entered data to the user via the terminal
+ Enters the analysis into the Analysis spreadsheet on Google Sheets

## Libraries Used

+ Gspread
+ DateTime
+ OS
+ Pandas

## Testing

To test the program for entering data, please enter the below;

| Question                  | Answer |
| --------                  | ------ |
| County:                   | Sligo  |
| Number of vehicles:       | 9      |
| Monthly spend (lts):      | 10000  |
| Monthly spend (€):        | 18500  |
| Limited or sole trader:   | LTD    |
| Service Rating:           | 5      |
| Price Rating:             | 1      |
| Sites Rating:             | 4      |
| Reliabilty Rating:        | 5      |


This data will then be entered in a new row on the Data worksheet.

To view the analysis, select 2 and the data will be displayed to the screen and entered into the Analysis spreadsheet.


## Bugs

+ There was an issue when trying to seperate out the array which contained the entered data. As there was a combination of both strings and integers, these had to be seperated out so the data could be validated. 
+ When getting the current customer count, it was not working correctly. I then imported the Pandas library and used the "value_counts" which returned the correct value.
+ There was an issue where they were warnings detected from lines being too long.
I reseached this and was able to resolve. 

## Validator Testing

I ran the Python code through the linter at https://pep8ci.herokuapp.com/# and there were no errors found.

![Validated Python code](docs/Python-Linter.png)

## Deployment

This program was deployed using Heroku.
Live link :
Repository :
Google Sheet: 

## Credits

+ Love Sandwiches walkthrough.
+ https://www.w3schools.com/python/pandas/pandas_getting_started.asp for importing and using the Pandas library.
+ https://www.geeksforgeeks.org/get-current-date-using-python/ for importing the date time library.
+ https://www.delftstack.com/howto/python/python-clear-console/?utm_content=cmp-true for importing and using the OS library
+ https://www.codecademy.com/resources/docs/markdown/tables for using tables in Markdown

