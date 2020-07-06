import gspread as gc
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver

#all authentication
scope = ["https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
#client_email= fareswmansi@beebloot-mastersheet.iam.gserviceaccount.com
client = gc.authorize(credentials)
worksheet = client.open('testme3').sheet1

