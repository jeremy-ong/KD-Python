from datetime import date, datetime, timedelta, timezone
from functools import total_ordering
from re import match, search
from urllib.parse import urlparse

import numpy as np


class KiURL():
    """Wrapper class for the URL data type.

    Keyword arguments:
    url (str): A string of the URL.

    Attributes:
    url: A ParseResult object of the supplied URL string.
    """
    def __init__(self, url):
        self.url = urlparse(url)

    def __repr__(self):
        return self.url.geturl()


class KiDate():
    """Wrapper class for the Date data type.
    
    Keyword arguments:
    date_ (str): A string of the date.
    dateFormat (str): A strptime format string. Defaults to '%Y/%m/%d'.

    Attributes:
    date_: a Date object of the supplied date.
    """
    def __init__(self, date_, dateFormat='%Y/%m/%d'):
        self.date_ = datetime.strptime(date_, dateFormat).date()

    def __repr__(self):
        return self.date_.strftime('%Y/%m/%d')


class KiLocalDateTime():
    """Wrapper class for the LocalDateTime data type.
    
    Keyword arguments:
    datetime_ (str): A string in KTS Local Date Time format.
        ISO format also accepted.

    Attributes:
    datetime_: A numpy datetime64 object.
    """
    def __init__(self, datetime_):
        self.datetime_ = datetime_.replace('/', '-').replace('@', 'T').replace(' ', '')
        self.datetime_ = np.datetime64(self.datetime_)
        print(self)

    def __repr__(self):
        return str(self.datetime_).replace('-', '/').replace('T', '@')


class KiZonedDateTime():
    """Wrapper class for the ZonedDateTime data type.
    
    Keyword arguments:
    datetime_ (str): A string of the date and time, including timezone.
        Timezone must be of format (+|-)hours(:minutes)? or (+|-)KiTZ and should be appended
        directly to the datetime string (ex. 2015/01/12@02:04:23+4)
    datetimeFormat (str): A strptime format string. Defaults to '%Y/%m/%d@%H:%M:%S'.

    Attributes:
    datetime_: A DateTime object of the supplied date and time, including timezone.
    """
    _timezones = {
        'AR/ART': -3, 'AU/ACST': 9.5, 'AU/ACDT': 10.5, 'AU/AEST': 10, 'AU/AEDT': 11,
        'AU/AWST': 8, 'AU/NFT': 11, 'AU/NFDT': 12, 'BR/ACT': -5, 'BR/AMT': -4,
        'BR/BRT': -3, 'BR/FNT': -2, 'CA/AST': -4, 'CA/ADT': -3, 'CA/CST': -6, 'CA/CDT': -5,
        'CA/EST': -5, 'CA/EDT': -4, 'CA/MST': -7, 'CA/MDT': -6, 'CA/NST': -3.5,
        'CA/NDT': -2.5, 'CA/PST': -8, 'CA/PDT': -7, 'CN/CST': 8, 'CO/COT': -5,
        'CZ/CET': 1, 'CZ/CEST': 2, 'EG/EET': 2, 'ET/EAT': 3, 'FR/CET': 1,
        'FR/CEST': 2, 'DE/CET': 1, 'DE/CEST': 2, 'GR/EET': 2, 'GR/EEST': 3,
        'IN/IST': 5.5, 'ID/WIB': 7, 'ID/WITA': 8, 'ID/WIT': 9, 'IR/IRST': 3.5,
        'IR/IRDT': 4.5, 'IQ/AST': 3, 'IE/IST': 1, 'IT/CET': 1, 'IT/CEST': 2,
        'JP/JST': 9, 'KE/EAT': 3, 'MX/CST': -6, 'MX/CDT': -5, 'MX/EST': -5,
        'MX/MST': -7, 'MX/MDT': -6, 'MX/PST': -8, 'MX/PDT': -7, 'NL/CET': 1,
        'NL/CEST': 2, 'NL/AST': -4, 'NZ/NZST': 12, 'NZ/NZDT': 13, 'NG/WAT': 1,
        'PK/PST': 5, 'PL/CET': 1, 'PL/CEST': 2, 'RO/EET': 2, 'RO/EEST': 3,
        'RU/KALT': 2, 'RU/MSK': 3, 'RU/SAMT': 4, 'RU/YEKT': 5, 'RU/OMST': 6,
        'RU/KRAT': 7, 'RU/IRKT': 8, 'RU/YAKT': 9, 'RU/VLAT': 10, 'RU/MAGT': 11,
        'RU/PETT': 12, 'SA/AST': 3, 'SG/SST': 8, 'ZA/SAST': 2, 'KR/KST': 9,
        'ES/CET': 1, 'ES/CEST': 2, 'SE/CET': 1, 'SE/CEST': 2, 'CH/CET': 1,
        'CH/CEST': 2, 'TR/FET': 3, 'UA/EET': 2, 'UA/EEST': 3, 'UTC': 0, 'GB/DST': 1,
        'US/AST': -4, 'US/AKST': -9, 'US/AKDT': -8, 'US/CHST': 10, 'US/CST': -6,
        'US/CDT': -5, 'US/EST': -5, 'US/EDT': -4, 'US/HST': -10, 'US/MST': -7,
        'US/MDT': -6, 'US/PST': -8, 'US/PDT': -7, 'US/SST': -11, 'Z': 0
    }

    def __init__(self, datetime_, dateFormat='%Y/%m/%d@%H:%M:%S'):
        datetime_timezone = match('(.+)([+-]([\d]+(:\d+)?|[a-zA-Z/]+))', datetime_)
        self.datetime_ = datetime.strptime(datetime_timezone.group(1), dateFormat)
        tz = datetime_timezone.group(2)
        offset_parsed = match('([+-])(\d+)(:\d+)?', tz)
        if offset_parsed:
            offset = int(offset_parsed.group(2))
            if offset_parsed.group(3):
                offset += int(offset_parsed.group(3)[1:]) / 60
            if offset_parsed.group(1) == '-':
                offset *= -1
        elif tz[1:] in self._timezones:
            offset = self._timezones[tz[1:]]
        else:
            raise ValueError('Invalid timezone')

        delta = timedelta(hours=offset)
        tz_object = timezone(delta)
        self.datetime_ = self.datetime_.replace(tzinfo=tz_object)


    def __repr__(self):
        tz = self.datetime_.tzinfo
        delta = tz.utcoffset(None)
        seconds = delta.total_seconds()
        operator = '+' if seconds >= 0 else '-'
        if seconds < 0:
            seconds *= -1
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        minutes = '' if minutes == 0 else ':' + str(minutes)
        return '{}{}{}{}'.format(self.datetime_.strftime('%Y/%m/%d@%H:%M:%S'), operator, hours, minutes)


