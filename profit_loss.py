from pathlib import Path
import csv

# to create file from file path
profit_loss=Path.cwd()/'project_group'/'csv_reports'/'profit-and-loss-usd.csv'

# read the profit and loss file
with profit_loss.open(mode='r', encoding='UTF-8') as file:
    reader=csv.reader(file)
    next(reader) #skip the header
    # Define an empty list to store the net profit values
    net_profit=[]
    # Loop through each row in the reader 
    for row in reader:
        # Append the value in the first column (index 0, day) & fifth column (index 4, net_profit) to the net_profit list
        net_profit.append([row[0],row[4]])



# Define a function to calculate the profit difference
def profit_calc():
    """
    Function calculates the difference in net profit compared to the previous day if it is lower than the previous day
    """

    # Creates an empty list to store the day numbers from the net_profit list
    firstdaylist=net_profit[0]
    # Defines the variable used to count the day and the first day number
    day=float(firstdaylist[0])-1

    # Defines the variables used to store the previous profit and deficit count
    previous_profit=0
    deficit_count=0
    
    # Creates 2 empty lists to store the days which have deficit and the deficit amount
    deficit_day=[]
    deficit_profit=[]
  
    # Creates a for loop so that the program reads through every set of data in the net_profit list
    for data in net_profit:
        # Increases the day count by 1 for every data
        day+=1
        
        # Stores the net profit data in the current_profit variable.
        current_profit=float(data[1])

        # Creates the if condition that if the day number is the same as the first day,
        if day==firstdaylist[0]:
            # it will not do the check to see whether it is less than the previous day
            # instead it will just store the current_profit data into the previous_profit variable
            # so that the check can be done for the next set of data onwards.
            previous_profit+=current_profit

        # If the day number is not the first day,
        else:
            # the program will perform the profit check to see if the profit data is less than the previous day.
            # If the current_profit data is less than the previous_profit variable,
            if current_profit < previous_profit:
                
                # the program will first increase the deficit count by 1.
                deficit_count+=1
                # Then, the program will count the difference in net profit and store it in the profitdiff variable.
                profitdiff=previous_profit-current_profit

                # Then, the program will append the day number into the deficit_day list
                # and the profit difference into the deficit_profit list.
                deficit_day.append(day)
                deficit_profit.append(profitdiff)

                # Afterwards, the program will reset the previous_profit variable to 0, and then replace 
                # it with the current_profit data so that the next set of data will be compared to this set of data.
                previous_profit=0
                previous_profit+=current_profit
                
            # If the current_profit data is more than the previous_profit variable,
            else:
                # the program will just perform the reset of the previous_profit variable to 0, and then replace
                # it with the current_profit data so that the next set of data will be compared to this set of data.
                previous_profit=0
                previous_profit+=current_profit


    # After every set of data in the net_profit list has been analysed,
    # the program will go through this if condition to decide what to show to the user.
    # If there is no deficit data, aka the program only goes through the second if condition in the for loop,
    if deficit_count==0:
        # the program will return the net profit surplus statement to the user.
        return '[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY'

    # otherwise,
    else:
        # the program will store the required statements to show to the user in the calc_result variable.
        calc_result = ''

        # Creates a for loop so that the program will go through every data in the deficit_day & deficit_profit lists
        # and ensures that it only does this for the number of deficit_count.
        for calc in range(deficit_count):
            # The program will place the appropriate data for each deficit day and deficit profit into the statement below
            calc_result+=f'\n[PROFIT DEFICIT] DAY: {deficit_day[calc]}, AMOUNT: USD{deficit_profit[calc]}'

        # After every deficit_data has been placed into the calc_result variable, the program will return the calc_result.
        return f'{calc_result}'


