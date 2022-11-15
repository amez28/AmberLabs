###################################################################
# Amber Amezquita
# Lab 4
#
# Use parallel lists. List(bday) List(name)
# Read Contacts, add to lists. contactsLab4.txt.append()
# Display avg. age
# names_list = ['Henry Bemis','Penthor Mul']
# birth_list = ['8/4/2008','5/3/1928']

def main():

    contact_info = open('contactsLab4.txt','r')
    print()
    print(format('Name','25'), 'Birth Date')
    name = contact_info.readline()
    while name != '':
        birth_date = contact_info.readline().rstrip('\n')
        name = name.rstrip('\n')
        print(format(name,'25'), birth_date)
        name = contact_info.readline()

    contact_info.close()
###############################################
# Function name: find_season
# Input: birth_month value
# Output: season
# Purpose: compares birth_month to id season
###############################################
def find_season(month):  # input month/ return season
    if month <= 2 or month == 12:
        season = 'Winter'
    if month >= 3 and month <= 5:
        season = 'Spring'
    if month >= 6 and month <=8:
        season = 'Summer'
    if month >= 9 and month <= 11:
        season = 'Fall'
    return season
######################################################################
# Function name: is_leap_year
# Input: takes birth_year fx value
# Output: t/f
# Purpose: To determine if the year is a leap or not leap year
######################################################################
def is_leap_year(year):  # return boolean value/T=Leap F=Not Leap
    leap = True
    if year % 4 == 0:
        if year % 400 == 0:
            leap = True
        elif year % 100 == 0:
            leap = False
    else:
        leap = False
    return leap
########################################################################
# Function name: get_age
# Input:
# Output:
# Purpose:
#########################################################################
def get_age():
    current_date = input("Enter today's date(mm/dd/yyyy): ", )
########################################################################
# Function name: display_friends
# Input:
# Output:
# Purpose:
#########################################################################
def display_friends():
    # open file
    contact_info = open('contactsLab4.txt','r')
    # Column Headings
    print()
    print(format('Name','25'),'Birth Year')
    # Read first name in file
    name = contact_info.readline()
    while name != '':  # Checking for End of file
        birth_year = contact_info.readline().rstrip('\n')
        name = name.rstrip('\n')
        print(format(name,'25'), birth_year)
        name = contact_info.readline()
    contact_info.close()
main()