class KiDuration():
    """Wrapper class for the Duration data type.
    
    Keyword arguments:
    duration (str): A string of the duration in KTS Duration format.

    Attributes:
    duration: A list of numpy timedelta64 objects of the specified duration.
    """
    def __init__(self, duration):
        tokens = duration.split(':')
        self.duration = []
        if 'days' in tokens[0]:
            self.duration.append(np.timedelta64(search('\d+', tokens[0]).group(0), 'D'))
            del tokens[0]
        self.duration.append(np.timedelta64(tokens[0], 'h'))
        self.duration.append(np.timedelta64(tokens[1], 'm'))
        self.duration.append(np.timedelta64(search('(\d+)(\.)?', tokens[2]).group(1), 's'))
        if '.' in tokens[2]:
            fractional = search('\.(\d+)', tokens[2]).group(1)[:9]
            print(fractional)
            if len(fractional) > 6:
                while len(fractional) < 9:
                    fractional += '0'
                self.duration.append(np.timedelta64(fractional, 'ns'))
            elif len(fractional) > 3:
                while len(fractional) < 6:
                    fractional += '0'
                self.duration.append(np.timedelta64(fractional, 'us'))
            else:
                while len(fractional) < 3:
                    fractional += '0'
                self.duration.append(np.timedelta64(fractional, 'ms'))

    def __repr__(self):
        pass


@total_ordering
class KiVersion():
    """Wrapper class for the Version data type.
    
    Keyword arguments:
    version (str): A string of the version.

    Attributes:
    version:: A 5-tuple containing the version components (major, minor, micro, qualifier, qualifierNumber).
    """
    def __init__(self, version):
        self.version = _parse_version(version)

    def __lt__(self, other):
        # Make copies so we don't overwrite existing None values.
        version_self = list(self.version)
        version_other = list(other.version)

        for i in range(3):
            if version_self[i] is None:
                version_self[i] = 0
            if version_other[i] is None:
                version_other[i] = 0
            if version_self[i] < version_other[i]:
                return True
            if version_self[i] > version_other[i]:
                return False

        if version_self_str < version_other_str:
            return True
        if version_self_str > version_other_str:
            return False
        if version_self[3] is not None and version_other[3] is None:
            return True
        if version_self[3] is None and version_other[3] is not None:
            return False
        if version_self[3] is not None and version_other[3] is not None:
            if version_self[3] < version_other[3]:
                return True
            if version_self[3] > version_other[3]:
                return False

        if version_self[4] is None:
            version_self[4] = 0
        if version_other[4] is None:
            version_other[4] = 0
        if version_self[4] < version_other[4]:
            return True
        if version_self[4] > version_other[4]:
            return False

        return False

    def __eq__(self, other):
        # Make copies so we don't overwrite existing None values.
        version_self = list(self.version)
        version_other = list(other.version)

        for i in range(5):
            if version_self[i] is None:
                version_self[i] = 0
            if version_other[i] is None:
                version_other[i] = 0
            if version_self[i] != version_other[i]:
                return False

        return True

    def _parse_version(version):
        major = match('(\d+)(\.|-|$)', version).group(1)
        minor = match('\d+\.(\d+)(\.|-|$)', version).group(1)
        micro = match('\d+\.\d+\.(\d+)(-|$)', version).group(1)
        qualifier = match('\d+\.\d+\.\d+-([a-zA-Z]+)(\d|-|$)', version).group(1)
        qualifierNumber = match('\d+\.\d+\.\d+-[a-zA-Z]+-{0,1}(\d+)$', version).group(1)

        return (major, minor, micro, qualifier, qualifierNumber)
