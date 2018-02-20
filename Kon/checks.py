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
    return message.author.id in cfg["OwnerID"]


def server_check(message):
    return message.guild.id in cfg["Servers"]


def private_check(ctx):
    return isinstance(ctx.channel, discord.abc.PrivateChannel)


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
    triggers = ['reddit', 'recruitment', 'xxxxxxxxxxxxxxxxxx']
    if message.mentions:
        for trigger in triggers:
            if trigger in message.content.lower():
                if message.channel.id == xxxxxxxxxxxxxxxxxx:
                    role = "Smore"
                else:
                    role = False
                return role
            
           
def member_check(message):
    clan_roles = [xxxxxxxxxxxxxxxxxx]
    user_roles = [y.id for y in message.author.roles]
    has_role = False
    for role in clan_roles:
        if role in user_roles:
            has_role = True
            break
    return has_role
