import pandas as pd
import sys
import datetime
from datetime import timedelta
parse_dates = ['time']
all_data = pd.read_csv(sys.argv[1], parse_dates=parse_dates)
dates = {}
count = 0
for date in all_data["time"]:
    if dates.has_key(date):
        dates[date] = dates[date] + 1
    else:
        dates[date] = 1
dates_used = dates.copy()
for date in all_data["time"]:
    print(date + datetime.timedelta(milliseconds= float("%.2f" % (dates[date] - dates_used[date] * (1000 / dates[date])))) )
    date_temp = date + datetime.timedelta(milliseconds= float("%.2f" % (dates[date] - dates_used[date] * (1000 / dates[date]))) )
    dates_used[date] = dates_used[date] - 1
    date = date_temp
all_data.to_csv(sys.argv[1])