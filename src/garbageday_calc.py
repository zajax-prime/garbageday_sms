import datetime
import pandas as pd

def load_config():

    # Opening JSON file
    with open('gd_config.json', 'r') as openfile:

        # Preferably I would like to rewrite this to turn any top level keys into seperate dataframes
        # Would allow multiple key configs
        config_df = pd.read_json(openfile)

        tenants_df = pd.json_normalize(config_df["tenants"])

        return(tenants_df)


# Thanks to MyTecbits and ugoren on stackoverflow for the calculation for week-number-of-month related functions
# https://www.mytecbits.com/internet/python/week-number-of-month
# https://stackoverflow.com/questions/8801084/how-to-calculate-next-friday
def week_number_of_month(date_value):
     return (date_value.isocalendar()[1] - date_value.replace(day=1).isocalendar()[1] + 1)


def find_trash_person(requester_phone_number):

    # Initialize function results in a dictionary
    trash_stats = dict()

    # Load tenants from the config json
    tenants_df = load_config()

    # Evaluate if requester a tenant by comparing requester phone number, return a bool
    trash_stats['requester_is_tenant'] = requester_phone_number in tenants_df.phoneNumber.values


    # If the requester is an actual tenant, calculate whos garbage week it is and add to the trash_stats dict
    # else return null values in trash_stats dict
    if trash_stats['requester_is_tenant']:
        
        # Lookup first name based off of phone number
        trash_stats['requester_name'] = tenants_df.loc[tenants_df['phoneNumber'] == requester_phone_number].firstName.values[0]

        #Calculate what week of the month the next friday falls on
        today = datetime.datetime.today().date()
        friday = today + datetime.timedelta( (4-today.weekday()) % 7 )
        trash_stats['week_of_month'] = week_number_of_month(friday)

        # Given the week/apt number, return a series of phone numbers that have trash week
        matching_phone_numbers = tenants_df.loc[tenants_df['aptNum'] == trash_stats['week_of_month']].phoneNumber

        # Evaluate if it's the requester's trash week by seeing if the Apt's Phone Numbers == requester's Phone Number
        # There is definitely a more readable way to do this
        # https://stackoverflow.com/questions/21319929/how-to-determine-whether-a-pandas-column-contains-a-particular-value
        # Creates a boolean series, which is then evaluated if it has any true values, if none then TRUE
        # But then reversed with NOT to make it return whether there was a match or not
        trash_stats['requester_trash_person_status'] = not matching_phone_numbers[matching_phone_numbers.isin([requester_phone_number])].empty

    else:
        trash_stats['week_of_month'] = None
        trash_stats['requester_trash_person_status'] = None
        trash_stats['requester_name'] = None

    return (trash_stats)
#debug
#find_trash_person('+19723459836')