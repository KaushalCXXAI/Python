"""
Exercise Description
    Write an isValidDate() function with parameters year, month, and day. The function
should return True if the integers provided for these parameters represent a valid date. Otherwise,
the function returns False. Months are represented by the integers 1 (for January) to 12 (for
December) and days are represented by integers 1 up to 28, 29, 30, or 31 depending on the month
and year. Your solution should import your leapyear.py program from Exercise #20 for its
isLeapYear() function, as February 29th is a valid date on leap years.
September, April, June, and November have 30 days. The rest have 31, except February which
has 28 days. On leap years, February has 29 days.
These Python assert statements stop the program if their condition is False. Copy them to
the bottom of your solution program. Your solution is correct if the following assert statements'
conditions are all True:
assert isValidDate(1999, 12, 31) == True
assert isValidDate(2000, 2, 29) == True
assert isValidDate(2001, 2, 29) == False
assert isValidDate(2029, 13, 1) == False
assert isValidDate(1000000, 1, 1) == True
assert isValidDate(2015, 4, 31) == False
assert isValidDate(1970, 5, 99) == False
assert isValidDate(1981, 0, 3) == False
assert isValidDate(1666, 4, 0) == False

import datetime
d = datetime.date(1970, 1, 1)
oneDay = datetime.timedelta(days=1)
for i in range(1000000):
    assert isValidDate(d.year, d.month, d.day) == True
    d += oneDay
"""

from EX20_Leap_Year import isLeapYear
def isValidDate(year, month, day):

    if 0 < day <= 31 and 0 < month <= 12:
        if day == 29 and month == 2:
            if isLeapYear(year):
                return True
            else:
                return False

        if day == 30:
            if month in [9,4,6,11] and not month == 2:
                return True
            elif month in [1,3,5,7,8,10,12] and not month == 2:
                return True
            else:
                return False

        if day == 31:
            if month in [1,3,5,7,8,10,12] and not month == 2:
                return True
            else:
                return False

        return True
    else:
        return False

#=================================================================================================
# The Below version is given by chat gpt which is again way better then my (mine's probably shit )
#=================================================================================================


# from EX20_Leap_Year import isLeapYear

# def isValidDate(year, month, day):
#     if month < 1 or month > 12:
#         return False
#     if day < 1:
#         return False

#     # Days in each month
#     if month == 2:
#         if isLeapYear(year):
#             return day <= 29
#         else:
#             return day <= 28
#     elif month in [4,6,9,11]:
#         return day <= 30
#     else:
#         return day <= 31


assert isValidDate(1999, 12, 31) == True
assert isValidDate(2000, 2, 29) == True
assert isValidDate(2001, 2, 29) == False
assert isValidDate(2029, 13, 1) == False
assert isValidDate(1000000, 1, 1) == True
assert isValidDate(2015, 4, 31) == False
assert isValidDate(1970, 5, 99) == False
assert isValidDate(1981, 0, 3) == False
assert isValidDate(1666, 4, 0) == False

import datetime
d = datetime.date(1970, 1, 1)
oneDay = datetime.timedelta(days=1)
for i in range(1000000):
    assert isValidDate(d.year, d.month, d.day) == True
    d += oneDay