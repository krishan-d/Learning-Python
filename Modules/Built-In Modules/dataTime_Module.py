"""
datetime module:
"""

import time as t
import datetime as dt
from datetime import date, time, datetime, timezone, timedelta
import pytz as pytz


# Constants:
print("Year allowed in date or datetime object:")
print(dt.MAXYEAR, "|", dt.MINYEAR)

"""
Types(class):
datetime.date:
    datetime.date(year, month, day)

datetime.time:
    datetime.time(hour, minute, second, microsecond, tzinfo)

datetime.datetime:
    datetime.datetime(year_number, month_number, day_number, hours, minutes, seconds, microsecond, tzinfo)

datetime.timedelta:
    A duration expressing the difference between two date, time, or datetime instances to microsecond resolution.

datetime.tzinfo:
    An abstract base class for time zone information objects.
    These are used by the datetime and time classes to provide a customizable notion of time adjustment.

datetime.timezone:
    A class that implements the tzinfo abstract base class as a fixed offset from the UTC.


Properties:: date, datetime, time, and timezone:
    Immutable : Each operation produce a new object.
    hashable, means can be used as dictionary keys.
    support pickling via pickle module.


Aware or Naive:
    date - Naive.
    datetime object d is aware if:
        d.tzinfo is not None
        d.tzinfo.utcoffset(d) does not return None.
    time object t is aware if:
        t.tzinfo is not None
        t.tzinfo.utcoffset(None) does not return None.
"""

# ---------------------------------------------------------
# timedelta Objects:
# represents a duration, the difference between two dates or times.

# datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
# Only days, seconds and microseconds are stored internally.

print("\nTimedelta object constructor:")
ob_Td = timedelta(days=50, seconds=27, microseconds=10, milliseconds=29000, minutes=5, hours=8, weeks=2)
print("Timedelta obj :", ob_Td)  # 64 days, 8:05:56.000010

Td = timedelta(microseconds=-1)
print("Days:", Td.days, "Seconds:", Td.seconds, "Microseconds:", Td.microseconds)  # -1 86399 999999

# str(t) : Returns a string in the form [D day[s], ][H]H:MM:SS[.UUUUUU], where D is negative for negative t.
print("str:", str(Td))  # -1 day, 23:59:59.999999

# repr(t) : Returns string representation of the timedelta object as a constructor call with canonical attribute values.
print("repr:", repr(Td))  # datetime.timedelta(days=-1, seconds=86399, microseconds=999999)

# days : -999999999 <= d <= 999999999
# seconds : 0 <= s <= 86399
# microseconds : 0 <= ms <= 999999

print("Timedelta min :", timedelta.min)
print("Timedelta max :", timedelta.max)
print("Timedelta least possible difference :", timedelta.resolution)


Td1 = timedelta(seconds=57)
Td2 = timedelta(hours=2, seconds=2)
print(Td2 != Td1)


