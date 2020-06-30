import gspread as gc
from oauth2client.service_account import ServiceAccountCredentials
import numpy as np
import pandas as pd
import pprint
from lists import database_list_of_lists, dont_print, python_list

#all verifications and sheet/txt file opening:
scope = ["https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
pp = pprint.PrettyPrinter()

#client_email= fareswmansi@beebloot-mastersheet.iam.gserviceaccount.com
client = gc.authorize(credentials)

print("Welcome to the google sheets automation program, to begin automating data transfer, enter yes")
start_point = raw_input("")

if start_point == 'yes':
    print("Please enter the worksheet name that you wish to access.")
    what_sheet = raw_input("")

    #value list of number column:
    worksheet = client.open(what_sheet).sheet1
    value_list = worksheet.col_values(7)
    matched_strings = []
    find_this = []

    cell = worksheet.cell(1, 2, value_render_option='FORMULA').value
    print(cell)

    #start of userinterface
    print("What sheet number within the worksheet would you like to access?")
    what_sheet = raw_input("")

    if what_sheet == '1':

        print("To input new data from database, press 1. To view data within google spread sheet, press 2.")
        last_choice = raw_input("")

        if last_choice == '1':
            print("code is running...")

            #loop through database values and gspread values to find similariteis and input into string
            for list in database_list_of_lists:
                for phone_number in list:
                    if phone_number in value_list:
                        if phone_number not in matched_strings:
                            matched_strings.append(phone_number)

            print(matched_strings)

            #loop through database values and gspread values to find similariteis and input into string
            for list in database_list_of_lists:
                for phone_number in list:
                    for number in value_list:
                            if phone_number == number:
                                matched_strings.append(number)

            #use similarity to find row and column of string in gspread
            print(matched_strings)
            i = 0
            for i in range(len(matched_strings)):
                i += 1
                while i < len(matched_strings):
                        add_this = worksheet.findall(matched_strings[i])
                        break
            find_this.append(add_this)
            print(find_this)

        elif last_choice == '2':
            print("Data within batching sheet: ")
            sheet = client.open('testme2').sheet1

            #retrieve data from google spreadsheet1
            list_of_lists = sheet.get_all_values()
        
            check_length = len(list_of_lists)

            #while loop to remove data from all values and put necessary data within python list
            i = 0
            while i < check_length:
                i += 1
                if list_of_lists[i] != dont_print:
                    insert_this = list_of_lists[i]

                    #inserting google sheet data into python list
                    python_list = insert_this.copy()
                    print("Data within the sheet: ")
                    pp.pprint(python_list)

                    #begin finding data and inputting it into string
                else:
                    break

