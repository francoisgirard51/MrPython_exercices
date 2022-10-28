# Instructions
# Give a definition of the is_leap year function which, given a natural integer n,
# returns the boolean True if n is a leap year, False otherwise.
def is_a_leap_year(year : int) -> bool:
    """Preconditions: year is a positive integer
    returns True if it is a leap year (can be divided by 4, 100 et 400), False otherwise
    """
    return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0))

assert is_a_leap_year(2020) == True
assert is_a_leap_year(2000) == True
assert is_a_leap_year(1000) == False
assert is_a_leap_year(1918) == False

# Instructions:
# We now want to know which day of the week falls on any date, for example November 16, 2025.
# Give a definition of the day_of_the_week function which, given three integers corresponding
# respectively to the day, month and year, is greater than or equal to at 1900, returns the
# character string corresponding to the day of the week on which this date falls. Use for this
# the fact that the first of January 1900 fell on a Monday. It is also useful to introduce a
# list containing the number of days in each of the 12 months of the year, as well as a list
# containing the names of the days of the week. It is also useful to call the function of the
# previous question.
def day_of_the_week(day : int, month : int, year : int)-> str:
    """Preconditions: 1<= day <= 31, 1<= month <= 12, year >= 1900
    Days and months define an acceptable date
    """

    nb_days : int = 0
    nb_days_months : List[int] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    a: int
    for a in range(1900, year):
        nb_days = nb_days + 365
        if is_a_leap_year(a):
            nb_days = nb_days + 1
    m: int
    for m in range(0, month - 1):
        nb_days = nb_days + nb_days_months[m]
    if is_a_leap_year(year) and month > 2:
        nb_days = nb_days + 1
    nb_days = nb_days + day - 1
    list_days : List[str] = ['monday', 'tuesday', 'wednesday', 'thursday', \
                               'friday', 'saturday', 'sunday']
    return list_days[nb_days % 7]

assert day_of_the_week(1,1,2000) == 'saturday'
assert day_of_the_week(11,11,2021) == 'thursday'
assert day_of_the_week(11,11,1918) == 'monday'

# Instructions:
# We want to know in which years, since 1919, November 11 fell on a Sunday. Give a definition
# of the function sunday_november_11 without argument which returns the list of these years.
def Sunday_11_November()-> List[int]:
    """..."""
    L: List[int] = []
    year: int
    for year in range(1919, 2022):
        if day_of_the_week(11, 11, year) == 'dimanche':
            L.append(year)
    return L

# Other solution
# def Sunday_11_November()-> List[int]:
#    """"Préconditions: N/A
#    """
#    return [year for year in range(1919, 2022) \
#        if day_of_the_week(11, 11, year) == 'dimanche']
