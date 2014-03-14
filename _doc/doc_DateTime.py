# -*- coding: utf-8 -*-
# Copyright (c) 2014 Roman Merkushin
# rmerkushin@ya.ru

import time
from datetime import datetime
from dateutil.parser import parse
from babel.dates import format_datetime
from dateutil.relativedelta import relativedelta

__version__ = "v1.0.0"

class DateTime:

    """
    <p>The Robot Framework <a href="https://github.com/rmerkushin/uDateTime">DateTime</a> is a library which provides common functionality for manipulate date and time in different locales.<br>
    DateTime library is based on <a href="http://babel.pocoo.org/">Babel</a> and <a href="http://labix.org/python-dateutil">python-dateutil</a>.</p>
    """

    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def wait(self, seconds):
        """
        <p>Suspends test execution for the given number of seconds.</p>
        <p><b>Example usage:</b></p>
        <table>
            <thead>
                <tr>
                    <td><b>Keyword</b></td>
                    <td><b>Argument</b></td>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Wait</td>
                    <td>5</td>
                </tr>
            </tbody>
        </table>
        """
        print "Suspend test execution on " + str(seconds) + " seconds."
        time.sleep(int(seconds))

    def get_unix_time(self):
        """
        <p>Returns current Unix time.</p>
        <p><b>Example usage:</b></p>
        <table>
            <thead>
                <tr>
                    <td><b>Variable</b></td>
                    <td><b>Keyword</b></td>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>${unix_time}</td>
                    <td>Get Unix Time</td>
                </tr>
            </tbody>
        </table>
        <p><b>Example result:</b><br>
        INFO : ${unix_time} = 1394694526.94</p>
        """
        return time.time()

    def get_timestamp(self, locale="en", time_format="dd-LL-y H:mm:ss.A", *args, **delta):
        """
        <p>Returns current local timestamp in defined format and locale.<br>
        <i>"locale"</i> argument allows to set timestamp languages such as the ISO country and language codes.<br>
        <i>"time_format"</i> argument allows to set timestamp pattern for representation as described below.</p>
        <p><b>Date format:</b></p>
        <table>
            <thead>
                <tr>
                    <td><b>Field</b></td>
                    <td><b>Symbol</b></td>
                    <td><b>Description</b></td>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Era</td>
                    <td>G</td>
                    <td>Replaced with the era string for the current date. One to three letters for the abbreviated form, four letters for the long form, five for the narrow form.</td>
                </tr>
                <tr>
                    <td rowspan="2">Year</td>
                    <td>y</td>
                    <td>Replaced by the year. Normally the length specifies the padding, but for two letters it also specifies the maximum length.</td>
                </tr>
                <tr>
                    <td>Y</td>
                    <td>Same as y but uses the ISO year-week calendar.</td>
                </tr>
                <tr>
                    <td rowspan="2">Quarter</td>
                    <td>Q</td>
                    <td>Use one or two for the numerical quarter, three for the abbreviation, or four for the full name.</td>
                </tr>
                <tr>
                    <td>q</td>
                    <td>Use one or two for the numerical quarter, three for the abbreviation, or four for the full name.</td>
                </tr>
                <tr>
                    <td rowspan="2">Month</td>
                    <td>M</td>
                    <td>Use one or two for the numerical month, three for the abbreviation, or four for the full name, or five for the narrow name.</td>
                </tr>
                <tr>
                    <td>L</td>
                    <td>Use one or two for the numerical month, three for the abbreviation, or four for the full name, or 5 for the narrow name.</td>
                </tr>
                <tr>
                    <td rowspan="2">Week</td>
                    <td>w</td>
                    <td>Week of year.</td>
                </tr>
                <tr>
                    <td>W</td>
                    <td>Week of month.</td>
                </tr>
                <tr>
                    <td rowspan="3">Day</td>
                    <td>d</td>
                    <td>Day of month.</td>
                </tr>
                <tr>
                    <td>D</td>
                    <td>Day of year.</td>
                </tr>
                <tr>
                    <td>F</td>
                    <td>Day of week in month.</td>
                </tr>
                <tr>
                    <td rowspan="2">Week day</td>
                    <td>E</td>
                    <td>Day of week. Use one through three letters for the short day, or four for the full name, or five for the narrow name.</td>
                </tr>
                <tr>
                    <td>e</td>
                    <td>Local day of week. Same as E except adds a numeric value that will depend on the local starting day of the week, using one or two letters.</td>
                </tr>
            </tbody>
        </table>
        <p><b>Time format:</b></p>
        <table>
            <thead>
                <tr>
                    <td><b>Field</b></td>
                    <td><b>Symbol</b></td>
                    <td><b>Description</b></td>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Period</td>
                    <td>a</td>
                    <td>AM or PM.</td>
                </tr>
                <tr>
                    <td rowspan="4">Hour</td>
                    <td>h</td>
                    <td>Hour [1-12].</td>
                </tr>
                <tr>
                    <td>H</td>
                    <td>Hour [0-23].</td>
                </tr>
                <tr>
                    <td>K</td>
                    <td>Hour [0-11].</td>
                </tr>
                <tr>
                    <td>k</td>
                    <td>Hour [1-24].</td>
                </tr>
                <tr>
                    <td>Minute</td>
                    <td>m</td>
                    <td>Use one or two for zero places padding.</td>
                </tr>
                <tr>
                    <td rowspan="3">Second</td>
                    <td>s</td>
                    <td>Use one or two for zero places padding.</td>
                </tr>
                <tr>
                    <td>S</td>
                    <td>Fractional second, rounds to the count of letters.</td>
                </tr>
                <tr>
                    <td>A</td>
                    <td>Milliseconds in day.</td>
                </tr>
                <tr>
                    <td rowspan="4">Timezone</td>
                    <td>z</td>
                    <td>Use one to three letters for the short timezone or four for the full name.</td>
                </tr>
                <tr>
                    <td>Z</td>
                    <td>Use one to three letters for RFC 822, four letters for GMT format.</td>
                </tr>
                <tr>
                    <td>v</td>
                    <td>Use one letter for short wall (generic) time, four for long wall time.</td>
                </tr>
                <tr>
                    <td>V</td>
                    <td>Same as z, except that timezone abbreviations should be used regardless of whether they are in common use by the locale.</td>
                </tr>
            </tbody>
        </table>
        <p><i>"delta"</i> argument allows to set timestamp delta (minus or plus). It allows take one or multiple parameters such as: years, months, weeks, days, hours, minutes, seconds, microseconds.<br>
        <i>"delta"</i> also allows to set specific timestamp parts (year, month, day, hour, minute, second, microsecond).</p>
        <p><b>Example usage:</b></p>
        <table>
            <thead>
                <tr>
                    <td><b>Variable</b></td>
                    <td><b>Keyword</b></td>
                    <td><b>Argument</b></td>
                    <td><b>Argument</b></td>
                    <td><b>Argument</b></td>
                    <td><b>Argument</b></td>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>${timestamp}</td>
                    <td>Get Timestamp</td>
                    <td>locale=rus</td>
                    <td>time_format=dd LLL y H:mm:ss</td>
                    <td></td>
                    <td></td>
                </tr>
                <tr>
                    <td>${timestamp_with_delta}</td>
                    <td>Get Timestamp</td>
                    <td>locale=rus</td>
                    <td>time_format=LLL y H:mm</td>
                    <td>months=-2</td>
                    <td></td>
                </tr>
                <tr>
                    <td>${timestamp_with_delta}</td>
                    <td>Get Timestamp</td>
                    <td>locale=rus</td>
                    <td>time_format=LLL y H:mm</td>
                    <td>months=-2</td>
                    <td>year=2012</td>
                </tr>
            </tbody>
        </table>
        <p><b>Example result:</b><br>
        INFO : ${timestamp} = 13 Март 2014 17:54:57<br>
        INFO : ${timestamp_with_delta} = Янв. 2014 17:54<br>
        INFO : ${delta_and_cpecific_part} = Янв. 2012 17:54</p>
        """
        delta = dict((key, int(value)) for (key, value) in delta.items())
        timestamp = datetime.today() + relativedelta(**delta)
        return format_datetime(timestamp, time_format, locale=locale)

    def get_utc_timestamp(self, locale="en", time_format="dd-LL-y H:mm:ss.A", *args, **delta):
        """
        <p>Returns current UTC timestamp in defined format and locale.<br>
        `Get Utc Timestamp` keyword arguments are the same as `Get Timestamp` arguments.</p>
        <p><b>Example usage:</b></p>
        <table>
            <thead>
                <tr>
                    <td><b>Variable</b></td>
                    <td><b>Keyword</b></td>
                    <td><b>Argument</b></td>
                    <td><b>Argument</b></td>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>${utc_timestamp}</td>
                    <td>Get Utc Timestamp</td>
                    <td>locale=rus</td>
                    <td>time_format=dd LLL y H:mm:ss</td>
                </tr>
            </tbody>
        </table>
        <p><b>Example result:</b><br>
        INFO : ${utc_timestamp} = 13 Март 2014 11:32:58</p>
        """
        delta = dict((key, int(value)) for (key, value) in delta.items())
        timestamp = datetime.utcnow() + relativedelta(**delta)
        return format_datetime(timestamp, time_format, locale=locale)

    def convert_timestamp_format(self, timestamp, time_format, locale="en"):
        """
        <p>Converts timestamp from one format to another.<br>
        <b>Warning!</b> This keyword support only numeric or string with English locale words timestamps.<br>
        <i>"time_format"</i> and <i>"locale"</i> arguments are the same as `Get Timestamp` arguments.</p>
        <p><b>Example usage:</b></p>
        <table>
            <thead>
                <tr>
                    <td><b>Variable</b></td>
                    <td><b>Keyword</b></td>
                    <td><b>Argument</b></td>
                    <td><b>Argument</b></td>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>${timestamp}</td>
                    <td>Get Timestamp</td>
                    <td></td>
                    <td></td>
                </tr>
                <tr>
                    <td>${rus_timestamp}</td>
                    <td>Convert Timestamp Format</td>
                    <td>time_format=dd LLL y H:mm:ss</td>
                    <td>locale=rus</td>
                </tr>
            </tbody>
        </table>
        <p><b>Example result:</b><br>
        INFO : ${timestamp} = 13-03-2014 18:38:07.67087810<br>
        INFO : ${rus_timestamp} = 13 Март 2014 18:38:07</p>
        """
        timestamp = parse(timestamp)
        return format_datetime(timestamp, time_format, locale=locale)