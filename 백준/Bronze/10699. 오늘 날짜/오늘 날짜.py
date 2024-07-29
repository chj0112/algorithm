import datetime

tm = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
print(tm.strftime('%Y-%m-%d'))