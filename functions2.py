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

#checks the column names in empty spreadsheet to avoid confusion
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
def find_strings(test_coordinate_list, number_list, name_list, second_test_coordinate_list):
    for i in range(len(number_list)):
        try:
            cell = worksheet.find(number_list[i])
            test_coordinate_list.append(cell)
        except:
            print("Number %r not found within the google spreadsheet" % (number_list[i]))
            print("Attempting to locate input fields using name...")
            for l in range(len(name_list)):
                try:
                    cell = worksheet.find(name_list[l])
                    second_test_coordinate_list.append(cell)
                except:
                    print("Name: %r not found within the google spreadsheet." % (name_list[l]))
                    text_file = open('failed_input.txt', 'a')
                    text_file.write("Not found: " + str(name_list[l]) + "\n")
                    text_file.close()

#create coordinates for area input
def row_coordinate_seperate(test_coordinate_list, number_list, row_coordinate):
    for i in range(len(test_coordinate_list)):
        seperateMe = str(test_coordinate_list[i]).replace('<Cell ', '')
        secondSeperate = str(seperateMe).replace('u\'%s' % (number_list[i]), '')
        thirdSeperate = str(secondSeperate).replace(' \'>', '')
        fourthSeperate = str(thirdSeperate).replace('2', '')
        fifthSeperate = str(fourthSeperate).replace('R', '')
        finalSeperate = str(fifthSeperate).replace('C', '')
        row_coordinate.append(finalSeperate)
        row_coordinate[0] = '2'

#create row coordinates for name inputs
def row_coordinate_seperate_failedInput(second_test_coordinate_list, name_list, second_row_coordinate):
    for i in range(len(second_test_coordinate_list)):
        seperateMe = str(second_test_coordinate_list[i]).replace('<Cell ', '')
        secondSeperate = str(seperateMe).replace('u\'%s' % (name_list[i]), '')
        thirdSeperate = str(secondSeperate).replace(' \'>', '')
        fourthSeperate = str(thirdSeperate).replace('2', '')
        fifthSeperate = str(fourthSeperate).replace('R', '')
        finalSeperate = str(fifthSeperate).replace('C', '')
        second_row_coordinate.append(finalSeperate)

