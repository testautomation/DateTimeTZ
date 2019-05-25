# -*- coding: utf-8 -*-
# Copyright (c) 2014 Roman Merkushin / rmerkushin@ya.ru
# Update 2019 by Tset Noitamotua



import time
from datetime import datetime
from dateutil.parser import parse
from babel.dates import format_datetime
from dateutil.relativedelta import relativedelta

__version__ = "v1.0.0"

class DateTimeTZ:

    """
    Robot Framework [https://github.com/testautomation/DateTimeTZ|DateTimeTZ] library provides functionality for manipulating date and time in different locales and time zones.\n
    DateTime library is based on [http://babel.pocoo.org|Babel] and [http://labix.org/python-dateutil|python-dateutil].
    """

    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def wait(self, seconds):
        """
        Suspends test execution for the given number of seconds.\n
        *Example usage:*
        | *Keyword* | *Argument* |
        | Wait | 5 |
        """
        print "Suspend test execution on " + str(seconds) + " seconds."
        time.sleep(int(seconds))

    def get_unix_time(self):
        """
        Returns current Unix time.\n
        *Example usage:*
        | *Variable* | *Keyword* |
        | ${unix_time} | Get Unix Time |
        *Example result:*\n
        INFO : ${unix_time} = 1394694526.94
        """
        return time.time()

    def get_timestamp(self, locale="en", time_format="dd-LL-y H:mm:ss.A", *args, **delta):
        """
        Returns current local timestamp in defined format and locale.\n
        _"locale"_ argument allows to set timestamp languages such as the ISO country and language codes.\n
        _"time_format"_ argument allows to set timestamp pattern for representation as described below.\n
        *Date format:*
        | *Field* | *Symbol* | *Description* |
        | Era | G | Replaced with the era string for the current date. One to three letters for the abbreviated form, four letters for the long form, five for the narrow form. |
        | Year | y | Replaced by the year. Normally the length specifies the padding, but for two letters it also specifies the maximum length. |
        | | Y | Same as y but uses the ISO year-week calendar. |
        | Quarter | Q | Use one or two for the numerical quarter, three for the abbreviation, or four for the full name. |
        | | q | Use one or two for the numerical quarter, three for the abbreviation, or four for the full name. |
        | Month | M | Use one or two for the numerical month, three for the abbreviation, or four for the full name, or five for the narrow name. |
        | | L | Use one or two for the numerical month, three for the abbreviation, or four for the full name, or 5 for the narrow name. |
        | Week | w | Week of year. |
        | | W | Week of month. |
        | Day | d | Day of month. |
        | | D | Day of year. |
        | | F | Day of week in month. |
        | Week day | E | Day of week. Use one through three letters for the short day, or four for the full name, or five for the narrow name. |
        | | e | Local day of week. Same as E except adds a numeric value that will depend on the local starting day of the week, using one or two letters. |
        *Time format:*\n
        | *Field* | *Symbol* | *Description* |
        | Period | a | AM or PM. |
        | Hour | h | Hour [1-12]. |
        | | H | Hour [0-23]. |
        | | K | Hour [0-11]. |
        | | k | Hour [1-24]. |
        | Minute | m | Use one or two for zero places padding. |
        | Second | s | Use one or two for zero places padding. |
        | | S | Fractional second, rounds to the count of letters. |
        | | A | Milliseconds in day. |
        | Timezone | z | Use one to three letters for the short timezone or four for the full name. |
        | | Z | Use one to three letters for RFC 822, four letters for GMT format. |
        | | v | Use one letter for short wall (generic) time, four for long wall time. |
        | | V | Same as z, except that timezone abbreviations should be used regardless of whether they are in common use by the locale. |
        _"delta"_ argument allows to set timestamp delta (minus or plus). It allows take one or multiple parameters such as: years, months, weeks, days, hours, minutes, seconds, microseconds.\n
        _"delta"_ also allows to set specific timestamp parts (year, month, day, hour, minute, second, microsecond).\n
        *Example usage:*
        | *Variable* | *Keyword* | *Argument* | *Argument* | *Argument* | *Argument* |
        | ${timestamp} | Get Timestamp | locale=rus | time_format=dd LLL y H:mm:ss |
        | ${timestamp_with_delta} | Get Timestamp | locale=rus | time_format=LLL y H:mm | months=-2 |
        | ${timestamp_with_delta} | Get Timestamp | locale=rus | time_format=LLL y H:mm | months=-2 | year=2012 |
        *Example result:*\n
        INFO : ${timestamp} = 13 Март 2014 17:54:57\n
        INFO : ${timestamp_with_delta} = Янв. 2014 17:54\n
        INFO : ${delta_and_cpecific_part} = Янв. 2012 17:54
        """
        delta = dict((key, int(value)) for (key, value) in delta.items())
        timestamp = datetime.today() + relativedelta(**delta)
        return format_datetime(timestamp, time_format, locale=locale)

    def get_utc_timestamp(self, locale="en", time_format="dd-LL-y H:mm:ss.A", *args, **delta):
        """
        Returns current UTC timestamp in defined format and locale.\n
        *Get Utc Timestamp* keyword arguments are the same as *`Get Timestamp`* arguments.\n
        *Example usage:*\n
        | *Variable* | *Keyword* | *Argument* | *Argument* |
        | ${utc_timestamp} | Get Utc Timestamp | locale=rus | time_format=dd LLL y H:mm:ss |
        *Example result:*\n
        INFO : ${utc_timestamp} = 13 Март 2014 11:32:58
        """
        delta = dict((key, int(value)) for (key, value) in delta.items())
        timestamp = datetime.utcnow() + relativedelta(**delta)
        return format_datetime(timestamp, time_format, locale=locale)

    def convert_timestamp_format(self, timestamp, time_format, locale="en"):
        """
        Converts timestamp from one format to another.\n
        *Warning!* This keyword support only numeric or string with English locale words timestamps.\n
        _"time_format"_ and _"locale"_ arguments are the same as *`Get Timestamp`* arguments.\n
        *Example usage:*\n
        | *Variable* | *Keyword* | *Argument* | *Argument* |
        | ${timestamp} | Get Timestamp |
        | ${rus_timestamp} | Convert Timestamp Format | time_format=dd LLL y H:mm:ss | locale=rus |
        *Example result:*\n
        INFO : ${timestamp} = 13-03-2014 18:38:07.67087810\n
        INFO : ${rus_timestamp} = 13 Март 2014 18:38:07
        """
        timestamp = parse(timestamp)
        return format_datetime(timestamp, time_format, locale=locale)
