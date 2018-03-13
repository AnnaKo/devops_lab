# !/usr/bin/python
"""python script"""
# pylint: disable=invalid-name

YEAR = int(input("Type in the year number: "))
"""type in year number"""

def leap_year(YEAR):
    """calculating leap years function"""
    # if YEAR <= 1900:
        # print "Sorry, the year must be greater than 1900. Try again"
    # elif YEAR >= 10 ** 5:
        # print "Sorry, the year must be less than 10000. Try again"
    if YEAR % 4 != 0:
        leap_year = False
    elif YEAR % 100 == 0:
        if YEAR % 400 == 0:
            leap_year = True
        else:
            leap_year = False
    else:
        leap_year = True
    return leap_year


if leap_year(YEAR) is False:
    print(leap_year(YEAR))
    print(" is NOT a leap year")
else:
    print(leap_year(YEAR))
    print(" IS a leap year")
