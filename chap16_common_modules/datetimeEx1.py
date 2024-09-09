#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' an exercise of multiprocessing'

__author__ = 'victor yu'

import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):

    #parse the datetime string into a native datatime object
    t=datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    
    #parse the timezone string like 'UTC+7:00
    offseth=re.match(r'^(UTC)(\+|\-)(\d{1,2})', tz_str).groups()


    print('offseth[1]',offseth[1])
    print('offseth[2]',offseth[2])

    
    sign= 1 if offseth[1] == '+' else -1
    offset=timedelta(hours=sign*int(offseth[2]))

    tz_info = timezone(offset)

    #convert the above native datetime object into a timezone aware datetime object
    local_time=t.replace(tzinfo=tz_info)

    print('local time with timezone', local_time)

    #convert the timezone aware datetime object into UTC datetime object
    utc_time = local_time.astimezone(timezone.utc)

    return utc_time.timestamp()

    

# Test:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')