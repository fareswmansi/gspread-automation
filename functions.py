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

#create coordinates for number input
def number_coordinate_create(number_coordinate_list, number_list):
    coordinate = 'A'
    for i in range(2, (len(number_list) + 2)):
        append_this = coordinate + str(i)
        number_coordinate_list.append(append_this)

#create coordinates for area input
def area_coordinate_create(area_coordinate_list, area_list):
    coordinate = 'B'
    for i in range(2, (len(area_list) + 2)):
        append_this = coordinate + str(i)
        area_coordinate_list.append(append_this)

#create coordinates for building input
def building_coordinate_create(building_coordinate_list, building_list):
    coordinate = 'C'
    for i in range(2, (len(building_list) + 2)):
        append_this = coordinate + str(i)
        building_coordinate_list.append(append_this)

#create coordinate for location input
def location_coordinate_create(location_coordinate_list, location_list):
    coordinate = 'D'
    for i in range(2, (len(location_list) + 2)):
        append_this = coordinate + str(i)
        location_coordinate_list.append(append_this)