Td3 = timedelta(days=365)
print("Total seconds :", Td3.total_seconds())
tenYears = 10 * Td3
print(repr(tenYears))
print(tenYears.days // 365)
nineYear = tenYears - Td3
print(repr(nineYear))


TimeGap = timedelta(hours=23, minutes=34)
print("Future Time :", str(datetime.now() + TimeGap))


# ---------------------------------------------------------
# date Object:
# datetime.date(year, month, day)

print("\nDate object constructor:")
ob_Date = date(2020, 10, 27)
print("Date obj :", ob_Date)

# classMethods:
# date.today():
dateToday = date.today()
print("Date Today :", dateToday, "| Equivalent To :", date.fromtimestamp(t.time()))

# date.fromtimestamp(timestamp):
# Return the local date corresponding to the POSIX timestamp, such as is returned by time.time().
print("From Timestamp :", date.fromtimestamp(t.time()))


# date.fromordinal(ordinal):
# Return the date corresponding to the proleptic Gregorian ordinal, where January 1 of year 1 has ordinal 1.
# ValueError is raised unless 1 <= ordinal <= date.max.toordinal().
# For any date d, date.fromordinal(d.toordinal()) == d.
print("From Ordinal :", date.fromordinal(730920))  # 730920th day after 1. 1. 0001  #-> 2002-03-11


# date.fromisoformat(date_string):
# date_string : Format YYYY-MM-DD.
# This is the inverse of date.isoformat().
print("From Iso Format :", date.fromisoformat('2020-12-03'))


# date.fromisocalendar(year, week, day):
# This is the inverse of the function date.isocalendar().
print("From iso Calendar :", date.fromisocalendar(2022, 20, 6))


# class attributes:
print("Date Min :", date.min)
print("Date Max :", date.max)
print("Date Resolution :", date.resolution)


# instance attributes:
# date.year
# date.day
# date.month


# instance methods:
# replace(self, year: int = ..., month: int = ..., day: int = ...) -> date: ...
dateObj = ob_Date.replace(day=dateToday.day)
print("Replace :", dateObj)


# Mon : 0 and Sun : 6.
print("Weekday :", dateToday.weekday())

# Mon : 1 and Sun : 7.
print("Iso Weekday :", dateToday.isoweekday())


# Methods related to formatting string output:
print(dateToday.isoformat())
print(dateToday.strftime("%d/%m/%Y"))
print(dateToday.strftime("%A %d. %B %Y"))
print(dateToday.ctime())


# methods for extracting 'components' under different calendars:
print("Date TimeTuple :")
dTup = dateToday.timetuple()
for i in dTup:
    print('\t', i)


print("Date Iso calendar :")
ic = dateToday.isocalendar()
for i in ic:
    print('\t', i)


# ---------------------------------------------------------
# datetime object:
# constructor:
# class datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
# MINYEAR <= year <= MAXYEAR,
# 1 <= month <= 12,
# 1 <= day <= number of days in the given month and year,
# 0 <= hour < 24,
# 0 <= minute < 60,
# 0 <= second < 60,
# 0 <= microsecond < 1000000,
# fold in [0, 1].
print("\nDatetime object constructors:")
datetimeObj = datetime(2020, 5, 17)
print("Datetime obj :", datetimeObj)


# other constructors:
# classMethod datetime.today()
# Return the current local datetime, with tzinfo None.
datetimeToday = datetime.today()
print("Datetime Today :", datetimeToday)

# classMethod datetime.now(tz=None)
# Return the current local date and time.
print("Datetime Now:", datetime.now())


UTC = pytz.utc
IST = pytz.timezone('Asia/Kolkata')
datetimeUTC = datetime.now(tz=UTC)
print("In UTC :", datetimeUTC.strftime('%Y:%m:%d %H:%M:%S %Z %z'))
datetimeIST = datetime.now(IST)
print("In IST :", datetimeIST.strftime('%Y:%m:%d %H:%M:%S %Z %z'))


# classMethod datetime.utcnow()
# Return the current UTC date and time, with tzinfo None.
print("UTC Now :", datetime.utcnow())

# classMethod datetime.fromtimestamp(timestamp, tz=None)
# Return the local date and time corresponding to the POSIX timestamp.
print("From Timestamp :", datetime.fromtimestamp(t.time(), UTC))

# classMethod datetime.utcfromtimestamp(timestamp)
# Return the UTC datetime corresponding to the POSIX timestamp, with tzinfo None.
print("UTC From Timestamp :", datetime.utcfromtimestamp(t.time()))

# classMethod datetime.fromordinal(ordinal)

# classMethod datetime.fromisoformat(date_string)
print("From Iso Format :", datetime.fromisoformat("2020-08-04"))

# classMethod datetime.combine(date, time, tzinfo)
print("Combine :", datetime.combine(date.today(), time(12, 30), tzinfo=IST))

# classMethod datetime.fromisocalendar(year, week, day)
print("From Iso Calendar :", datetime.fromisocalendar(2020, 20, 6))

# classMethod datetime.strptime(date_string, format):
# strptime(cls, date_string: str, format: str) -> datetime: ...
# Return a datetime corresponding to date_string, parsed according to format.
print(datetime.strptime('07/02/2022', '%d/%m/%Y'))


# Formatting datetime:
print(datetime.now().strftime('%d/%m/%Y'))


# class attributes:
print("Datetime Min :", datetime.min)
print("Datetime max :", datetime.max)
print("Datetime resolution :", datetime.resolution)


# instance attributes(read-only):
# datetime.year
# datetime.month
# datetime.day
# datetime.hour
# datetime.minute
# datetime.second
# datetime.microsecond
# datetime.tzinfo
# datetime.fold


# instance methods:
print("Datetime Date :", datetimeIST.date())


# datetime.time()
# Return time object with same hour, minute, second, microsecond and fold. tzinfo is None.
print("Datetime Time :", datetimeIST.time())


# datetime.timetz():
# Return time object with same hour, minute, second, microsecond, fold, and tzinfo attributes.
print("TimeTz :", datetimeUTC.timetz())


# datetime.astimezone(tz=None)
# Return a datetime object with new tzinfo attribute tz.
# To convert the time of a particular time zone into another time zone.
print("asTimezone :", datetimeIST.astimezone(UTC))


# datetime.utcoffset()
# If tzinfo is None, returns None, else returns self.tzinfo.utcoffset(self).
print("UTC offset :", datetimeIST.utcoffset())


# datetime.dst()
# If tzinfo is None, returns None.
print("Dst :", datetimeIST.dst())

print("Tzname :", datetimeIST.tzname())


# datetime.replace(year, month, day, hour, minute, second, microsecond, tzinfo, *, fold=0)
datetimeObj = datetimeObj.replace(day=10)
print("Replace :", datetimeObj)


print("Weekday :", datetimeIST.weekday())
print("Iso weekday :", datetimeIST.isoweekday())
print("Timestamp :", datetimeIST.timestamp())


# Methods related to formatting string output:
print("Iso Format :", datetimeIST.isoformat())
print(datetimeIST.strftime("%d/%m/%Y"))
print("cTime :", datetimeIST.ctime())


# Using datetime.timetuple() to get tuple of all attributes
print("Datetime TimeTuple attributes :")
datetimeTup = datetimeIST.timetuple()
for i in datetimeTup:
    print('\t', i)


# Date in ISO format:
print("Datetime Iso calendar :")
ic = datetimeIST.isocalendar()
for i in ic:
    print('\t', i)


# ---------------------------------------------------------
# time object:
# datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0):
print("\nTime object constructor:")

ob_Time = time(10, 29, 40)
print("Time obj :", ob_Time)

# classMethod:
iTime = time.fromisoformat("04:23:10.000047+04:00")
print("From Iso Format :", iTime)


# class attributes:
print("Time Max :", time.max)
print("Time Min :", time.min)
print("Time Resolution :", time.resolution)


# instance attributes:
# time.hour
# time.minute
# time.second
# time.microsecond
# time.tzinfo
# time.fold


# instance method:
new_Time = ob_Time.replace(hour=12, tzinfo=IST)
print("Time replace :", new_Time)

print("Time Formatting :", iTime.strftime("%H:%M:%S %Z"))
print("Dst :", iTime.dst())
print("Tzname :", iTime.tzname())


# ---------------------------------------------------------
# timezone object:
# datetime.timezone(offset, name=None)
# offset : timedelta object representing the difference between the local time & UTC.
# Between -timedelta(hours=24) and timedelta(hours=24), otherwise ValueError is raised.
print("\nTimezone object constructor:")

ob_Timezone = timezone(timedelta(hours=13), name='NewTz')
print("Timezone obj :", ob_Timezone)
print("Timezone UTC :", ob_Timezone.utc)

# timezone.utcoffset(dt) -> timedelta | None: ...
# Timedelta : difference between the local time and UTC.
print("UTC offset :", ob_Timezone.utcoffset(None))

# timezone.tzname(dt)
# Return the fixed value specified when the timezone instance is constructed.
print("Timezone name :", ob_Timezone.tzname(None))

# timezone.dst(dt)
# Always returns None.
print("Dst :", ob_Timezone.dst(None))


# strftime():
# Convert object to a string according to a given format.
# instance method.
# date, datetime, time
# shrftime(format)

# strptime():
# Parse a string into a datetime object given a corresponding format.
# class method.
# datetime
# strptime(date_string, format)

# %a	Weekday, short version	Wed
# %A	Weekday, full version	Wednesday
# %w	Weekday as a number 0-6, 0 is Sunday	3
# %d	Day of month 01-31	31
# %b	Month name, short version	Dec
# %B	Month name, full version	December
# %m	Month as a number 01-12	12
# %y	Year, short version, without century	18
# %Y	Year, full version	2018
# %H	Hour 00-23	17
# %I	Hour 00-12	05
# %p	AM/PM	PM
# %M	Minute 00-59	41
# %S	Second 00-59	08
# %f	Microsecond 000000-999999	548513
# %z	UTC offset	+0100
# %Z	Timezone	CST
# %j	Day number of year 001-366	365
# %U	Week number of year, Sunday as the first day of week, 00-53	52
# %W	Week number of year, Monday as the first day of week, 00-53	52
# %c	Local version of date and time	Mon Dec 31 17:41:00 2018
# %C	Century	20
# %x	Local version of date	12/31/18
# %X	Local version of time	17:41:00
# %%	A % character	%
# %G	ISO 8601 year	2018
# %u	ISO 8601 weekday (1-7)	1
# %V	ISO 8601 week number (01-53)	01
