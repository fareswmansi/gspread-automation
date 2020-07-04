from lists import database_list_of_lists, number_list, area_list, building_list, location_list, test_coordinate_list, row_coordinate, recurring_customers, recurring_customers_raw, final_recurring_customers
from variables import scope, credentials, worksheet, client
from functions import number_loop, area_loop, building_loop, location_loop, find_strings, row_coordinate_seperate, area_input, building_input, location_input, find_customers, customer_seperate, find_recurring, getting_cell_value, matched_string, find_matched_string


print("Welcome to the google sheet automation program, to begin automating, press YES")
first_choice = raw_input('')

if first_choice == 'yes' or first_choice == 'YES':
    print("Would you like to automate the program or find recurring orders?")
    second_choice = raw_input("")
    
    if second_choice == '1':
        print("What is the name of the sheet you would like to access?")
        sheet_name = raw_input('')
        sheet = client.open('testme3').sheet1

        #split data from databse and input into list in correct order
        number_loop(database_list_of_lists, number_list)
        area_loop(database_list_of_lists, area_list)
        building_loop(database_list_of_lists, building_list)
        location_loop(database_list_of_lists, location_list)

        #create coordinates for data input 
        find_strings(test_coordinate_list, number_list)
        row_coordinate_seperate(test_coordinate_list, number_list, row_coordinate)
        
        #input data into google sheet
        area_input(row_coordinate, area_list)
        building_input(row_coordinate, building_list)
        location_input(row_coordinate, location_list)

        print("Recurring customers: ")

        getting_cell_value(recurring_customers_raw, recurring_customers)
        matched_string(recurring_customers, final_recurring_customers)
        find_matched_string(final_recurring_customers)

    else:
        print("Finding recurring orders...")
        find_customers(recurring_customers_raw)
        customer_seperate(recurring_customers, recurring_customers_raw)
        find_recurring(recurring_customers)