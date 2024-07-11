from datetime import datetime

time = datetime.now()
print(time.strftime('%Y/%m/%d %H:%M:%S'))
print(time.strftime('%y/%B/%d %H:%M:%S %p'))
print(time.strftime('%a, %Y %b %d'))
print(time.strftime('%A, %Y %B %d'))
print('Weekday: ',time.isoweekday())
print('Day of the year: ',time.strftime('%j'))
print('Week number of the year: ',time.strftime('%U'))