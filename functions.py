from variables import worksheet

#loop through database list and seperate phone number
def number_loop(database_list_of_lists, number_list):
    for i in range(len(database_list_of_lists)):
        number_list.append(database_list_of_lists[i][1])

#loop through database list and seperate area
def area_loop(database_list_of_lists, area_list):
    for i in range(len(database_list_of_lists)):
        area_list.append(database_list_of_lists[i][2])

#loop through databse list and seperate building #
def building_loop(database_list_of_lists, building_list):
    for i in range(len(database_list_of_lists)):
        building_list.append(database_list_of_lists[i][3])

#loop through database list and seperate location coordinates
def location_loop(database_list_of_lists, location_list):
    for i in range(len(database_list_of_lists)):
        location_list.append(database_list_of_lists[i][4])


#find strings for number input
def find_strings(test_coordinate_list, number_list):
    for i in range(len(number_list)):
        cell = worksheet.find(number_list[i])
        test_coordinate_list.append(cell)

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

#area input into google sheet
def area_input(row_coordinate, area_list):
    for i in range(len(row_coordinate)):
        worksheet.update_cell(row_coordinate[i], 2, area_list[i])

#building input into google sheet
def building_input(row_coordinate, building_list):
    for i in range(len(row_coordinate)):
        worksheet.update_cell(row_coordinate[i], 3, building_list[i])

#location innput into google sheet
def location_input(row_coordinate, location_list):
    for i in range(len(row_coordinate)):
        worksheet.update_cell(row_coordinate[i], 4, location_list[i])