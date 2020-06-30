from lists import database_list_of_lists, number_list, building_list, area_list, location_list, number_coordinate_list, area_coordinate_list, building_coordinate_list, location_coordinate_list
from functions import number_loop, area_loop, building_loop, location_loop, number_coordinate_create, area_coordinate_create, building_coordinate_create, location_coordinate_create, number_input, area_input, building_input, location_input
from variables import scope, credentials, worksheet, client


print("Welcome to the google sheet automation program, to begin automating, press YES")
first_choice = raw_input('')

if first_choice == 'yes' or first_choice == 'YES':
    print("What is the name of the sheet you would like to access?")
    sheet_name = raw_input('')
    worksheet = client.open(sheet_name).sheet1

    #split database loop and allocate each type to a certain list
    number_loop(database_list_of_lists, number_list)
    area_loop(database_list_of_lists, area_list)
    building_loop(database_list_of_lists, building_list)
    location_loop(database_list_of_lists, location_list)

    #create coordinates for input in google sheet
    number_coordinate_create(number_coordinate_list, number_list)
    area_coordinate_create(area_coordinate_list, area_list)
    building_coordinate_create(building_coordinate_list, building_list)
    location_coordinate_create(location_coordinate_list, location_list)

    #input data from seperate lists into google sheet using coordinates
    number_input(number_list, number_coordinate_list)
    area_input(area_list, area_coordinate_list)
    building_input(building_list, building_coordinate_list)
    location_input(location_list, location_coordinate_list)