"""
Date helper functions
"""

def is_leap_year(year):
    """
    If a year is a leap year.
    Args:
        year: year number.
    Return:
        Boolean: True if a year is leap year.
    """
    if year % 4:
        return False
    elif year % 100:
        return True
    elif year % 400:
        return False
    else:
        return True


def days_in_year(year):
    """
    Return the number of days in a year.
    Args:
        year: year number
    Return:
        number of days this year.
    """
    if is_leap_year(year):
        days = 366
    else:
        days = 365
    return days


def days_in_month(month, year=None):
    """
    Number of days in the month
    Algorithm:
        if month is not February:
            Right shift the sequence 5546 (0b1010110101010) by month, get the
            right-most digit and plus 30. This is equivalent to
            [31, 30, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month]
        elif not a leap year:
            28 days
        else:
            29 days
    Args:
        month: month number.
        year: year number.
    Returns:
        number of days in the month.
    """
    if month != 2:
        days = 30 + (5546 >> month & 1)
    elif is_leap_year(year):
        days = 29
    else:
        days = 28
    return days

