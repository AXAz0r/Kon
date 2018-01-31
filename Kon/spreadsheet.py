import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet_one = client.open("doc_name").get_worksheet(0)

# Extract and print all of the values
sheet_one_list = sheet_one.col_values(1)


def ban_check(message):
    sheet_one_lower = [x.lower() for x in sheet_one_list]
    message = message.content.partition(' ')[0]
    return message.lower() in sheet_one_lower:
