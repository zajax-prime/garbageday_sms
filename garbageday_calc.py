# thanks MyTecbits and ugoren on stackoverflow
# https://www.mytecbits.com/internet/python/week-number-of-month
# https://stackoverflow.com/questions/8801084/how-to-calculate-next-friday

import datetime
import pandas as pd

#dirName = Path(__file__).parent
#print(dirName)

def load_config():

    # Opening JSON file
    with open('gd_config.json', 'r') as openfile:
        # Reading from json file - going with pandas
        #config = json.load(openfile)
        #i want to rewrite to turn any top level keys into seperate dataframes

        config_df = pd.read_json(openfile)
        #print(config.keys())
        #for key in config:

        tenants_df = pd.json_normalize(config_df["tenants"])

        return(tenants_df)

def week_number_of_month(date_value):
     return (date_value.isocalendar()[1] - date_value.replace(day=1).isocalendar()[1] + 1)

def find_trash_person(sender_phone_number):

    #load tenants from the config json
    tenants_df = load_config()

    #today = datetime.datetime.today().date()
    today = datetime.datetime(year=2022, month=7, day=9).date()
    friday = today + datetime.timedelta( (4-today.weekday()) % 7 )
    week_of_month = week_number_of_month(friday)
    print("\nWeek number of month: ",week_of_month, "\n")

    #given the week/apt number, return a series of phone numbers that have trash week
    matching_phone_numbers = tenants_df.loc[tenants_df['aptNum'] == week_of_month].phoneNumber

    sender_phone_number = '+19723459836'

    #Evaluate if it's the sender's trash week by seeing if the Apt's Phone Numbers == Sender's Phone Number
    #There is definitely a more readable way to do this
    #https://stackoverflow.com/questions/21319929/how-to-determine-whether-a-pandas-column-contains-a-particular-value
    #Creates a boolean series, which is then evaluated if it has any true values, if none then TRUE
    #But then reversed with NOT to make it return whether there was a match or not
    sender_trash_person_status = not matching_phone_numbers[matching_phone_numbers.isin([sender_phone_number])].empty
    #Package easy to reference dictionary as return value
    trash_stats = dict()
    trash_stats['sender_trash_person_status'] = sender_trash_person_status
    trash_stats['week_of_month'] = week_of_month
    return (trash_stats)

 