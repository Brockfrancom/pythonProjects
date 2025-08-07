import datetime
from datetime import datetime
from datetime import timedelta
import string

def month_last_day(dt):
    while True:
        day = int(dt.strftime('%d'))
        dPlusOne = dt + timedelta(days=1)
        day2 = int(dPlusOne.strftime('%d'))
        if day2 == 01:
            return day
        dt = dPlusOne

print month_last_day(datetime(2013, 8, 4))
