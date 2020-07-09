from variables import worksheet
import time
from tqdm import tqdm

#progress bar to indicate commpletion progress
def progress_bar():
    for i in tqdm(range(10)):
        time.sleep(1)

#gets values of label columns in order to proceed with the checking process
def first_check(first_check_list, final_check_list):
    values_list = worksheet.row_values(1)
    first_check_list.append(values_list)
    for list in first_check_list:
        for i in range(len(list)):
            seperateme = str(list[i]).replace('u', '')
            final_check_list.append(seperateme)

#checks the column names in empty spreadsheet to avoid confusion and check compatibility
def you_may_pass(final_check_list):
    if (final_check_list[0] == 'Name') and (final_check_list[1] == 'Nmber') and (final_check_list[2] == 'Area') and (final_check_list[3] == 'Bilding/Villa') and (final_check_list[4] == 'Location'):
        return True
    else:
        print("Please edit the names of the columns in ur spreadsheet: col1 = Name, col2 = Number, col3 = Area, col4 = Bilding/Villa, col5 = Location")
        exit(0)

#loop through database list and seperate name
def name_loop(database_list_of_lists, name_list):
    for i in range(len(database_list_of_lists)):
        name_list.append(database_list_of_lists[i][1])

#loop through database list and seperate phone number
def number_loop(database_list_of_lists, number_list):
    for i in range(len(database_list_of_lists)):
        number_list.append(database_list_of_lists[i][2])

#loop through database list and seperate area
def area_loop(database_list_of_lists, area_list):
    for i in range(len(database_list_of_lists)):
        area_list.append(database_list_of_lists[i][3])

#loop through databse list and seperate building #
def building_loop(database_list_of_lists, building_list):
    for i in range(len(database_list_of_lists)):
        building_list.append(database_list_of_lists[i][4])

#loop through database list and seperate location coordinates
def location_loop(database_list_of_lists, location_list):
    for i in range(len(database_list_of_lists)):
        location_list.append(database_list_of_lists[i][5])

#find strings for number input
def find_strings(test_coordinate_list, number_list, name_list, second_test_coordinate_list, use_me):
    for i in range(len(number_list)):
        try:
            cell = worksheet.find(number_list[i])
            test_coordinate_list.append(cell)
        except:
            print("Number %r not found within the google spreadsheet" % (number_list[i]))
            use_me.append(number_list[i])
            print("Attempting to locate input fields using name...")
            try:
                cell = worksheet.find(name_list[i])
                second_test_coordinate_list.append(cell)
            except:
                print("Name: %r not found within the google spreadsheet." % (name_list[i]))
                text_file = open('failed_input.txt', 'a')
                text_file.write("Not found: " + str(name_list[i]) + "\n")
                text_file.close()

#create index to append data to lists to input data using name
def create_index(use_me, number_list, index_list):
    for i in range(len(use_me)):
        index = number_list.index(use_me[i])
        index_list.append(index)

#append data from area list for name input
def second_area_loop(index_list, area_list, second_area_list):
    for i in range(len(index_list)):
        append_me = area_list[index_list[i]]
        second_area_list.append(append_me)

#append data from building list for name input
def second_building_loop(index_list, building_list, second_building_list):
    for i in range(len(index_list)):
        append_me = building_list[index_list[i]]
        second_building_list.append(append_me)

#append data from location list for name input
def second_location_loop(index_list, location_list, second_location_list):
    for i in range(len(index_list)):
        append_me = location_list[index_list[i]]
        second_location_list.append(append_me)

#create coordinates for area input
def row_coordinate_seperate(test_coordinate_list, number_list, row_coordinate):
    for i in range(len(test_coordinate_list)):
        seperateMe = str(test_coordinate_list[i]).replace('<Cell ', '')
        thirdSeperate = str(seperateMe).replace(' \'>', '')
        fourthSeperate = str(thirdSeperate).replace('R', '')
        finalSeperate = str(fourthSeperate).replace('C2', '')
        sep = ' '
        rest = finalSeperate.split(sep, 1)[0]
        row_coordinate.append(rest)

#create coordinates for area input
def row_coordinate_seperate_failedInput(second_test_coordinate_list, test_test_test_test, name_list, second_row_coordinate):
    for i in range(len(second_test_coordinate_list)):
        seperateMe = str(second_test_coordinate_list[i]).replace('<Cell ', '')
        thirdSeperate = str(seperateMe).replace(' \'>', '')
        fourthSeperate = str(thirdSeperate).replace('R', '')
        finalSeperate = str(fourthSeperate).replace('C1', '')
        sep = ' '
        rest = finalSeperate.split(sep, 1)[0]
        second_row_coordinate.append(rest)

#input area data from number list
def area_input(row_coordinate, area_list, number_list):
    for i in range(len(row_coordinate)):
        try:
            worksheet.update_cell(row_coordinate[i], 3, area_list[i])
        except:
            print("Could not input data for number: %r" % number_list[i])
            text_file = open('failed_input.txt', 'a')
            text_file.write("Input data error: " + str(number_list[i]) + "\n")

#input area data from name list
def second_area_input(second_row_coordinate, second_area_list, name_list):
    for i in range(len(name_list)):
        try:
            worksheet.update_cell(second_row_coordinate[i], 3, second_area_list[i])
        except:
            print("Could not input data for name: %r" % name_list[i])
            text_file = open('failed_input.txt', 'a')
            text_file.write("Input data error: " + str(name_list[i]) + "\n")

#input building data from number list
def building_input(row_coordinate, building_list):
    for i in range(len(row_coordinate)):
        try:
            worksheet.update_cell(row_coordinate[i], 4, building_list[i])
        except:
            pass

#input building data from name list
def second_building_input(second_row_coordinate, second_building_list):
    for i in range(len(second_row_coordinate)):
        try:
            worksheet.update_cell(second_row_coordinate[i], 4, second_building_list[i])
        except:
            pass

#input location data from number list
def location_input(row_coordinate, location_list):
    for i in range(len(row_coordinate)):
        try:
            worksheet.update_cell(row_coordinate[i], 5, location_list[i])
        except:
            pass

#input location data from name list
def second_location_input(second_row_coordinate, second_location_list):
    for i in range(len(second_row_coordinate)):
        try:
            worksheet.update_cell(second_row_coordinate[i], 5, second_location_list[i])
        except:
            pass

def final_check(row_coordinate, second_row_coordinate):
    length = len(row_coordinate) + len(second_row_coordinate)
    for i in range(length):
        cell = worksheet.find()
