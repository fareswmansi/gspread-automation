from functions2 import progress_bar, first_check, you_may_pass, name_loop, number_loop, area_loop, building_loop, location_loop, find_strings, row_coordinate_seperate, row_coordinate_seperate, row_coordinate_seperate_failedInput
from lists import test_coordinate_list, number_list, row_coordinate, name_list, building_list, location_list, area_list, database_list_of_lists, final_check_list, first_check_list, second_test_coordinate_list, row_coordinate, second_row_coordinate

first_check(first_check_list, final_check_list)
you_may_pass(final_check_list)

progress_bar()
name_loop(database_list_of_lists, name_list)
number_loop(database_list_of_lists, number_list)
area_loop(database_list_of_lists, area_list)
building_loop(database_list_of_lists, building_list)
location_loop(database_list_of_lists, location_list)

find_strings(test_coordinate_list, number_list, name_list, second_test_coordinate_list)
print(test_coordinate_list)
print(second_test_coordinate_list)
row_coordinate_seperate(test_coordinate_list, number_list, row_coordinate)
print(row_coordinate)
row_coordinate_seperate_failedInput(second_test_coordinate_list, name_list, second_row_coordinate)
print(second_row_coordinate)