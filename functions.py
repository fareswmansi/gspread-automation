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
            print("Number: %r not found within google spreadsheet" % (number_list[i]))
            print("Attempting to locate input fields using name...")
            try:
                cell = worksheet.find(name_list[i])
                second_test_coordinate_list.append(cell)
            except:
                print("Name: %r not found withing google spreadsheet") % (name_list[i])
                text_file = open('failed_input.txt', 'a')
                text_file.write("Not found: " + str(number_list[i]) +  " " + str(name_list[i]) + "\n")
                text_file.close()
            
#create coordinates for area input
def row_coordinate_seperate(test_coordinate_list, number_list, row_coordinate):
    for i in range(len(test_coordinate_list)):
        seperateMe = str(test_coordinate_list[i]).replace('<Cell ', '')
        secondSeperate = str(seperateMe).replace('u\'%s' % (number_list[i]), '')
        thirdSeperate = str(secondSeperate).replace(' \'>', '')
        fourthSeperate = str(thirdSeperate).replace('1', '')
        fifthSeperate = str(fourthSeperate).replace('R', '')
        finalSeperate = str(fifthSeperate).replace('C', '')
        row_coordinate.append(finalSeperate)

#area input into google sheet, input failed entrys into empty text file
def area_input(row_coordinate, area_list, number_list):
    for i in range(len(row_coordinate)):
        try:
            worksheet.update_cell(row_coordinate[i], 3, area_list[i])
        except:
            print("Could not input area data for number: %r" % (number_list[i]))
            text_file = open('failed_input.txt', 'a')
            text_file.write("Input data error: " + str(number_list[i]) + "\n")

#building input into google sheet
def building_input(row_coordinate, building_list, number_list):
    for i in range(len(row_coordinate)):
        try:
            worksheet.update_cell(row_coordinate[i], 4, building_list[i])
        except:
            pass

#location innput into google sheet
def location_input(row_coordinate, location_list, number_list):
    for i in range(len(row_coordinate)):
        try:
            worksheet.update_cell(row_coordinate[i], 5, location_list[i])
        except:
            pass

#delete
def find_customers(recurring_customers_raw):
    values = worksheet.col_values(1)
    recurring_customers_raw.append(values)
#delete
def customer_seperate(recurring_customers, recurring_customers_raw):
    for i in range(len(recurring_customers_raw)):
        seperatefirst = str(recurring_customers_raw[i]).replace('u\'Number\',', '')
        seperatesecond = str(seperatefirst).replace('u\'', '')
        finalseperate = str(seperatesecond).replace('\'', '')
        recurring_customers.append(finalseperate)
#delete
def find_recurring(recurring_customers):
    for i in range(len(recurring_customers)):
        if recurring_customers[i] == recurring_customers[i]:
            print(recurring_customers[i])
        else:
            print("No recurring customers founnd.")



#gets value of all numbers in google spreadsheet
def getting_cell_value(recurring_customers_raw, recurring_customers):
    cell = worksheet.col_values(1, value_render_option='FORMATTED_VALUE')
    recurring_customers_raw.append(cell)
    for list in recurring_customers_raw:
        list.pop(0)
        for i in range(len(list)):
            recurring_customers.append(list[i])

#seperates 
def matched_string(recurring_customers, final_recurring_customers):
    for i in range(len(recurring_customers)):
        seperatefirst = str(recurring_customers[i]).replace('u\'', '')
        final_recurring_customers.append(seperatefirst)

def find_matched_string(number_list, test_list, test_test_list):
    for i in range(len(number_list)):
        cell_list = worksheet.findall(number_list[i])
        test_list.append(cell_list)
        for i in range(len(test_list)):
            if test_list[i][1] == True:
                print(test_list[i][1])
            else:
                print("No recurring customers found.")

#create coordinates for area input
def row_coordinate_seperate_failedInput(second_test_coordinate_list, name_list, second_row_coordinate):
    for i in range(len(second_test_coordinate_list)):
        seperateMe = str(second_test_coordinate_list[i]).replace('<Cell ', '')
        secondSeperate = str(seperateMe).replace('u\'%s' % (name_list[i]), '')
        thirdSeperate = str(secondSeperate).replace(' \'>', '')
        fourthSeperate = str(thirdSeperate).replace('1', '')
        fifthSeperate = str(fourthSeperate).replace('R', '')
        finalSeperate = str(fifthSeperate).replace('C', '')
        second_row_coordinate.append(finalSeperate)

#area input into google sheet, input failed entrys into empty text file
def area_input_failedInput(second_row_coordinate, area_list, name_list):
    for i in range(len(second_row_coordinate)):
        try:
            worksheet.update_cell(second_row_coordinate[i], 3, area_list[i])
        except:
            print("Could not input area data for number: %r" % (name_list[i]))
            text_file = open('failed_input.txt', 'a')
            text_file.write("Input data error: " + str(name_list[i]) + "\n")

#building input into google sheet
def building_input_failedInput(second_row_coordinate, building_list, name_list):
    for i in range(len(second_row_coordinate)):
        try:
            worksheet.update_cell(second_row_coordinate[i], 4, building_list[i])
        except:
            pass

#location innput into google sheet
def location_input_failedInput(second_row_coordinate, location_list, name_list):
    for i in range(len(second_row_coordinate)):
        try:
            worksheet.update_cell(second_row_coordinate[i], 5, location_list[i])
        except:
            pass