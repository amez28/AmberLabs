def main ():   # Will display the message
    user_Name = input("Enter your name: ")
    birth_Month = int(input("Enter the number associated with your " \
                            + "birth month(must be an integer): "))
    get_month(birth_Month)
    birth_Year = int(input('Enter the year you were born: '))

    get_year(birth_Year)

    find_season(birth_Month)



    # print(f"Hello, {user_Name}! You were born in the {season} and {birth_Year} was {leap}a " \
    #       + "leap year.")
    # print()
    # another = input('Enter another name to begin again' + \
    #                 ' or type "zzz" to quit?: ')



def get_month(month):   # ask the user for birth month/validate
    # birth_Month = int(input("Enter the number associated with your " \
    #                         + "birth month(must be an integer): "))
    while month < 1 or month > 12:
        print('Error: The input is invalid.')
        month = int(input("Enter the correct " +
                                "integer: "))
        # zzz add another input validation for 0
    while month <= 0:
        print('Error: The input is invalid.')
        month = int(input('Enter the correct' +
                                'integer: '))
        return month


def get_year(year):  # birth year/validate/ >0
    # birth_Year = int(input('Enter the year you were born: '))
    while year < 0:
        print('Error: The input is invalid.')
        year = int(input('Enter the correct integer: '))
        return year

def find_season(month):  # input month/ return season
    if month <= 2 or month == 12:
        season = 'Winter'
    if month >= 3 and month <= 5:
        season = 'Spring'
    if month >= 6 and month <=8:
        season = 'Summer'
    if month >= 9 and month <= 11:
        season = 'Fall'
#
# def is_leap_year():  # return boolean value/T=Leap F=Not Leap


main()