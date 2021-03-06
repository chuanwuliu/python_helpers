"""
Time Classes
"""
import time as _time

class Date(object):
    """ Date class defined by year and month."""

    def __init__(self, year=2000, month=1):
        assert isinstance(year, int) and isinstance(month, int)
        self._year = year
        self._month = month

    def __repr__(self):
        return "%s.%s(%d, %d)" % (self.__class__.__module__,
                                  self.__class__.__qualname__,
                                  self._year,
                                  self._month)

    def __str__(self):
        return "%04d-%02d" % (self._year, self._month)

    def __hash__(self):
        return hash((self._year, self._month))

    def __eq__(self, other):
        return self._cmp(other) == 0

    def __lt__(self, other):
        return self._cmp(other) < 0

    def __le__(self, other):
        return self._cmp(other) <= 0

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __add__(self, other):
        if isinstance(other, Duration):
            return self.__class__(self._year + (self._month + other.months - 1) // 12,
                        (self._month + other.months - 1) % 12 + 1)
        else:
            raise NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Duration):
            return self.__add__(-other)
        elif isinstance(other, self.__class__):
            return Duration(12 * (self._year - other._year) + self._month - other._month)

    def _cmp(self, other):
        if isinstance(other, self.__class__):
            return _cmp(self._getstate(), other._getstate())
        else:
            raise _cmperror(self, other)

    def _getstate(self):
        return (self._year, self._month)

    @property
    def year(self):
        return self._year

    @property
    def month(self):
        return self._month

    def now(self):
        y, m = _time.localtime()[:2]
        return self.__class__(y, m)

    def today(self):
        return self.now()

    def is_leap_year(self):
        return _is_leap_year(self._year)

    def days_of_year(self):
        return 366 if self.is_leap_year() else 365

    def days_of_month(self):
        return _days_in_month(self._month, self._year)

    def next_tax_date(self):
        return self.__class__(self._year + self._month // 7, 7)


class Duration():
    """Time Duration in units of months."""

    def __init__(self, months=0, years=0):
        assert isinstance(months, int) and isinstance(years, int)
        self._months = months + 12 * years

    def __bool__(self):
        return self.months != 0

    def __repr__(self):
        return "%s.%s(%d)" % (self.__class__.__module__,
                                  self.__class__.__qualname__,
                                  self._months)

    def __hash__(self):
        return hash(self._months)

    def __pos__(self):
        return self

    def __neg__(self):
        return self.__class__(-self._months)

    def __eq__(self, other):
        return self._cmp(other) == 0

    def __lt__(self, other):
        return self._cmp(other) < 0

    def __le__(self, other):
        return self._cmp(other) <= 0

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self._months + other._months)
        else:
            raise NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return self.__add__(-other)

    def __mul__(self, other):
        assert isinstance(other, int)
        return self.__class__(self._months * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, Duration):
            return self.months / other.months
        elif isinstance(other, int) and not self.months % other:
            return self.__class__(self.months % other)
        else:
            raise NotImplemented

    def _cmp(self, other):
        if isinstance(other, Duration):
            return _cmp(self._getstate(), other._getstate())
        else:
            raise _cmperror(self, other)

    def _getstate(self):
        return self._months

    @property
    def months(self):
        return self._months


def _cmp(x, y):
    return 0 if x == y else 1 if x > y else -1


def _cmperror(x, y):
    raise TypeError("can't compare '%s' to '%s'" % (
        type(x).__name__, type(y).__name__))


def _is_leap_year(year):
    """
    Return True if a year is leap year else False.
    """
    if year % 4:
        return False
    elif year % 100:
        return True
    elif year % 400:
        return False
    else:
        return True


_DAYS_IN_MONTH = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def _days_in_month(month, year):
    """
    Days of that month of that year.
    """
    if month != 2:
        return _DAYS_IN_MONTH[month - 1]
    elif _is_leap_year(year):
        return 29
    else:
        return 28