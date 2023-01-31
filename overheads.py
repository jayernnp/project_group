from pathlib import Path
import csv

# to create file from file path
overhead=Path.cwd()/'project_group'/'csv_reports'/'overheads.csv'

# read the overhead file
with overhead.open(mode='r', encoding='UTF-8') as file:
    reader=csv.reader(file)
    next(reader) #skip the header

    # Define an empty list to store the overhead values and categories
    overheadlist=[]

    # Loop through each row in the reader 
    for row in reader:
        # Append the value in the first column (index 0, day) & second column (index 1, percentage) to the overheads list
        # For the second column, it also converts the percentage values to float before appending into the list. 
        overheadlist.append([row[0],float(row[1])])


# Defines the function to identify the overhead category with the highest percentage.
def overhead_check():
    """
    Function identifies the overhead with the highest percentage and returns the value and overhead category
    """
    
    # Creates 2 empty lists to store the percentage and category names respectively.
    percentage_list=[]
    category_list=[]

    # Defines the variable used to identify the index of the category with the highest percentage.
    max_index=0

    # Creates a for loop so that the program reads through every set of data in the overheadlist list.
    for data in overheadlist:

        # First, the program will append the category name into the category_list list (first column, index 0)
        category_list.append(data[0])

        # Then, the program will convert the percentage value (2nd column, index 1) into float and store it into the floatdata variable.
        floatdata=float(data[1])
        # The program will then append this float value into the percentage_list list.
        percentage_list.append(floatdata)
    
    # After the program has read through every set of data, the program will then identify the 
    # highest value in the percentage_list using the max function.
    highest_percentage=max(percentage_list)
    
    # Creates a for loop to identify the index of the highest percentage value, placing the value using the enumerate function.
    for value in enumerate(percentage_list):

        # When the for loop identifies the highest_percentage value
        if value==highest_percentage:
            # the max_index value will be equal to the index of this highest_percentage value.
            max_index=value
    
    # After the program identified the index of the highest_percentage value, the program will proceed to find the 
    # name of the category with the same index, aka the category name of the highest_percentage, then convert every character
    # in the category name into upper case, storing this upper case name of the category in the percent_category variable.
    percent_category=(category_list[max_index]).upper()
    
    # The program will then return the statement of the highest overhead, with the name of the percent_category and the highest_percentage
    return f'[HIGHEST OVERHEADS] {percent_category}: {highest_percentage}%'
            

