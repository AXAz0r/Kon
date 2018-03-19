import json
import discord
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("RD Clans Banned list").get_worksheet(0)

# Extract and print all of the values
sheet_list = sheet.col_values(1)


with open('config.json') as json_data_file:
    cfg = json.load(json_data_file)


def owner_check(message):
    return f'{message.author.id}' in cfg["OwnerID"]


def server_check(message):
    return f'{message.guild.id}' in cfg["Servers"]


def private_check(message):
    return isinstance(message.channel, discord.abc.PrivateChannel)


def ban_check(message):
    sheet_lower = [x.lower() for x in sheet_list]
    if message.mentions:
        mention_name = message.mentions[0].name
        mention_nick = message.mentions[0].display_name
        if mention_name.lower() in sheet_lower:
            return True
        elif mention_nick.lower() in sheet_lower:
            return True
    name = message.content.partition(' ')[0]
    return name.lower() in sheet_lower


def role_check(message):
    if message.mentions:
        if message.channel.id == xxxxxxxxxxxxxxxxxx:
            role = xxxxxxxxxxxxxxxxxxx
        else:
            role = False
        return role
            
           
def member_check(message):
    clan_roles = [xxxxxxxxxxxxxxxxxx]
    user_roles = [y.id for y in message.mentions[0].roles]
    has_role = False
    for role in clan_roles:
        if role in user_roles:
            has_role = True
            break
    return has_role


def kon_auth(auth_data, cmd_auth: str):
    auth_str = auth_data.get('auth')
    if auth_str is None:
        auth_str = []
    auth_str.clear()
    auth_data.update({'auth': [cmd_auth]})
    with open('permissions/kon_auth.json', 'w', encoding='utf-8') as auth_file:
        json.dump(auth_data, auth_file)

