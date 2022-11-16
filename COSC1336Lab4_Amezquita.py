###############################################################################################
# Amber Amezquita
# Lab 4
# This lab creates a table of contact information(Name, Age, Season born, leap year ) and asks
# for user input to create the current age for contact.
###############################################################################################

def main():
    # zzz EXCEPTION HANDLING
    current_date = input("Enter today's date(mm/dd/yyyy): ", )
    print()

    try:
        contact_info = open('contactsLab4.txt', 'r')   # Import file
    except:
        print("Cannot open file.  Exiting")
        exit()
    names = []       # Create list objects names, birthdates
    birthdates = []
    i = 1
    for line in contact_info:
        # print(i, line)
        if i % 2 == 0:  # if even, then it correlates to Birth Dates in file
            birthdates.append(line.rstrip('\n'))  # r.strip only works with STR. Not lists.
        else:  # if odd, it correlates to Names in file
            names.append(line.rstrip('\n'))
        i += 1

    i = 0
    total_age=0
    for birthdate in birthdates:
        total_age += get_age(current_date, birthdate)
        i+=1
    average_age = total_age / len(birthdates)
    print(f'The average age is {str(average_age).split(".")[0]}')

    print(format('Names List', '25'), 'Birthdates List')
    # print(birthdates[1])   # index of 1
    for i in range (0, len(birthdates)):   # i is now the index. 0 to length of birthdays
        # age = get_age(birthdates[i])
        print(format(names[i],'25') + ' ' + birthdates[i] ) # printing every name

    # zzz print('Average age: ')
    # print('Average Age: ',(get_age(current_date))_
    print()
    # Outputs to screen Names and Contacts
    display_contacts(names, birthdates, current_date)




#####################################################################################
# Function name: find_season
# Input: birthdate
# Output: season
# Purpose: compares birth_month to id season
#####################################################################################
def find_season(birthdate):  # input birthdate/ return season
    # recieves a string
    birthday_split = birthdate.split('/')
    b_month = int(birthday_split[0])
    if b_month <= 2 or b_month == 12:
        season = 'Winter'
    if b_month >= 3 and b_month <= 5:
        season = 'Spring'
    if b_month >= 6 and b_month <= 8:
        season = 'Summer'
    if b_month >= 9 and b_month <= 11:
        season = 'Fall'
    return season


######################################################################
# Function name: is_leap_year
# Input: takes birth_year fx value
# Output: t/f
# Purpose: To determine if the year is a leap or not leap year
######################################################################
def is_leap_year(birthdate):  # return boolean value/T=Leap F=Not Leap
    birthday_split = birthdate.split('/')
    year = int(birthday_split[2])
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
# Input: uses parameters: current_date, birthdate
# Output: Age
# Purpose: Calculates age in correlation to current year
#########################################################################
def get_age(current_date, birthdate):
    todays_date = current_date.split('/')  # [11],[12],[2022]
    t_year = int(todays_date[2])
    t_month = int(todays_date[0])
    t_day = int(todays_date[1])
    birthday_split = birthdate.split('/')
    b_year = int(birthday_split[2])
    b_month = int(birthday_split[0])
    b_day = int(birthday_split[1])

    # Calculate if today's date is past their birthdate date.  A = Age
    # If today's day is smaller than the birth's day, subtract 1 from month
    a_day = t_day - b_day
    if a_day < 0:
        t_month -= 1

    # If today's month is smaller than the birth's month, subtract 1 from year
    a_month = t_month - b_month
    if a_month < 0:
        t_year -= 1

    # Now that I've calculated that their birth date has/hasn't past, subtract years
    a_year = t_year - b_year

    return a_year


########################################################################
# Function name: display_contacts
# Input:
# Output:
# Purpose:
#########################################################################
def display_contacts(names, birthdates, current_date):
    # Titles of lists (name, age, season, leap year)
    print(format('Name', '25'),format('Age','7'),format('Season','12'),('Leap Year?'))

    # Print entries
    for i in range(0, len(birthdates)):  # i is now the index. 0 to length of birthdays
        # age = get_age(birthdates[i])
        current_age = get_age(current_date, birthdates[i])
        season_str = find_season(birthdates[i])
        year_boo = is_leap_year(birthdates[i])
        if year_boo == True:
            year_str = 'Yes'
        else:
            year_str = 'No'


        print(format(names[i], '25'), format(current_age,'7'),format(season_str,'12'), year_str)




main()