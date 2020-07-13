from functions import progress_bar, first_check, you_may_pass, name_loop, number_loop, area_loop, building_loop, location_loop, find_strings, row_coordinate_seperate, row_coordinate_seperate_failedInput, area_input, second_area_input, create_index, second_area_loop, second_building_loop, second_location_loop, second_building_input, second_location_input,  building_input, location_input, final_check
from lists import test_coordinate_list, number_list, row_coordinate, name_list, building_list, location_list, area_list, final_check_list, first_check_list, second_test_coordinate_list, row_coordinate, second_row_coordinate, test_test_test_test, use_me, index_list, second_area_list, second_building_list, second_location_list, all_coordinates, status_list
from data import input_here

raw_input("Welcome to the gspread automation program. To continue, press ENTER")


#check spreadsheet compatibility
first_check(first_check_list, final_check_list)
you_may_pass(final_check_list)

progress_bar()
#create lists for data input using number
name_loop(input_here, name_list)
number_loop(input_here, number_list)
area_loop(input_here, area_list)
building_loop(input_here, building_list)
location_loop(input_here, location_list)

#create coordinates using number and name
find_strings(test_coordinate_list, number_list, name_list, second_test_coordinate_list, use_me)
print(test_coordinate_list)
print(second_test_coordinate_list)
row_coordinate_seperate(test_coordinate_list, number_list, row_coordinate)
row_coordinate_seperate_failedInput(second_test_coordinate_list, test_test_test_test, name_list, second_row_coordinate)
create_index(use_me, number_list, index_list)

#create lists for data input using name 
second_area_loop(index_list, area_list, second_area_list)
second_building_loop(index_list, building_list, second_building_list)
second_location_loop(index_list, location_list, second_location_list)

#input data
progress_bar()
area_input(row_coordinate, area_list, number_list)
second_area_input(second_row_coordinate, second_area_list, name_list)
building_input(row_coordinate, building_list)
second_building_input(second_row_coordinate, second_building_list)
location_input(row_coordinate, location_list)
second_location_input(second_row_coordinate, second_location_list)

#adds status
final_check(second_row_coordinate, row_coordinate, status_list)