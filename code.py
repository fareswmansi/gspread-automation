from lists import database_list_of_lists, number_list, area_list, building_list, location_list, test_coordinate_list, row_coordinate, recurring_customers, recurring_customers_raw, final_recurring_customers, test_list, test_test_list, first_check_list, final_check_list, write_in_me, name_list, second_test_coordinate_list, second_row_coordinate
from functions import number_loop, area_loop, building_loop, location_loop, find_strings, row_coordinate_seperate, area_input, building_input, location_input, find_customers, customer_seperate, find_recurring, getting_cell_value, matched_string, find_matched_string, first_check, you_may_pass, progress_bar, name_loop, row_coordinate_seperate_failedInput, area_input_failedInput, building_input_failedInput, location_input_failedInput

raw_input("Welcome to the gspread automation program. To continue, press enter.")

first_check(first_check_list, final_check_list)
you_may_pass(final_check_list)

progress_bar()
#split data from databse and input into list in correct order
name_loop(database_list_of_lists, name_list)
number_loop(database_list_of_lists, number_list)
area_loop(database_list_of_lists, area_list)
building_loop(database_list_of_lists, building_list)
location_loop(database_list_of_lists, location_list)

#create coordinates for data input 
find_strings(test_coordinate_list, number_list, name_list, second_test_coordinate_list)
row_coordinate_seperate(test_coordinate_list, number_list, row_coordinate)
row_coordinate_seperate_failedInput(second_test_coordinate_list, name_list, second_row_coordinate)

#input data into google sheet
area_input(row_coordinate, area_list, number_list)
area_input_failedInput(second_row_coordinate, area_list, name_list)
building_input(row_coordinate, building_list, number_list)
building_input_failedInput(second_row_coordinate, building_list, name_list)
location_input(row_coordinate, location_list, number_list)
location_input_failedInput(second_row_coordinate, location_list, name_list)

progress_bar()
print("Recurring customers: ")
#find recurring customers
getting_cell_value(recurring_customers_raw, recurring_customers)
matched_string(recurring_customers, final_recurring_customers)
print(final_recurring_customers)
"""find_matched_string(number_list, test_list, test_test_list)"""