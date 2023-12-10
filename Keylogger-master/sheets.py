import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Keylog Data").sheet1
while (1):
	row = input("Enter text:").split()
	index = 1
	sheet.insert_row(row, index)

# Extract and print all of the values
list_of_hashes = sheet.get_all_records()
print(list_of_hashes)