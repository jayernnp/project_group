from pathlib import Path
import csv

# to create file from file path
cash_on_hand=Path.cwd()/'project_group'/'csv_reports'/'cash-on-hand-usd.csv'
# darrel try
# read the cash on hand file
with cash_on_hand.open(mode='r', encoding='UTF-8') as file:
    reader=csv.reader(file)
    next(reader) #skip the header
    # Define an empty list to store the cash on hand values
    cashonhand=[]
    # Loop through each row in the reader
    for row in reader:
        # Append the value in the first column (index 0, day) and the second column (index 1, cash on hand) to the cashonhand list.
        cashonhand.append([row[0],row[1]])

# Define a function to calculate the cash on hand difference
def cash_calc():
    """
    Function calculates difference in cash on hand compared to previous day if it is lower than previous day
    """

    # Creates an empty list to store the day numbers from the cashonhand list
    firstdaylist=cashonhand[0]
    # Defines the variable used to count the day and the first day number
    day=float(firstdaylist[0])-1

    # Defines the variables used to store the previous COH and deficit count
    previous_cash=0
    deficit_count=0
    
    # Creates 2 empty lists to store the days which have deficit and the deficit amount
    deficit_day=[]
    deficit_cash=[]

    # Creates a for loop so that the program reads through every set of data in the cashonhand list
    for data in cashonhand:
        # Increases the day count by 1 for every data
        day+=1

        # Stores the current cash on hand data in the current_cash variable.
        current_cash=float(data[1])

        # Creates the if condition that if the day number is the same as the first day,
        if day==firstdaylist[0]:
            # it will not do the check to see whether it is less than the previous day
            # instead it will just store the current_cash data into the previous_cash variable
            # so that the check can be done for the next set of data onwards.
            previous_cash+=current_cash

        # If the day number is not the same as the first day,
        else:
            # the program will perform the COH check to see if the cash on hand data is less than the previous day.
            # If the current_cash data is less than the previous_cash variable,
            if current_cash < previous_cash:

                # the program will first increase the deficit count by 1.
                deficit_count+=1
                # Then, the program will count the difference in cash on hand and store it in the cashdiff variable.
                cashdiff=previous_cash-current_cash

                # Then, the program will append the day number into the deficit_day list
                # and the cash on hand difference into the deficit_cash list.
                deficit_day.append(day)
                deficit_cash.append(cashdiff)

                # Afterwards, the program will reset the previous_cash variable to 0, and then replace 
                # it with the current_cash data so that the next set of data will be compared to this set of data.
                previous_cash=0
                previous_cash+=current_cash

            # If the current_cash data is more than the previous_cash variable,
            else:
                # the program will just perform the reset of the previous_cash variable to 0, and then replace
                # it with the current_cash data so that the next set of data will be compared to this set of data.
                previous_cash=0
                previous_cash+=current_cash


    # After every set of data in the cashonhand list has been analysed,
    # the program will go through this if condition to decide what to show to the user.
    # If there is no deficit data, aka the program only goes through the second if condition in the for loop,
    if deficit_count==0:
        # the program will return the cash surplus statement to the user.
        return '[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY'

    # Otherwise,
    else:
        # the program will store the required statements to show to the user in the calc_result variable.
        calc_result = ''

        # Creates a for loop so that the program will go through every data in the deficit_day & deficit_cash lists
        # and ensures that it only does this for the number of deficit_count.
        for calc in range(deficit_count):
            # The program will place the appropriate data for each deficit day and deficit cash into the statement below
            calc_result += f'\n[CASH DEFICIT] DAY: {deficit_day[calc]}, AMOUNT: USD{deficit_cash[calc]}'

        # After every deficit_data has been placed into the calc_result variable, the program will return the calc_result.
        return f'{calc_result}'

