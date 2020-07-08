from functions2 import progress_bar, first_check, you_may_pass, name_loop, number_loop, area_loop, building_loop, location_loop, find_strings, row_coordinate_seperate, row_coordinate_seperate_failedInput, area_input, second_area_input, create_index, second_area_loop, second_building_loop, second_location_loop, second_building_input, second_location_input,  building_input, location_input
from lists import test_coordinate_list, number_list, row_coordinate, name_list, building_list, location_list, area_list, database_list_of_lists, final_check_list, first_check_list, second_test_coordinate_list, row_coordinate, second_row_coordinate, test_test_test_test, use_me, index_list, second_area_list, second_building_list, second_location_list

#check spreadsheet compatibility
first_check(first_check_list, final_check_list)
you_may_pass(final_check_list)

progress_bar()
#create lists for data input using number
name_loop(database_list_of_lists, name_list)
number_loop(database_list_of_lists, number_list)
area_loop(database_list_of_lists, area_list)
building_loop(database_list_of_lists, building_list)
location_loop(database_list_of_lists, location_list)

#create coordinates using number and name
find_strings(test_coordinate_list, number_list, name_list, second_test_coordinate_list, use_me)
row_coordinate_seperate(test_coordinate_list, number_list, row_coordinate)
row_coordinate_seperate_failedInput(second_test_coordinate_list, test_test_test_test, name_list, second_row_coordinate)
create_index(use_me, number_list, index_list)

#create lists for data input using name 
second_area_loop(index_list, area_list, second_area_list)
second_building_loop(index_list, building_list, second_building_list)
second_location_loop(index_list, location_list, second_location_list)

#input data
area_input(row_coordinate, area_list, number_list)
second_area_input(second_row_coordinate, second_area_list, name_list)
building_input(row_coordinate, building_list)
second_building_input(second_row_coordinate, second_building_list)
location_input(row_coordinate, location_list)
second_location_input(second_row_coordinate, second_location_list)
